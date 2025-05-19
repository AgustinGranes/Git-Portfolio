def contar_palabra(nombre_archivo, palabra):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().lower()  # Convertir a minúsculas para un conteo preciso
            conteo_exacto = contenido.count(f"{palabra} ")  # 'the ' con espacio
            conteo_amplio = contenido.count(palabra)  # 'the' sin espacio, incluye 'then', 'there', etc.
            print(f"En {nombre_archivo}:")
            print(f"Conteo amplio ('{palabra}'): {conteo_amplio}")
            print(f"Conteo exacto ('{palabra} ' con espacio): {conteo_exacto}\n")
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no se encuentra.")

# Lista de archivos de texto descargados de Project Gutenberg
archivos = ["texto1.txt", "texto2.txt", "texto3.txt"]  # Modificá con los nombres reales de tus archivos

for archivo in archivos:
    contar_palabra(archivo, "the")