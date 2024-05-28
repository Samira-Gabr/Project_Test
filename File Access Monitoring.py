#Use Python's watchdog library to monitor file system changes.
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class FileMonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'File modified: {event.src_path}')
        # Log event or send alert

    def on_created(self, event):
        print(f'File created: {event.src_path}')
        # Log event or send alert

if __name__ == "__main__":
    path = "/path/to/directory"
    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

