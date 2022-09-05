from pill_pack_dashboard.config import Config
from ppd_flask.models import fill_lists
from sqlalchemy import create_engine
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import platform

dbURL = Config.SQLALCHEMY_DATABASE_URI
engine = create_engine(DBURL, echo=True, future=True)
opSys = platform.system()
path = Config.PATH_TO_WATCH

if opSys == 'Darwin':
    driver = webdriver.Safari()
else:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


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

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        
        print(event) # Your code here
        print(f'The file path is: {event.src_path}')