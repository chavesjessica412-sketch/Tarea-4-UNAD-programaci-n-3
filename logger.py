import datetime

class Logger:
    def __init__(self, file="logs.txt"):
        self.file = file

    def log(self, level, message):
        with open(self.file, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now()}] {level}: {message}\n")

logger = Logger()