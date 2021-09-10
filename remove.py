import os
import time
import log 

Log = log.Logger()

def removeOldFile(Day,Path):
    rmTime = time.time() - 3600 * 24 * Day
    
    for file in os.listdir(Path):
        filename = Path + os.sep +file
        if os.path.getmtime(filename) < rmTime:
            try:
                if os.path.isfile(filename):
                    os.remove(filename)
                    Log.Info('Removing old file : '+filename)
                else:
                    Log.Info('File not found')
            except:
                Log.Error('Delete file error')