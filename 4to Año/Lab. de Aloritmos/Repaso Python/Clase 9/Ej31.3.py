import random

my_ticket = ["A", "B", "C", "1"]
lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E"]
contador = 0

while True:
    simulador = random.sample(lista, 4)
    contador += 1
    
    if simulador == my_ticket:
        break  # Sale del bucle si simulador es igual a my_ticket

print(f"Se tuvo que simular el sorteo {contador} veces hasta que tu boleto logró salir ganador.")
