while True:
    try:
        edad = int(input("Por favor, ingresa tu edad (o escribe -1 para salir): "))
        if edad == -1:  # Condición para salir del bucle
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        elif edad < 0:  # Validación de edad negativa
            print("La edad no puede ser negativa. Intenta nuevamente.")
        elif edad < 3:
            print("La entrada es gratis.")
        elif edad <= 12:
            print("La entrada cuesta $10.")
        else:
            print("La entrada cuesta $15.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
