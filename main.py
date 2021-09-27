from backup import backup
import time
from remove import removeOldFile

def main():
    while(True):
        if backup():
            print("Data is already save on "+time.strftime("%Y/%m/%d %H:%M:%S"))
            removeOldFile(5,'Data') # removeOldFile(Day,Path)
            time.sleep(3600*3)
        else:
            print("An error occurred. Please to check log file.")
            time.sleep(10)

main()
