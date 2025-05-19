def suma_numeros():
    try:
        num1 = int(input("Ingresá el primer número: "))
        num2 = int(input("Ingresá el segundo número: "))
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es {resultado}.")
    except ValueError:
        print("Error: Por favor, ingresá solo números.")

suma_numeros()