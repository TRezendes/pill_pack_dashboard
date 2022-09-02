from pill_pack_dashboard.config import Config
from .models import
from
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path = Config.PATH_TO_WATCH

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
