from pathlib import Path
stop = 0
nombres = []

while stop == 0:
    input_nombre = input("Escribe tu nombre (stop para terminar): ")
    nombres.append(input_nombre)
    if input_nombre == "stop":
        stop = 1
path = Path('Nombres.txt')

input_nombre = input("Escribe tu nombre: ")
path.write_text(f"Hola {input_nombre}")