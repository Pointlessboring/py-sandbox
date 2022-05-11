def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs']=songs
    return(album)

albums = []
while True:

    artist = input ("\nWhat is the artist's name ('q' to quit): ")
    if artist == 'q':
        break

    title  = input ("\nWhat is the albums's name ('q' to quit): ")
    if title == 'q':
        break
    
    album = make_album(artist, title)
    print(album)
    albums.append(album)

print(albums)

