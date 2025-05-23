edad = 16

if edad < 2:
    print("Es un bebe")
elif edad > 2 and edad > 4:
    print("Es un Nene chiquito")
elif edad > 4 and edad < 13:
    print("Es un Nene")
elif edad > 13 and edad < 20:
    print("Es un adolescente")
elif edad > 20 and edad < 65:
    print("Es un Adulto")
else:
    print("Es un Adulto Mayor")