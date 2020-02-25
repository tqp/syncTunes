import os

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3


# MUTAGEN GETTERS

def print_all(mp3_file):
    print(mp3_file)


def get_title(path):
    return MP3(path)['TIT2'].text[0]


def get_artist(path):
    return MP3(path)['TPE1'].text[0]


def get_genre(path):
    return MP3(path)['TCON'].text[0]


def get_album(path):
    return MP3(path)['TALB'].text[0]


# MUTAGEN SETTERS

def set_title(path, title):
    mp3_write = EasyID3(path)
    mp3_write['title'] = title
    try:
        mp3_write.save()
    except:
        print('TQP UnicodeEncodeError: ' + path)


def set_artist(path, artist):
    mp3_write = EasyID3(path)
    mp3_write['artist'] = artist
    mp3_write.save()


def set_genre(path, genre):
    mp3_write = EasyID3(path)
    mp3_write['genre'] = genre
    mp3_write.save()


def set_album(path, album):
    mp3_write = EasyID3(path)
    mp3_write['album'] = album
    mp3_write.save()


# OS GETTERS


def get_artist_from_filename(file_name):
    data = file_name.split(" - ")
    return data[0].strip()


def get_title_from_filename(file_name):
    data = file_name.split(" - ")
    return data[1].strip().replace('.mp3', '')


def get_genre_from_path(root):
    return os.path.basename(root)


# ACTIONS

def list_files(path):
    for root, dirs, files in os.walk(path):
        print("----- " + root + " -----")
        for file_name in files:
            get_genre_from_path(root)
            # get_artist_from_filename(file_name)
            # get_title_from_filename(file_name)


def update_tags_from_path(path):
    for root, dirs, files in os.walk(path):
        print("----- " + root + " -----")
        mp3_files = [file for file in files if any(file.endswith(suffix) for suffix in {'.mp3'})]
        for file_name in mp3_files:
            path = root + "\\" + file_name
            # print(path)
            set_title(path, get_title_from_filename(file_name))
            set_artist(path, get_artist_from_filename(file_name))
            set_album(path, get_genre_from_path(root))
            set_genre(path, get_genre_from_path(root))


def main():
    # path = "M:\\Test Folder\\Beach\\Dobie Gray - Drift Away.mp3"
    # path = "M:\\Test Folder\\Beach"
    # path = 'M:\\Tim\'s Playlists'
    # path = 'M:\\Tim\'s Playlists\\Relax Folder\\Relax - Feel Good'
    path = 'M:\\Test Folder'

    update_tags_from_path(path)


main()
