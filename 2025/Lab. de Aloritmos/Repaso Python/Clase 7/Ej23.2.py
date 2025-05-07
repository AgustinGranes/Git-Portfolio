def hacer_album(artista, titulo, canciones=""):
    if canciones:
        album = f"{artista}, {titulo}, {canciones}."
    else:
        album = f"{artista}, {titulo}."
    return album.title()

print(hacer_album("Patricio Rey", "La mosca"))
print(hacer_album("Patricio Rey", "Oktubre", "17"))