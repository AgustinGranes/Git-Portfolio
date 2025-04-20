mascota1 = {"tipo": "Perro", "nombre_dueño": "Sofía"}
mascota2 = {"tipo": "Gato", "nombre_dueño": "Juan"}
mascota3 = {"tipo": "Pez", "nombre_dueño": "Carla"}
mascota4 = {"tipo": "Loro", "nombre_dueño": "Luis"}

mascotas = [mascota1, mascota2, mascota3, mascota4]

for mascota in mascotas:
    print("Tipo de animal: ", mascota["tipo"])
    print("Nombre del dueño: ", mascota["nombre_dueño"])
    print("-" * 20)
