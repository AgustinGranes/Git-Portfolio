class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def obtener_nombre_descriptivo(self):
        return f"{self.marca} {self.modelo} {self.año}"

class Bateria:
    def __init__(self, capacidad_bateria=40):
        self.capacidad_bateria = capacidad_bateria

    def describir_bateria(self):
        print(f"Este auto tiene una batería de {self.capacidad_bateria} kWh.")

    def obtener_autonomia(self):
        if self.capacidad_bateria == 40:
            rango = 150
        elif self.capacidad_bateria == 65:
            rango = 225
        else:
            rango = 100  # Valor por defecto si la capacidad es diferente
        print(f"Este auto tiene una autonomía de {rango} kilómetros.")

    def actualziar_bateria(self):
        pass

class AutoElectrico(Auto):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
        self.bateria = Bateria()

    def llenar_tanque(self):
        print("¡Este auto no tiene un tanque de nafta!")

mi_leaf = AutoElectrico('nissan', 'leaf', 2024)
print(mi_leaf.obtener_nombre_descriptivo())

mi_leaf.bateria.describir_bateria()
mi_leaf.bateria.obtener_autonomia()