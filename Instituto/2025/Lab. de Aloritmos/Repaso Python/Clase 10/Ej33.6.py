# Función para leer los archivos sin mostrar errores si faltan
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(f"Contenido de {nombre_archivo}:\n{contenido}")
    except FileNotFoundError:
        pass  # No hacemos nada si el archivo no existe

# Intentamos leer ambos archivos
leer_archivo("gatos.txt")
leer_archivo("perros.txt")