from logging.handlers import TimedRotatingFileHandler
import os
from datetime import datetime

class CustomTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, dir_name, when, interval, backupCount):
        self.dir_name = dir_name
        self.when = when
        self.interval = interval
        self.backupCount = backupCount
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        filename = self.generate_filename()
        super().__init__(filename, when, interval, backupCount)

    def generate_filename(self):
        return os.path.join(self.dir_name, f'walkthetalk-{self.current_date}.log')

    def emit(self, record):
        new_date = datetime.now().strftime("%Y-%m-%d")
        if new_date != self.current_date:
            self.current_date = new_date
            self.baseFilename = self.generate_filename()
        super().emit(record)

