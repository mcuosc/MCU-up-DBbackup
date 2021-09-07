import logging as log
import time

class Logger():
    def __init__(self):
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
        log.error(content,)

