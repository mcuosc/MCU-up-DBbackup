from backup import backup
import time
import logging as log

def main():
    while(True):
        if backup():
            print("Data is already save on "+time.strftime("%Y/%m/%d %H:%M:%S"))
            time.sleep(3600)
        else:
            print("An error occurred")
            time.sleep(10)

main()
