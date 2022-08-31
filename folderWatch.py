import sys
import time
import logging
from config import Config
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

path=Config.PATH_TO_WATCH

#Example: log all changes, recursive
# from https://pythonhosted.org/watchdog/quickstart.html#a-simple-example
'''
if __name__ == "__main__":

    # logging.basicConfig(level=logging.INFO,
    #                     format='%(asctime)s - %(message)s',
    #                     datefmt='%Y-%m-%d %H:%M:%S')
    # # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    # event_handler = LoggingEventHandler()
    # observer = Observer()
    # observer.schedule(event_handler, path, recursive=True)
    # observer.start()
    # try:
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()
    # observer.join()

    handler = FileSystemEventHandler()
    observer.schedule(handler, path, recursive=True)
    observer.start()
    filePath = handler.on_created()
    '''


#Example code from https://philipkiely.com/code/python_watchdog.html
class Watcher:

    def __init__(self, directory=".", handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(
            self.handler, self.directory, recursive=True)
        self.observer.start()
        print("\nWatcher Running in {}/\n".format(self.directory))
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated\n")


class MyHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event) # Your code here
        print(f'The file path is: {event.src_path}')

if __name__=="__main__":
    w = Watcher(path, MyHandler())
    w.run()
