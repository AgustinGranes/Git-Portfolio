mensajes = [
    "Variable: Espacio en memoria que se utiliza para almacenar un valor que puede cambiar durante la ejecución del programa.",
    "Función: Bloque de código reutilizable que realiza una tarea específica y puede ser llamado en cualquier parte del programa.",
    "Bucle: Estructura que permite repetir un bloque de código un número determinado de veces o hasta que se cumpla una condición.",
    "Lista: Estructura de datos que almacena una colección de elementos ordenados, accesibles por índices.",
    "Diccionario: Estructura de datos que almacena pares clave-valor, donde cada clave es única y se usa para acceder a su valor correspondiente.",
    "Clase: Plantilla para crear objetos definidos por el usuario con atributos y métodos.",
    "Módulo: Archivo que contiene definiciones y funciones que pueden ser importadas y reutilizadas en otros programas.",
    "Paquete: Colección de módulos organizados en directorios que facilita la estructura de un proyecto en Python.",
    "Lambda: Expresión que define funciones anónimas en una sola línea.",
    "Decorador: Función que modifica el comportamiento de otra función o método."
]
mensajes_enviados = []

def mostrar_mensaje(mensaje):
    print(mensaje)
        
def enviar_mensajes(mensaje):
    mostrar_mensaje(mensaje)
    mensajes_enviados.append(mensaje)

for mensaje in mensajes:
    enviar_mensajes(mensaje)

print("")
print(*mensajes_enviados)