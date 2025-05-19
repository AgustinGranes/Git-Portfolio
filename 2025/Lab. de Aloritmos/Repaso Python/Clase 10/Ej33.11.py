import json
from pathlib import Path

path = Path("usuario.json")

def obtener_nuevo_usuario():
    """Solicita un nuevo nombre y lo guarda en el archivo JSON."""
    nombre = input("Ingresá tu nombre: ")
    with path.open("w", encoding="utf-8") as archivo:
        json.dump({"nombre": nombre}, archivo)
    return nombre

def saludar_usuario():
    """Verifica si ya hay un nombre guardado y pregunta si es correcto."""
    if path.exists():
        try:
            with path.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                nombre_guardado = datos.get("nombre", "")
            
            confirmar = input(f"¿Sos {nombre_guardado}? (sí/no): ").strip().lower()
            if confirmar == "sí":
                print(f"¡Bienvenido de nuevo, {nombre_guardado}!")
            else:
                nombre = obtener_nuevo_usuario()
                print(f"Guardamos tu nuevo nombre, {nombre}. ¡Bienvenido!")
        except json.JSONDecodeError:
            print("Hubo un problema al leer el archivo, se ingresará un nuevo nombre.")
            nombre = obtener_nuevo_usuario()
            print(f"Guardamos tu nuevo nombre, {nombre}. ¡Bienvenido!")
    else:
        nombre = obtener_nuevo_usuario()
        print(f"Guardamos tu nombre, {nombre}. ¡Bienvenido!")

saludar_usuario()