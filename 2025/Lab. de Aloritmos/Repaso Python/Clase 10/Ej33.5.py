# Creación de archivos con nombres de gatos y perros
with open("gatos.txt", "w") as archivo_gatos:
    archivo_gatos.write("Michi\nPelusa\nBigotes\n")

with open("perros.txt", "w") as archivo_perros:
    archivo_perros.write("Firulais\nBobby\nLuna\n")

# Función para leer los archivos y manejar errores
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(f"Contenido de {nombre_archivo}:\n{contenido}")
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no se encuentra en la ubicación esperada.\n")

# Intentamos leer ambos archivos
leer_archivo("gatos.txt")
leer_archivo("perros.txt")
