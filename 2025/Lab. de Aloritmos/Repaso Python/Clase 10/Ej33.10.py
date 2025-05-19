import json
from pathlib import Path

path = Path("usuario.json")

# Si el archivo existe, leer los datos almacenados
if path.exists():
    try:
        contenido = path.read_text(encoding="utf-8")
        usuario = json.loads(contenido)
        print(f"¡Sé quién sos! Te llamás {usuario['nombre']}, tenés {usuario['edad']} años y vivís en {usuario['ciudad']}.")
    except json.JSONDecodeError:
        print("Hubo un problema al leer los datos almacenados.")
else:
    # Si el archivo no existe, pedir los datos y guardarlos
    nombre = input("Ingresá tu nombre: ")
    edad = input("Ingresá tu edad: ")
    ciudad = input("Ingresá tu ciudad: ")

    usuario = {"nombre": nombre, "edad": edad, "ciudad": ciudad}

    try:
        contenido = json.dumps(usuario)
        path.write_text(contenido, encoding="utf-8")
        print("Tu información ha sido guardada correctamente. ¡Nos vemos la próxima!")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")
