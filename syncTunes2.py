# Windows: "Files" are in "Folders"
# iTunes: "Songs" are in "Libraries" or "Playlists"

import win32com.client
import os
import eyed3

eyed3.log.setLevel("ERROR")
iTunes = win32com.client.Dispatch("iTunes.Application")

# TODO
# Copy File to Library
# Delete Song from Library
# Add Song to Playlist
# Remove Song from Playlist


# === TOOLS ===

def create_playlist(playlist_name):
    print("Create Playlist: " + playlist_name)
    iTunes.CreatePlaylist(playlist_name)


def delete_playlist(playlist_name):
    print("Delete Playlist: " + playlist_name)
    iTunes.LibrarySource.Playlists.ItemByName(playlist_name).Delete()


def delete_all_playlists():
    print("Delete All Playlists")
    playlist_list = list()
    for playlist in iTunes.LibrarySource.Playlists:
        playlist_delete_exceptions_list = {
            'Library', 'Music', 'Movies', 'TV Shows', 'Podcasts', 'Audiobooks', 'Genius'
        }
        if not any(substring == playlist.Name for substring in playlist_delete_exceptions_list):
            # Add playlists not found to the list to delete. Deleting them directly here doesn't fully work.

            playlist_list.append(playlist.Name)

    print(playlist_list)
    for playlist in playlist_list:
        delete_playlist(playlist)


def delete_file(file_path):
    print("Deleting File: " + file_path)
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print("FileNotFoundError: " + file_path)
    except Exception:
        print("Exception: " + file_path)


def rename_file(reason, root, file_name, change_from, change_to):
    print("Renaming File (" + reason + "): ")


# === DERIVED FILE FUNCTIONS ===


def include_files_by_conditions(files):
    include_suffixes = {'.mp3'}
    files = [file for file in files if any(file.endswith(suffix) for suffix in include_suffixes)]
    return files


def exclude_files_by_conditions(files):
    exclude_suffixes = {'.ini', '.db'}
    files = [file for file in files if not any(file.endswith(suffix) for suffix in exclude_suffixes)]
    exclude_substring = {}
    files = [file for file in files if not any(file.endswith(suffix) for suffix in exclude_substring)]
    return files


def find_bad_suffixes(files):
    bad_suffixes = {'.m4a'}
    bad_files = [file for file in files if any(file.endswith(suffix) for suffix in bad_suffixes)]
    return bad_files


def print_files_with_substring(root, file_name):
    substring_list = {'and'}
    if file_name.endswith(".mp3"):
        if any(substring in file_name for substring in substring_list):
            print("Highlight: " + root + "\\" + file_name)


def delete_files_with_suffix(root, file_name):
    included_suffixes = {'.jpg'}
    if any(file_name.endswith(suffix) for suffix in included_suffixes):
        print(os.path.join(root, file_name))
        delete_file(os.path.join(root, file_name))


# === TEMPLATES ===

def loop_through_all_folders_in_tree(path):
    excluded_folders = {'.cbsync', "_gsdata_"}
    for root, dirs, files in os.walk(path):
        for dirs_name in dirs:
            # Perform derived folder actions
            if not any(substring == dirs_name for substring in excluded_folders):
                print(dirs_name)


def loop_through_all_files_in_tree(path):
    # excluded_suffixes = {'.gss', '._gs', '.gsl', '.db', '.log'}
    # if not any(file_name.endswith(suffix) for suffix in excluded_suffixes):
    for root, dirs, files in os.walk(path):
        print("\n----- " + root + "-----")

        files_with_bad_suffixes = find_bad_suffixes(files)
        for file_name in files_with_bad_suffixes:
            print(os.path.join(root, file_name))


# === FILE ARRAY ACTIONS ===
# Good Code Samples to Remember:
# return files = [file for file in files if not any(substring in file for substring in excluded_suffixes)]

def exclude_files_with_bad_suffixes(path):
    print("\nFiles with bad suffixes:")
    bad_suffixes = {'.m4a'}
    for root, dirs, files in os.walk(path):
        bad_files = [file for file in files if any(file.endswith(suffix) for suffix in bad_suffixes)]
        for file_name in bad_files:
            print(os.path.join(root, file_name))


