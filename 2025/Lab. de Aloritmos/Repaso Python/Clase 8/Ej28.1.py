class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.clientes_atendidos = 0

    def describir_restaurante(self):
        print(f"Este restaurante se llama '{self.nombre}' y es de tipo {self.tipo}.")
        
    def abrir_restaurante(self):
        print(f"El restaurante '{self.nombre}' se encuentra abierto.")
    
    def establecer_clientes_atendidos(self, cantidad):
        self.clientes_atendidos = cantidad
        
    def sumar_clientes_atendidos(self, cantidad):
        self.clientes_atendidos += cantidad
        
restaurante1 = Restaurante("Lo de Agustín", "Bodegón")
restaurante1.establecer_clientes_atendidos(4)
print(restaurante1.clientes_atendidos)
restaurante1.sumar_clientes_atendidos(1)
print(restaurante1.clientes_atendidos)