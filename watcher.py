'''
MIT License

Copyright (c) 2022 Timothy Rezendes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os
import time
import platform
from config import Config
from selenium import webdriver
from sqlalchemy.orm import Session
from watchdog.observers import Observer
from sqlalchemy.orm import declarative_base
from watchdog.events import FileSystemEventHandler
from sqlalchemy import create_engine, select, Table, update

#with open('../config.py') as config:
#    from config import Config

# Initialize variables
dbURL = Config.SQLALCHEMY_DATABASE_URI
engine = create_engine(dbURL, echo=True, future=True)
Base = declarative_base()
opSys = platform.system()
path = Config.PATH_TO_WATCH
facilityList = []


# Reflect database table(s) created by the flask application
Base.metadata.reflect(engine)

class fill_lists(Base):
    __table__ = Base.metadata.tables['fill_lists']

# Initialize Selenium web driver
## Safari driver is built into MacOS
if opSys == 'Darwin':
    ## Unfortunately, Safari does not allow an automated browser window to be interacted with…
    # driver = webdriver.Safari()
    ## …so we're going to have to use Firefox
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from webdriver_manager.firefox import GeckoDriverManager
    
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
## Get latest Chrome driver if not on a Mac
else:
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Code for the Watcher and MyHandler classes is adapted from https://philipkiely.com/code/python_watchdog.html
class Watcher:
    def __init__(self, directory=".", handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory
    
    def run(self):
        self.observer.schedule(self.handler, self.directory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()

# Database query to generate facility list
with Session(engine) as session:
    stmt = select(fill_lists.list_export_name)
    result = session.execute(stmt)
    for facility in result:
        facilityList.append(facility.list_export_name)


class MyHandler(FileSystemEventHandler):
    driver.get("http://127.0.0.1:5000/dashboard")
    def on_created(self, event):
        fullFilePath=event.src_path
        fileName=fullFilePath.rsplit(os.sep, 1)[-1]
        if fileName in facilityList:
            with Session(engine) as session:
                stmt = update(fill_lists).where(fill_lists.list_export_name == fileName).values(exported=True)
                session.execute(stmt)
                session.commit()
        time.sleep(.5)
        driver.refresh()
        
if __name__ == '__main__':
    w = Watcher(path, MyHandler())
    w.run()
