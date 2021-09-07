def make_album (artista, album, tracks =''):
    albumes = {"Artista" : artista, "Album" : album}
    if tracks: 
        albumes ["Tracks"] = tracks
    return albumes


while True:
    artista = input ("Artista:")
    if artista == "q": break
    album = input ("Disco:")
    if album == "q": break
    tracks = input ("Tracks:")
    if tracks == "q": break
    info = make_album (artista, album, tracks)
    print (info)

#print (info)
