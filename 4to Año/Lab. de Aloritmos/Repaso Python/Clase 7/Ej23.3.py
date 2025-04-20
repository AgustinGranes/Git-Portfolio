def hacer_album(artista, titulo):
    return {"artista": artista, "titulo": titulo}

while True:
    print("\nIngresá 'salir' en cualquier momento para terminar.")
    
    artista = input("Ingresá el nombre del artista: ")
    if artista.lower() == "salir":
        break
    
    titulo = input("Ingresá el título del álbum: ")
    if titulo.lower() == "salir":
        break
    
    album = hacer_album(artista, titulo)
    print(f"\nÁlbum creado: {album}")