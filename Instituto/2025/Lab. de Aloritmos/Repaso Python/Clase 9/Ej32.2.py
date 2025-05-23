from pathlib import Path

archivo = Path("py_puede.txt")

print("Asi funciona si se pega el contenido completo:")   
contenido = archivo.read_text()
print(contenido) 

print("Asi funciona si se pega el contenido linea por linea:")   
lineas = archivo.read_text().splitlines()
for linea in lineas:
    print(linea) 