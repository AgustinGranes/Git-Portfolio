class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def describir_restaurante(self):
        print(f"Este restaurante se llama '{self.nombre}' y es de tipo {self.tipo}.")
        
    def abrir_restaurante(self):
        print(f"El restaurante '{self.nombre}' se encuentra abierto.")
        
restaurante1 = Restaurante("Lo de Agustín", "Bodegón")
restaurante1.describir_restaurante()