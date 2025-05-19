import json
from pathlib import Path

path = Path("numero_favorito.json")

try:
    contenido = path.read_text(encoding="utf-8")  # Leemos el contenido del archivo
    numero_favorito = json.loads(contenido)  # Convertimos el JSON de nuevo a un valor
    print(f"¡Sé cuál es tu número favorito! Es {numero_favorito}.")
except FileNotFoundError:
    print("Aún no se ha guardado ningún número favorito.")
except json.JSONDecodeError:
    print("Hubo un problema al leer el número guardado.")
