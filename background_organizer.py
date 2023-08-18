import time
import os
import shutil

while True:
    numFiles = len(os.listdir("C:\Users\Jonmc\Downloads"))
    time.sleep(60)
    oldNumFiles = numFiles
    numFiles = len(os.listdir("C:\Users\Jonmc\Downloads"))
    if numFiles != oldNumFiles:
        os.chdir('C:\\Users\\Jonmc\\Downloads')

        files = os.listdir()

        source_dir = 'C:\\Users\\Jonmc\\Downloads'
        destination_dir = "C:\\Users\\Jonmc\\OneDrive\\Documents\\Cover Letters"

        for file in files:
            if "Cover Letter" in file:
                #time since august 1, 2023
                time = os.path.getctime(file) - 1690848000
                if time > 0:
                    shutil.move(os.path.join(source_dir, file), destination_dir)