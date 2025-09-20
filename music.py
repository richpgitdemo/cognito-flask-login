"""
Create a group of classes that represents information about music artists, 
their albums, and the tracks on those albums.  Each class should contain the following information:
Artist:  name, released albums
Album: name, artist, tracks
Track: number, name, length (seconds), artists

Write a program to demonstrate cataloging artists, their albums, and the tracks on those albums.
Demonstrate ways to navigate the relationships between the classes.
List every track from every album published for an artist.
List the album, number of tracks, and the total run time of the album for each artist.


"""

class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []


class Album:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.tracks = []

class Track:
    def __init__(self, number, name, length):
        self.number = number
        self.name = name
        self.length = length
        self.artists = []



artist_one = Artist("Artist One")
artist_two = Artist("Artist Two")

album_one = Album("First Opus", artist_one)

artist_one.albums.append(album_one)

album_one.tracks.append(
    Track(1, "Cool Birds", 245)
    )

album_one.tracks.append(
    Track(2, "Warm Giraffes", 270)
    )





album_two = Album("Second Concerto", artist_two)

artist_two.albums.append(album_two)

album_two.tracks.append(
    Track(1, "Flying Flute", 180)
    )



album_three = Album("Second Opus", artist_one)

artist_one.albums.append(album_three)

album_three.tracks.append(
    Track(1, "Towering Oaks", 150)
    )

album_three.tracks.append(
    Track(2, "Lofty Cedars", 138)
    )


# List every track from every album published for an artist.
print("Track List")
for artist in [artist_one, artist_two]:
    print(f"{artist.name}")
    for album in artist.albums:
        for track in album.tracks:
            print(f"\t{track.name}")


print("\n\n")    

# List the album, number of tracks, and the total run time of the album for each artist
print("Album Details")
album_list = []
for artist in [artist_one, artist_two]:
    print(f"{artist.name}")
    for album in artist.albums:
        print(f"\tAlbum: {album.name} Tracks: {len(album.tracks)} Total Run Time: {sum([x.length for x in album.tracks])}")