usuarios_actuales = ["Juan", "Maria", "Pedro", "Ana", "Luis"]
usuarios_nuevos = ["JUAN", "Carlos", "Ana", "Roberto", "Elena"]

usuarios_actuales_lower = [i.lower() for i in usuarios_actuales]

for i in usuarios_nuevos:
    if i.lower() in usuarios_actuales_lower:
        print(f"El nombre de usuario '{i}' ya está en uso. Por favor, elige otro nombre.")
    else:
        print(f"El nombre de usuario '{i}' está disponible.")