class Usuario:
    def __init__(self, nombre, apellido, genero, pais, intentos_login):
        self.nombre = nombre
        self.apellido = apellido 
        self.genero = genero
        self.pais = pais
        self.intentos_login = intentos_login

    def describir_usuario(self):
        print(f"El nombre del usuario es {self.nombre}, su apellido es {self.apellido}, es de género {self.genero} y nació en {self.pais}.")
        
    def incrementar_intentos_login(self):
        self.intentos_login += 1
        print(f"El usuario {self.nombre} ha intentado ingresar {self.intentos_login} veces.")
        
    def reiniciar_intentos_login(self):
        self.intentos_login = 0
        print(f"El usuario {self.nombre} ha logrado iniciar sesión, sus intentos de inicio vuelven a ser 0.")

class Privilegios:
    def __init__(self, privilegios=None):
        if privilegios is None:
            self.privilegios = ["puede agregar publicaciones", "puede eliminar publicaciones", "puede bloquear usuarios"]
        else:
            self.privilegios = privilegios

    def mostrar_privilegios(self):
        print("Los privilegios que tiene el administrador son:")
        for i, privilegio in enumerate(self.privilegios, 1):
            print(f"Privilegio {i}: {privilegio}")

class Administrador(Usuario):
    def __init__(self, nombre, apellido, genero, pais, intentos_login):
        super().__init__(nombre, apellido, genero, pais, intentos_login)
        self.privilegios = Privilegios()

admin = Administrador("Admin", "1", "Femenino", "Argentina", 0)
admin.privilegios.mostrar_privilegios()