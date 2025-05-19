import json
from pathlib import Path

numero_favorito = input("Ingresá tu número favorito: ")
path = Path("numero_favorito.json")

try:
    contenido = json.dumps(numero_favorito)  # Convertimos el número a formato JSON
    path.write_text(contenido, encoding="utf-8")  # Guardamos el número en un archivo
    print("Tu número favorito ha sido guardado correctamente.")
except Exception as e:
    print(f"Error al escribir el archivo: {e}")
