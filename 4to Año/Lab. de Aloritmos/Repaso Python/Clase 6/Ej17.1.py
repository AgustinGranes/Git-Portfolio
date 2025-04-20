persona1 = {"nombre": "María", "apellido": "Gómez", "edad": 28, "ciudad": "Buenos Aires"}
persona2 = {"nombre": "Carlos", "apellido": "Pérez", "edad": 35, "ciudad": "Rosario"}
persona3 = {"nombre": "Lucía", "apellido": "Martínez", "edad": 22, "ciudad": "Córdoba"}

gente = [persona1, persona2, persona3]

for persona in gente:
    print("Nombre: ", persona["nombre"])
    print("Apellido: ", persona["apellido"])
    print("Edad: ", persona["edad"])
    print("Ciudad: ", persona["ciudad"])
    print("-" * 20)
