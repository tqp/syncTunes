import os
import win32com.client

iTunes = win32com.client.Dispatch("iTunes.Application")

mainLibrary = iTunes.LibraryPlaylist
tracks = mainLibrary.Tracks
numTracks = tracks.Count
print("Number of Tracks: " + str(numTracks))

srcDirectory = "C:\_TQP\Temp"

for dirPath, dirs, files in os.walk(srcDirectory):
    for file in files:
        if file.endswith(".mp3"):
            srcFilePath = srcDirectory + "\\" + file
            # print("[" + time.ctime(os.path.getmtime(dirPath + "\\" + file)) + "] " + dirPath + "\\" + file)

            print(file)

            # print(dirs)
            # for dir in dirs:
            #     if not dir.startswith("."):
            #         print(dir)
            #         iTunes.CreatePlaylist(dir)
            #
            # mainLibrary.AddFile(dirPath + "\\" + file)
