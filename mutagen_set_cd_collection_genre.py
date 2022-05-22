import os
import time

import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3


# MUTAGEN SETTERS

def set_genre_mp3(path, genre):
    try:
        audio = MP3(path)
        if 'TCON' in audio:
            mp3_write = EasyID3(path)
            mp3_write['genre'] = genre
            mp3_write.save()
        else:
            mp3_write = mutagen.File(path, easy=True)
            mp3_write.add_tags()
            mp3_write['genre'] = genre
            mp3_write.save(path, v1=2)
    except Exception as e:
        print('Exception: ' + path + ': ' + str(e))

# ACTIONS

def update_genre_to_cd_collection(path):
    for root, dirs, files in os.walk(path):
        print("----- " + root + " -----")
        mp3_files = [file for file in files if any(file.endswith(suffix) for suffix in {'.mp3'})]
        for file_name in mp3_files:
            path = root + "\\" + file_name
            set_genre_mp3(path, 'CD Collection')


def main():
    print('Starting \'CD Collection Genre\' Job at ' + time.ctime())
    path = 'M:\\CD Collection\\_Chill Out Compilations\\Samsung - ChillOut Sessions 3 - Disc 1'
    path = 'M:\\CD Collection\\Unknown Album'
    path = 'M:\\CD Collection'

    update_genre_to_cd_collection(path)


main()
