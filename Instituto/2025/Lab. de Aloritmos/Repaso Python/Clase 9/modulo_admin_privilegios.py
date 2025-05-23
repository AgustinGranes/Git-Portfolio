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