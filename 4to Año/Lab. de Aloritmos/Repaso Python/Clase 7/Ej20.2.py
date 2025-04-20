pedidos_sandwiches = ["atún", "pollo", "pastrón", "jamón y queso", "pastrón", "vegetariano", "pastrón"]

print("Lamentablemente, la sandwichería se quedó sin pastrón.")
print("")

while "pastrón" in pedidos_sandwiches:
    pedidos_sandwiches.remove("pastrón")

sandwiches_terminados = []

for sandwich in pedidos_sandwiches:
    print(f"Preparé tu sándwich de {sandwich}.")
    sandwiches_terminados.append(sandwich)

print("\nTodos los sándwiches están listos. Aquí está la lista:")
for sandwich in sandwiches_terminados:
    print(f"- Sándwich de {sandwich}")
