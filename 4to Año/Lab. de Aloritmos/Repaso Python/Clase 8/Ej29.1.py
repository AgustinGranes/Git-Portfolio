class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def describir_restaurante(self):
        print(f"Este restaurante se llama '{self.nombre}' y es de tipo {self.tipo}.")
        
    def abrir_restaurante(self):
        print(f"El restaurante '{self.nombre}' se encuentra abierto.")
        
class Heladeria(Restaurante):
    def __init__(self, nombre, tipo, *gustos):
        super().__init__(nombre, tipo)
        self.gustos = gustos
        
    def describir_heladeria(self):
        contador = 0
        if self.gustos:
            heladeria = f"La heladeria {self.nombre} es {self.tipo} y sus gustos son:"
            print(heladeria)
            for gusto in self.gustos:
                contador += 1
                print(f"El gusto {contador} es: {gusto}")
        else:
            heladeria = f"La heladeria {self.nombre} es {self.tipo} y no tiene gustos aun."
            print(heladeria)

heladeria1 = Heladeria("Lo de Agustín", "Artesanal", "Sambayon", "Frutilla", "Dulce de leche")
heladeria1.describir_heladeria()

heladeria2 = Heladeria("Valence", "Artesanal")
heladeria2.describir_heladeria()