def exclude_files_with_bad_substrings(path):
    print("\nFiles with bad substrings:")
    bad_substrings = {'ñ'}
    for root, dirs, files in os.walk(path):
        bad_files = [file for file in files if any(substring in file for substring in bad_substrings)]
        for file_name in bad_files:
            print(os.path.join(root, file_name))


def rename_mp3_files_not_conforming_to_standards(path):
    print("\nRenaming non-conforming MP3 files:")
    for root, dirs, files in os.walk(path):
        mp3_files = [file for file in files if any(file.endswith(suffix) for suffix in {'.mp3'})]
        for file_name in mp3_files:
            if "-" in file_name.lower() and " - " not in file_name.lower():
                rename_file("Dash Missing Spaces", root, file_name, "-", " - ")


def include_files_containing_substring(root, files, included_substrings):
    files_included = []
    for file in files:
        if any(substring in file for substring in included_substrings):
            files_included.append(file)
    return files_included


def exclude_files_containing_substring(root, files, excluded_substrings):
    files_not_excluded = []
    for file in files:
        if not any(substring in file for substring in excluded_substrings):
            files_not_excluded.append(file)
        else:
            print("Excluding by substring: " + os.path.join(root, file))
    return files_not_excluded


def include_files_with_suffix(root, files, included_suffixes):
    files_included = []
    for file in files:
        if any(substring in file for substring in included_suffixes):
            files_included.append(file)
    return files_included


def exclude_files_with_suffix(root, files, excluded_suffixes):
    files_not_excluded = []
    for file in files:
        if not any(substring in file for substring in excluded_suffixes):
            files_not_excluded.append(file)
        else:
            print("Excluding for suffix: " + os.path.join(root, file))
    return files_not_excluded


# === MAIN ACTIONS ===


def list_files(path):
    for root, dirs, files in os.walk(path):
        print("\n----- " + root + "-----")
        files = exclude_files_with_suffix(root, files, {'.m4a', '.db', '.ini', '.jpg', '.cbsync'})
        files = exclude_files_containing_substring(root, files, {'ñ', 'é', 'ó', '.cbsync'})
        # for file_name in files:
        #     print(os.path.join(root, file_name))


def delete_crap_files(path):
    print("\n===== Deleting crap files =====")
    for root, dirs, files in os.walk(path):
        files1 = include_files_with_suffix(root, files, {'.jpg'})
        files2 = include_files_containing_substring(root, files, {'.cbsync'})
        files = files1 + files2
        for file_name in files:
            delete_file(os.path.join(root, file_name))


def update_tags_from_file_name(path):
    print("\n===== Updating tags from file name =====")
    for root, dirs, files in os.walk(path):
        files = exclude_files_with_suffix(root, files, {'.m4a', '.db', '.ini', '.jpg', '.cbsync'})
        files = exclude_files_containing_substring(root, files, {'ñ', 'é', 'ó', '.cbsync'})
        for file_name in files:
            data = file_name.split("-")
            try:
                print("Updating Tags: [" + os.path.basename(root + "] " + data[0].strip() + " - " + data[1].strip()))
            except IndexError:
                print("Exception (IndexError): " + root + "\\" + file_name)

            # Set ID3 tags from filename and directory
            audio_file = eyed3.load(root + "\\" + file_name)
            try:
                audio_file.initTag()
                audio_file.tag.artist = data[0].strip()
                audio_file.tag.title = data[1].strip()
                audio_file.tag.genre = os.path.basename(root)
                audio_file.tag.album = u"TQP Album"
                audio_file.tag.comments.set("TQP")
                audio_file.tag.save()
            except AttributeError:
                print("AttributeError: " + root + "\\" + file_name)
            except IndexError:
                print("Exception (IndexError): " + root + "\\" + file_name)


# MAIN PROGRAM
rootDir = "Z:\\MUSIC\\iPod Music"
# rootDir = "C:\\_TQP\Temp"
# rootDir = "Z:\\MUSIC\\Non-Synched Mixes"


def main():
    print("SyncTunes v2")
    # list_files(rootDir)
    delete_crap_files(rootDir)
    update_tags_from_file_name(rootDir)


main()
