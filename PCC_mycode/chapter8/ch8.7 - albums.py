def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs']=songs
    return(album)

print(make_album('sting', 'dream of the blue turtles', 12))
print(make_album('eyna', 'orinocco flow'))
print(make_album('rolling stones', 'compilation', 20))