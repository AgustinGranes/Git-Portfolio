control = True 

while control:
    entrada = input("Por favor, ingresa tu edad (o escribe 'salir' para terminar): ")
    if entrada.lower() == 'salir':  
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break
    try:
        edad = int(entrada)
        if edad < 0: 
            print("La edad no puede ser negativa. Intenta nuevamente.")
        elif edad < 3:
            print("La entrada es gratis.")
        elif edad <= 12:
            print("La entrada cuesta $10.")
        else:
            print("La entrada cuesta $15.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
