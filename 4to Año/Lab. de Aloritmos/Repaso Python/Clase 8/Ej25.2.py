def sandwich(*ingredientes):
    print("Tu sandwich tendra los siguientes ingredientes: ")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")
    print()

sandwich("Mayonesa", "Lechuga", "Tomate", "Milanesa")
sandwich("Mostaza", "Pepino", "Papas Pay")