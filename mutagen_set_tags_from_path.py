import os
import time

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3


# MUTAGEN GETTERS

def print_all(mp3_file):
    print(mp3_file)


def get_title_from_tag(path):
    try:
        return MP3(path)['TIT2'].text[0]
    except Exception as e:
        print('Exception: ' + path + ': ' + str(e))


def get_artist_from_tag(path):
    return MP3(path)['TPE1'].text[0]


def get_genre_from_tag(path):
    return MP3(path)['TCON'].text[0]


def get_album_from_tag(path):
    return MP3(path)['TALB'].text[0]


# MUTAGEN DOES TAG EXIST

def does_title_tag_exist(path):
    try:
        title = MP3(path)['TIT2'].text[0]
        return True
    except Exception as e:
        print('Warning: Title tag does not exist for \'' + path + '\': ' + str(e))
        return False


def does_artist_tag_exist(path):
    try:
        title = MP3(path)['TPE1'].text[0]
        return True
    except Exception as e:
        print('Warning: Artist tag does not exist for \'' + path + '\': ' + str(e))
        return False


def does_genre_tag_exist(path):
    try:
        title = MP3(path)['TCON'].text[0]
        return True
    except Exception as e:
        print('Warning: Genre tag does not exist for \'' + path + '\': ' + str(e))
        return False


def does_album_tag_exist(path):
    try:
        title = MP3(path)['TALB'].text[0]
        return True
    except Exception as e:
        print('Exception in \'does_album_tag_exist\': Album tag does not exist for \'' + path + '\': ' + str(e))
        return False


# MUTAGEN SETTERS

def set_title(path, title):
    try:
        mp3_write = EasyID3(path)
        mp3_write['title'] = title
        mp3_write.save()
    except UnboundLocalError as e:
        print('UnboundLocalError: ' + path + ': ' + str(e))
    except Exception as e:
        print('Exception: ' + path + ': ' + str(e))


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
    data = file_name.split(' - ')
    try:
        title = data[1].strip().replace('.mp3', '')
        return title
    except Exception as e:
        print('Exception getting artist from filename: ' + file_name + ': ' + str(e))


def get_title_from_filename(file_name):
    data = file_name.split(' - ')
    try:
        artist = data[0].strip()
        return artist
    except Exception as e:
        print('Exception getting title from filename: ' + file_name + ': ' + str(e))


def get_genre_from_path(root):
    return os.path.basename(root)


# FUNCTIONS AND METHODS

def are_tags_missing(root, file_name):
    missing = False
    path = root + '/' + file_name

    if not does_title_tag_exist(path):
        # print('Title tag is missing for \'' + path + '\'')
        missing = True
    if not does_artist_tag_exist(path):
        # print('Artist tag is missing for \'' + path + '\'')
        missing = True
    if not does_genre_tag_exist(path):
        # print('Genre tag is missing for \'' + path + '\'')
        missing = True
    if not does_album_tag_exist(path):
        # print('Album tag is missing for \'' + path + '\'')
        missing = True

    return missing


def have_tags_changed(root, file_name):
    changed = False
    path = root + '/' + file_name

    # print('title : filename: ' + get_title_from_filename(file_name))
    # print('title : tag     : ' + get_title_from_tag(path))
    # print('artist: filename: ' + get_artist_from_filename(file_name))
    # print('artist: tag     : ' + get_artist_from_tag(path))
    # print('album : path    : ' + get_genre_from_path(root))
    # print('album : tag     : ' + get_genre_from_tag(path))
    # print('genre : path    : ' + get_genre_from_path(root))
    # print('genre : tag     : ' + get_genre_from_tag(path))

    if get_title_from_filename(file_name) != get_title_from_tag(path):
        changed = True
    if get_artist_from_filename(file_name) != get_artist_from_tag(path):
        changed = True
    if get_genre_from_path(root) != get_album_from_tag(path):
        changed = True
    if get_genre_from_path(root) != get_genre_from_tag(path):
        changed = True

    return changed


# ACTIONS

def list_files(path):
    for root, dirs, files in os.walk(path):
        print('----- ' + root + ' ----- (-)')
        for file_name in files:
            get_genre_from_path(root)
            # get_artist_from_filename(file_name)
            # get_title_from_filename(file_name)


def update_tags_from_path(path):
    for root, dirs, files in os.walk(path):
        print('----- ' + root + ' ----- (=)')
        mp3_files = [file for file in files if any(file.endswith(suffix) for suffix in {'.mp3'})]
        for file_name in mp3_files:
            # print('Checking: ' + file_name)
            path = root + '/' + file_name

            missing = are_tags_missing(root, file_name)
            changed = False
            if not missing:
                changed = have_tags_changed(root, file_name)

            if changed or missing:
                # print('Updating tags for: ' + path)
                try:
                    set_title(path, get_title_from_filename(file_name))
                    set_artist(path, get_artist_from_filename(file_name))
                    set_album(path, get_genre_from_path(root))
                    set_genre(path, get_genre_from_path(root))
                except Exception as e:
                    print('################')
                    print('YOU NEED TO FIX: ' + path)
                    print(e)
                    print('################')
                    pass


def main():
    print('Starting \'Set Playlist Tags\' Job at ' + time.ctime())
    # path = 'M:\\Temp'
    # path = 'M:\\Tim\'s Playlists'
    # path = 'M:\\Tim\'s Playlists\\Beach\\Beach - Cheesy'
    # path = '/volume1/music//Tim\'s Playlists/The 1980\'s Folder/The 1980\'s - Legwarmers'
    # path = '/volume1/music//Tim\'s Playlists/Beach/Beach - Cheesy'

    path = '/volume1/music/Tim\'s Playlists'

    update_tags_from_path(path)
    print('Finished.')


main()

# REF: online-audio-converter.com
