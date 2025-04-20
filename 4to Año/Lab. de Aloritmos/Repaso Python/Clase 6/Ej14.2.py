user = ["fabri", "agus", "luca", "admin"]

for usuario in user:
    if usuario == "admin":
        print("bienvenido admin quiere ver un informe de estado")
    elif usuario.lower != "admin":
        print("hola", usuario, "gracias por iniciar sesion")
    else:
        print("¡Necesitamos usuarios!")