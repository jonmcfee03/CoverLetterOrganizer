import os
import shutil
from pathlib import Path

print("Og", os.getcwd())

os.chdir("/mnt/c/Users/Jonmc/Downloads")

files = os.listdir()

source_dir = "/mnt/c/Users/Jonmc/Downloads"
destination_dir = "/mnt/c/Users/Jonmc/OneDrive/Documents/Cover Letters"

for file in files:
    if "Cover Letter" in file:
        #time since august 1, 2023
        time = os.path.getctime(file) - 1690848000
        print(time)
        if time > 0:
            shutil.move(os.path.join(source_dir, file), destination_dir)