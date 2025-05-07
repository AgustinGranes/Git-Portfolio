class usuario:
    def __init__(self, nombre, apellido, genero, pais):
        self.nombre = nombre
        self.apellido = apellido 
        self.genero = genero
        self.pais = pais

    def describir_usuario(self):
        print(f"El nombre del usuario es {self.nombre}, su apellido es {self.apellido}, es de genero {self.genero} y nacio en {self.pais}")

usuario1 = usuario("Agustin", "Granes", "Maculino", "Argentina")
usuario2 = usuario("Lorena", "Casas", "Femenino", "Argentina")

usuario1.describir_usuario()
usuario2.describir_usuario()