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
        
class administrador(usuario):
    def __init__(self, nombre, apellido, genero, pais, intentos_login, *privilegios):
        super().__init__(nombre, apellido, genero, pais, intentos_login)
        lista_privilegios = ("puede agregar publicaciones", "puede eliminar publicaciones", "puede bloquear usuarios")
        self.privilegios = lista_privilegios
        
    def mostrar_privilegios(self):
        contador = 0
        print("Los privilegios que tiene el administrador son: ")
        for privilegio in self.privilegios:
            contador += 1
            print(f"Privilegio {contador}: {privilegio}")

usuario1 = administrador("admin", "1", "Femenino", "Argentina", 0)

usuario1.mostrar_privilegios()