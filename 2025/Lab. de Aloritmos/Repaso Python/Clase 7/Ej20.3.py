print("Bienvenido a la encuesta de destinos de vacaciones soñados!")
print("Si pudieras visitar un lugar en el mundo, ¿a dónde irías?\n")

resultados = {}

while True:
    nombre = input("Por favor, ingresa tu nombre (o escribe 'salir' para finalizar): ")
    if nombre.lower() == 'salir':
        break
    destino = input(f"Hola, {nombre}, ¿a dónde te gustaría ir?: ")
    
    resultados[nombre] = destino

    print("¡Gracias por participar!\n")

print("\nResultados de la encuesta:")
for nombre, destino in resultados.items():
    print(f"{nombre} sueña con visitar {destino}.")
