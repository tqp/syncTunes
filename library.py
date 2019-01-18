import win32com.client
import os

iTunes = win32com.client.Dispatch("iTunes.Application")

mainLibrary = iTunes.LibraryPlaylist
tracks = mainLibrary.Tracks
numTracks = tracks.Count

srcDirectory = "C:\_TQP\Temp"
# srcDirectory = "Z:\MUSIC\iPod Music"
# print("Number of Tracks: " + str(numTracks))

for playlist in iTunes.LibrarySource.Playlists:
    print(playlist.Name)
    if not "Mix - Commercial" == playlist.Name:
        print("NOT")
    else:
        print("YES")


# for dir_path, dirs, files in os.walk(srcDirectory):
#     print("dir_path: " + dir_path)
#     if not "Mix - Commercial" in dir_path:
#         print("NOT")
#     else:
#         print("YES")



# playlist_delete_exceptions_list = {
#     'Library', 'Music', 'Movies', 'TV Shows', 'Podcasts', 'Audiobooks', 'Genius'
# }
# delete_list = list()
# for playlist in itunes.LibrarySource.Playlists:
#     if not any(substring == playlist.Name for substring in playlist_delete_exceptions_list):
#         if not any(playlist.Name in dir_path for dir_path, dirs, files in os.walk(srcDirectory)):
#             playlist_to_delete = playlist.Name
#             print("There is no directory named '" + playlist_to_delete + "'. Deleting playlist...")
#             delete_list.append(playlist_to_delete)
# for item in delete_list:
#     # print(item)
#     itunes.LibrarySource.Playlists.ItemByName(item).Delete()
# print("Done.")