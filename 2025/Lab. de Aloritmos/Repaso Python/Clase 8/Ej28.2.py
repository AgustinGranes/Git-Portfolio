class usuario:
    def __init__(self, nombre, apellido, genero, pais, intentos_login):
        self.nombre = nombre
        self.apellido = apellido 
        self.genero = genero
        self.pais = pais
        self.intentos_login = intentos_login

    def describir_usuario(self):
        print(f"El nombre del usuario es {self.nombre}, su apellido es {self.apellido}, es de genero {self.genero} y nacio en {self.pais}")
        
    def incrementar_intentos_login(self):
        self.intentos_login += 1
        print(f"El usuario {self.nombre} a intentado ingresar {self.intentos_login} veces.")
        
    def reiniciar_intentos_login(self):
        self.intentos_login = 0
        print(f"El usuario {self.nombre} a logrado iniciar sesion, sus intentos de inicio vuelven a ser 0.")

usuario2 = usuario("Lorena", "Casas", "Femenino", "Argentina", 0)

usuario2.describir_usuario()
usuario2.incrementar_intentos_login()
usuario2.incrementar_intentos_login()
usuario2.incrementar_intentos_login()
usuario2.reiniciar_intentos_login()