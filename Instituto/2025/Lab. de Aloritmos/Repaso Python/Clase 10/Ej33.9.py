import json
from pathlib import Path

path = Path("numero_favorito.json")

# Intentamos leer el número favorito si ya está guardado
if path.exists():
    try:
        contenido = path.read_text(encoding="utf-8")
        numero_favorito = json.loads(contenido)
        print(f"¡Sé cuál es tu número favorito! Es {numero_favorito}.")
    except json.JSONDecodeError:
        print("Hubo un problema al leer el número guardado.")
else:
    # Si el archivo no existe, pedimos el número favorito y lo guardamos
    numero_favorito = input("Ingresá tu número favorito: ")
    try:
        contenido = json.dumps(numero_favorito)
        path.write_text(contenido, encoding="utf-8")
        print("Tu número favorito ha sido guardado correctamente.")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")
