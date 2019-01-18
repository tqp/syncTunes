# Must have python_magic installed to use eyed3

import os
import time
import eyed3
import win32com.client

iTunes = win32com.client.Dispatch("iTunes.Application")
# srcDirectory = "C:\_TQP\Temp"
srcDirectory = "Z:\MUSIC\iPod Music"
eyed3.log.setLevel("ERROR")


def check_modified_time(src_file, dst_file):
    src_time = time.ctime(os.path.getmtime(src_file))
    dst_time = time.ctime(os.path.getmtime(dst_file))
    # print("Source Modified: " + srcTime)
    # print("Destination Modified: " + dstTime)
    return src_time > dst_time


# GENERAL USE: RENAME FILE
def rename_file(reason, dir_path, filename1, change_from, change_to):
    data1 = filename1.replace(".mp3", "").split("-")
    artist1 = data1[0].strip()
    title1 = data1[1].strip()
    # print("Artist: " + artist1)
    # print("Title: " + title1)
    artist1 = artist1.replace(change_from, change_to)
    title1 = title1.replace(change_from, change_to)
    new_filename = "{0} - {1}.mp3".format(artist1, title1)
    print("Renaming (" + reason + "): '" + filename1 + "' to '" + new_filename + "'" + " [" + dir_path + "]")
    os.rename(dir_path + "\\" + filename1, dir_path + "\\" + new_filename)


# GENERAL USE: DELETE FILE
def delete_file(src_file_path):
    print("Delete File: " + src_file_path)
    os.remove(src_file_path)


def is_valid_filename(file_name):
    valid = True
    if "lyric" in file_name.lower():
        print("WARNING: The word 'lyric' appears in the filename.")
        valid = False
    if "-" not in file_name.lower():
        valid = False
    if " - " not in file_name.lower():
        valid = False
    return valid


# HIGHLIGHT STRING IN FILENAME
def highlight_list():
    highlight_strings = {

    }
    return highlight_strings


def highlight_files(dir_path, file_name):
    if any(substring in file_name for substring in highlight_list()):
        print("Highlight: " + dir_path + "\\" + file_name)


# RENAME INCORRECT FILENAMES
def rename_incorrect_filenames(dir_path, file_name):
    if " - " not in file_name.lower():
        rename_file("Dash Missing", dir_path, file_name, "-", " - ")


# STANDARDIZE CAPITALIZATION IN FILENAME
def standardize_capitalization_exceptions_list():
    exceptions_list = {
        'The A Team'
    }
    return exceptions_list


def standardize_capitalization_word_list():
    exceptions_list = {
        'A', "An", "At", "And", "But", "By", "For", "From", "Of", "The"
    }
    return exceptions_list


def standardize_capitalization(dir_path, file_name):
    split = file_name.replace(".mp3", "").split("-")
    artist = split[0].strip()
    title = split[1].strip()

    if any(substring not in file_name for substring in standardize_capitalization_exceptions_list()):
        for substring in standardize_capitalization_word_list():
            if " " + substring + " " in artist or " " + substring + " " in title:
                rename_file("Capitalization", dir_path, file_name, " " + substring + " ", " " + substring.lower() + " ")


# UPDATE ID3 TAGS
def update_id3_tags(dir_path, file_name):
    data = file_name.split("-")
    # artist = data[0].strip()
    # title = data[1].strip()
    # print("Artist (from file): " + data[0].strip())
    # print("Title (from file) : " + data[1].strip())
    # print("Genre (from dir)  : " + os.path.basename(dir_path))

    # Set ID3 tags from filename and directory
    audio_file = eyed3.load(dir_path + "\\" + file_name)
    try:
        audio_file.initTag()
        audio_file.tag.artist = data[0].strip()
        audio_file.tag.title = data[1].strip()
        audio_file.tag.genre = os.path.basename(dir_path)
        audio_file.tag.album = u"TQP Album"
        audio_file.tag.comments.set("TQP")
        audio_file.tag.save()
    except AttributeError:
        print("Exception: " + dir_path + "\\" + file_name)


def sync_folders_and_playlists():
    print("\nSyncing folders and playlists...")
    # Loop through folders to see if a playlist exists for each one.
    for dir_path, dirs, files in os.walk(srcDirectory):
        # print("\n")
        # print("dir_path: " + dir_path)

        for dir_name in dirs:
            folder_playlist_name = dir_name
            # folder_playlist_name = dir_path.replace(srcDirectory, "").replace("\\", "", 1).replace("\\", " - ")
            # print("folder_playlist_name: " + folder_playlist_name)

            if len(folder_playlist_name) > 0:

                # Does this folder name match a playlist?
                if not iTunes.LibrarySource.Playlists.ItemByName(folder_playlist_name):
                    print("There is no playlist called '" + folder_playlist_name + "'. Creating playlist...")
                    iTunes.CreatePlaylist(folder_playlist_name)

    # Loop through playlists to see if a folder exists for each one.
    playlist_delete_exceptions_list = {
        'Library', 'Music', 'Movies', 'TV Shows', 'Podcasts', 'Audiobooks', 'Genius'
    }
    delete_list = list()
    for playlist in iTunes.LibrarySource.Playlists:
        if not any(substring == playlist.Name for substring in playlist_delete_exceptions_list):
            if not any(dir_path.endswith(playlist.Name) for dir_path, dirs, files in os.walk(srcDirectory)):
                playlist_to_delete = playlist.Name
                # Add playlists not found to the list to delete. Deleting them directly here doesn't fully work.
                delete_list.append(playlist_to_delete)

    # Delete playlists that were not found.
    for item in delete_list:
        print("There is no directory named '" + item + "'. Deleting playlist...")
        iTunes.LibrarySource.Playlists.ItemByName(item).Delete()
    print("Done.")


def analyze_file_names():
    print("\nAnalyzing file names...")
    for dir_path, dirs, files in os.walk(srcDirectory):
        for file_name in files:
            src_file_path = srcDirectory + "\\" + file_name
            # print("File: " + src_file_path);
            if file_name.endswith(".mp3"):
                # print("---------------------------")
                # print("[" + time.ctime(os.path.getmtime(dirPath + "\\" + filename)) + "] "
                # + dirPath + "\\" + filename)
                rename_incorrect_filenames(dir_path, file_name)
                highlight_files(dir_path, file_name)
                standardize_capitalization(dir_path, file_name)
                update_id3_tags(dir_path, file_name)
            elif file_name.endswith(".m4a"):
                print("- M4A file found: " + src_file_path)
                # else:
                # print("Non-mp3 file found: " + src_file_path)
                #     if file_name.startswith("AlbumArt_"):
                #         delete_file(src_file_path)
    print("Done.")


def sync_files_and_songs():
    print("\nSyncing files and songs...\n")
    for dir_path, dirs, files in os.walk(srcDirectory):
        print("dir_path: " + dir_path)

        print("Genre Name: " + dir_path
              .replace(srcDirectory + "\\", "")
              .replace("\\", " - ") + "\n")
        # for dir_name in dirs:
        #     print("dir_name: " + dir_name)

        # mainLibrary = iTunes.LibraryPlaylist
        # dirPath = "C:\_TQP\Temp"
        # file =
        # mainLibrary.AddFile(dirPath + "\\" + file)
        # print("Done.")


# MAIN PROGRAM
def main():
    sync_folders_and_playlists()
    analyze_file_names()
    # sync_files_and_songs()


main()
