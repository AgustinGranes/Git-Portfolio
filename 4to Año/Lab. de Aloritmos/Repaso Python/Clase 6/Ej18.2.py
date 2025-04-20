def es_multiplo_de_10():
    try:
        numero = int(input("Por favor, ingrese un número: "))
        if numero % 10 == 0:
            print(f"El número {numero} es múltiplo de 10.")
        else:
            print(f"El número {numero} no es múltiplo de 10.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
        
es_multiplo_de_10()
