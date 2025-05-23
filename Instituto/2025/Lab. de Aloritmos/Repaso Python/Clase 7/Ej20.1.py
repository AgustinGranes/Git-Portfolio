pedidos_sandwiches = ["atún", "pollo", "jamón y queso", "vegetariano"]
sandwiches_terminados = []

for sandwich in pedidos_sandwiches:
    print(f"Preparé tu sándwich de {sandwich}.")
    sandwiches_terminados.append(sandwich)

print("\nTodos los sándwiches están listos. Aquí está la lista:")
for sandwich in sandwiches_terminados:
    print(f"- Sándwich de {sandwich}")
