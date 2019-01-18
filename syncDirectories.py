import os
import time
from shutil import copyfile

srcDirectory = "C:\Temp\dir1"
dstDirectory = "C:\Temp\dir2"


def check_modified_time(srcFile, dstFile):
    srcTime = time.ctime(os.path.getmtime(srcFile))
    dstTime = time.ctime(os.path.getmtime(dstFile))
    # print("Source Modified: " + srcTime)
    # print("Destination Modified: " + dstTime)
    return srcTime > dstTime

for dirPath, dirs, files in os.walk(srcDirectory):
    for file in files:
        print("----------------")

        srcFilePath = srcDirectory + "\\" + file
        dstFilePath = dstDirectory + "\\" + file

        print("[" + time.ctime(os.path.getmtime(dirPath + "\\" + file)) + "] " + file)
        if not os.path.isfile(dstDirectory + "\\" + file):
            print(dstFilePath + " needs to be copied.")
            copyfile(srcFilePath, dstDirectory + "\\" + file)
        else:
            if check_modified_time(srcFilePath, dstFilePath):
                print(dstFilePath + " was updated.")
                copyfile(srcFilePath, dstFilePath)
            else:
                print("No updates needed.")
