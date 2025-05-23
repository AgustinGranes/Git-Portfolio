nombres = ['Fabrizio', 'Luca', 'Luchi']

print("Invitacion 1:")
mensaje = f"Hola {nombres[0]}, quiero que vengas a casa a comer."
print(mensaje)
print()

print("Invitacion 2:")
mensaje = f"Hola {nombres[1]}, quiero que vengas a casa a comer."
print(mensaje)
print()

print("Invitacion 3:")
mensaje = f"Hola {nombres[2]}, quiero que vengas a casa a comer."
print(mensaje)
print()

print("---")
print()
inasistencia = f"El invitado {nombres[0]}, no puede asistir."
print(inasistencia)

nombres[0] = "Barba"

print()
print("Invitacion 1:")
mensaje = f"Hola {nombres[0]}, quiero que vengas a casa a comer."
print(mensaje)
print()

print()
print("Invitacion 2:")
mensaje = f"Hola {nombres[1]}, quiero que vengas a casa a comer."
print(mensaje)
print()

print("---")
print()
print("Consegui una mesa mas grande, con lo cual pueden venir 2 personas mas!")
print()

nombres.insert(2, "Quintela")
nombres.append("Mate")

print("Invitacion 1:")
mensaje = f"Hola {nombres[0]}, quiero que vengas a casa a comer."
print(mensaje)
print()

print("Invitacion 2:")
mensaje = f"Hola {nombres[1]}, quiero que vengas a casa a comer."
print(mensaje)
print()

print("Invitacion 3:")
mensaje = f"Hola {nombres[2]}, quiero que vengas a casa a comer."
print(mensaje)
print()

print("Invitacion 4:")
mensaje = f"Hola {nombres[3]}, quiero que vengas a casa a comer."
print(mensaje)
print()

print("Invitacion 5:")
mensaje = f"Hola {nombres[4]}, quiero que vengas a casa a comer."
print(mensaje)
print()

print("---")
print()
print("La mesa no llega, el flete es un fracaso.")
print()

nombres.pop(4)
nombres.pop(3)
nombres.pop(2)

print("Invitacion 1:")
mensaje = f"Hola {nombres[0]}, quiero que vengas a casa a comer."
print(mensaje)
print()

print("Invitacion 2:")
mensaje = f"Hola {nombres[1]}, quiero que vengas a casa a comer."
print(mensaje)
print()