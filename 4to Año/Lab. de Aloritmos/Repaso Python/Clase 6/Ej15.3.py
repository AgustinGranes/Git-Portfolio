glosario = {
    "Variable": "Espacio en memoria que se utiliza para almacenar un valor que puede cambiar durante la ejecución del programa.",
    "Función": "Bloque de código reutilizable que realiza una tarea específica y puede ser llamado en cualquier parte del programa.",
    "Bucle": "Estructura que permite repetir un bloque de código un número determinado de veces o hasta que se cumpla una condición.",
    "Lista": "Estructura de datos que almacena una colección de elementos ordenados, accesibles por índices.",
    "Diccionario": "Estructura de datos que almacena pares clave-valor, donde cada clave es única y se usa para acceder a su valor correspondiente."
}

for palabra, definicion in glosario.items():
    print(f"{palabra}:\n\t{definicion}\n")
