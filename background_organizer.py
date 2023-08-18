import time
import os
import shutil

source_dir = "C:\\Users\\Jonmc\\Downloads"
destination_dir = "C:\\Users\\Jonmc\\OneDrive\\Documents\\Cover Letters"

while True:
    os.chdir(source_dir)
    files = os.listdir()
    numFiles = len(files)
    time.sleep(60)
    new_files = [file for file in os.listdir() if file not in files]

    for file in new_files:
        if "Cover Letter" in file:
            # Get the creation time of the file
            file_path = os.path.join(source_dir, file)
            creation_time = os.path.getctime(file_path)
            
            # Calculate the time since August 1, 2023
            time_since_august_1 = creation_time - 1690848000
            
            if time_since_august_1 > 0:
                shutil.move(file_path, os.path.join(destination_dir, file))
                print(f"Moved '{file}' to '{destination_dir}'")
