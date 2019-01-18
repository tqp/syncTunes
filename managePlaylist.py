import win32com.client

iTunes = win32com.client.Dispatch("iTunes.Application")

mainLibrary = iTunes.LibraryPlaylist
librarySource = iTunes.LibrarySource

print("Track Count: " + str(iTunes.LibraryPlaylist.Tracks.Count))
print("Playlist Count: " + str(iTunes.LibrarySource.Playlists.Count))

tracks = mainLibrary.Tracks
numTracks = tracks.Count

# iTunes.CreatePlaylist("pig")
# iTunes.LibrarySource.Playlists.ItemByName("Mix - Commercial").Delete()


if iTunes.LibrarySource.Playlists.ItemByName("Audiobooks1"):
    print("Yes")
else:
    print("No")

# print(iTunes.LibrarySource.Playlists.ItemByName("Audiobooks").Name)

# for playlist in iTunes.LibrarySource.Playlists:
#     print(playlist.Name + ", " + iTunes.LibrarySource.Playlists.ItemByName("Audiobooks").Name)
#     # if "Mix" in playlist.Name:
#     #     playlist.Delete()
