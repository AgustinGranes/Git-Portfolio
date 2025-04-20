from pathlib import Path

archivo_pi = Path("pi_millon.txt")

if archivo_pi.exists():
    contenido = archivo_pi.read_text().strip() 

    fecha_nacimiento = input("Ingresa tu cumpleaños, en la forma ddmmaa: ")

    if fecha_nacimiento in contenido:
        print("¡Tu cumpleaños aparece en los primeros un millón de dígitos de pi!")
    else:
        print("Tu cumpleaños no aparece en los primeros un millón de dígitos de pi.")
else:
    print("El archivo pi_millon.txt no se encuentra.")
