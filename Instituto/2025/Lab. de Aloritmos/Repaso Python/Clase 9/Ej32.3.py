from pathlib import Path

archivo = Path("py_puede.txt")
mensaje = ""

print("Asi funciona si se pega el contenido linea por linea:")   
lineas = archivo.read_text().splitlines()
for linea in lineas:
    mensaje = linea.replace('Python', 'HTML')
    print(mensaje) 