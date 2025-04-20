print("¡Vamos a hacer una pizza! Escribe 'salir' cuando hayas terminado de añadir ingredientes.")

while True:
    ingrediente = input("Ingresa un ingrediente para tu pizza: ")
    if ingrediente.lower() == 'salir':
        print("¡Gracias! Ahora prepararé tu pizza.")
        break
    else:
        print(f"¡Perfecto! Agregaré {ingrediente} a tu pizza.")
