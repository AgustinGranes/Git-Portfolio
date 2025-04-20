nombres = ['Fabrizio', 'Luca', 'Luchi']

print("Invitacion 1:")
mensaje1 = f"Hola {nombres[0]}, quiero que vengas a casa a comer."
print(mensaje1)
print()

print("Invitacion 2:")
mensaje2 = f"Hola {nombres[1]}, quiero que vengas a casa a comer."
print(mensaje2)
print()

print("Invitacion 3:")
mensaje3 = f"Hola {nombres[2]}, quiero que vengas a casa a comer."
print(mensaje3)
print()

print("---")
print()
inasistencia = f"El invitado {nombres[0]}, no puede asistir."
print(inasistencia)

nombres[0] = "Barba"

print()
print("Invitacion 4:")
mensaje4 = f"Hola {nombres[0]}, quiero que vengas a casa a comer."
print(mensaje4)
print()

print("---")
print()
print("Consegui una mesa mas grande, con lo cual pueden venir 2 personas mas!")

nombres.insert(2, "Quintela")
nombres.append("Mate")

print("Invitacion 1:")
mensaje1 = f"Hola {nombres[0]}, quiero que vengas a casa a comer."
print(mensaje1)
print()

print("Invitacion 2:")
mensaje2 = f"Hola {nombres[1]}, quiero que vengas a casa a comer."
print(mensaje2)
print()

print("Invitacion 3:")
mensaje3 = f"Hola {nombres[2]}, quiero que vengas a casa a comer."
print(mensaje3)
print()

print("Invitacion 4:")
mensaje4 = f"Hola {nombres[3]}, quiero que vengas a casa a comer."
print(mensaje4)
print()

print("Invitacion 5:")
mensaje5 = f"Hola {nombres[4]}, quiero que vengas a casa a comer."
print(mensaje5)
print()