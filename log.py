import logging as log
import time
import os

class Logger():
    def __init__(self):
        if not os.path.exists("Log/"):
            os.makedirs("Log/")
        self.logPath = r"Log/"
        self.logName = time.strftime("log_%Y%m%d_%H%M.txt")
        self.logFile = self.logPath + self.logName
        log.basicConfig(
            level=log.DEBUG,  # CRITICAL > ERROR > WARNING > INFO > DEBUG
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s:  %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename=self.logFile,
            filemode='a')
    def Info(self,content):
        log.info(content)

    def Error(self,content):
        log.error(content,exc_info=True)

