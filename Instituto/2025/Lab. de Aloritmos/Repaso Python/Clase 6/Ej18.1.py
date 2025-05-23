def verificar_disponibilidad():
    try:
        personas = int(input("¿Cuántas personas hay en su grupo para cenar? "))
        if personas > 0:
            if personas > 8:
                print("Van a tener que esperar por una mesa.")
            else:
                print("Su mesa está lista.")
        else:
            print("Por favor, ingrese un número válido de personas.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
        
verificar_disponibilidad()
