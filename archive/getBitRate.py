# Windows: "Files" are in "Folders"
# iTunes: "Songs" are in "Libraries" or "Playlists"

import win32com.client
import os
import eyed3

eyed3.log.setLevel("ERROR")
iTunes = win32com.client.Dispatch("iTunes.Application")

def get_exclude_suffix_list():
    return {
        '.m4a', '.db', '.ini', '.jpg', '.cbsync'
    }

def exclude_files_with_suffix(root, files, excluded_suffixes):
    files_excluded = []
    for file in files:
        if not any(substring in file for substring in excluded_suffixes):
            files_excluded.append(file)
        # else:
        #     print("Excluding (Suffix): " + os.path.join(root, file))
    return files_excluded


def exclude_files_containing_substring(root, files, excluded_substrings):
    files_excluded = []
    for file in files:
        if not any(substring in file for substring in excluded_substrings):
            files_excluded.append(file)
        else:
            print("Excluding (Substring): " + os.path.join(root, file))
    return files_excluded


def list_files(path):
    for root, dirs, files in os.walk(path):
        print("\n----- " + root + "-----")
        files = exclude_files_with_suffix(root, files, get_exclude_suffix_list())
        for file_name in files:

            print(os.path.join(root, file_name))

            audiofile = eyed3.load(root + "\\" + file_name)
            print(audiofile.info.bit_rate[1])

            # try:
            #     print(os.path.join(root, file_name))
            #
            #     audiofile = eyed3.load(root + "\\" + file_name)
            #     # print(audiofile.tag.artist)
            #     # print(audiofile.tag.album)
            #     # print(audiofile.tag.title)
            #     # print(audiofile.tag)
            #     for property1, value in vars(audiofile.tag).iteritems():
            #         print("property: " + property1 + ", value: " + value)
            # except AttributeError:
            #     print("TQP AttributeError: " + root + "\\" + file_name)

# MAIN PROGRAM
# rootDir = "Z:\\MUSIC\\iPod Music"
rootDir = "C:\\_TQP\Temp"
# rootDir = "Z:\\MUSIC\\Non-Synched Mixes"

list_files(rootDir)
