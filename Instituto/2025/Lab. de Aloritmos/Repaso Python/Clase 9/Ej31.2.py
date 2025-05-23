import random

def elegir_numeros():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "A", "B", "C", "D", "E"]
    print("Si tu boleto contiene alguno de los siguientes 4 caracteres, puedes retirar un premio: ")
    num1 = random.choice(lista)
    print(num1)
    lista.remove(num1)
    num2 = random.choice(lista)
    print(num2)
    lista.remove(num2)
    num3 = random.choice(lista)
    print(num3)
    lista.remove(num3)
    num4 = random.choice(lista)
    print(num4)
    lista.remove(num4)

elegir_numeros()