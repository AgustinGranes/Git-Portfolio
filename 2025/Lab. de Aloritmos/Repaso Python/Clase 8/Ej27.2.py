class restaurante:
    def __init__(self, nombre, describir_restaurante, abrir_restaurante):
        self.nombre = nombre
        self.describir_restaurante = describir_restaurante
        self.abrir_restaurante = abrir_restaurante

    def describir_restaurante(self):
        print(f"El Restaurante {self.nombre} es {self.describir_restaurante}")

restaurante1 = restaurante("La Parrilla", "Lindo")
restaurante2 = restaurante("Sushi Express", "Feo")
restaurante3 = restaurante("Pasta Bella", "Limpio")

restaurante1.describir_restaurante()
restaurante2.describir_restaurante()
restaurante3.describir_restaurante()