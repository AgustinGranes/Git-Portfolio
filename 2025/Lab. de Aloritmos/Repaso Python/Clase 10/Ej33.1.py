from pathlib import Path
path = Path('programming.txt')

input_nombre = input("Escribe tu nombre: ")
path.write_text(f"Hola {input_nombre}") 