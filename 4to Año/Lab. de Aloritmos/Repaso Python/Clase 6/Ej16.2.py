rios_paises = {
    'Nilo': 'Egipto',
    'Amazonas': 'Brasil',
    'Misisipi': 'Estados Unidos'
}

for key, value in rios_paises.items():
    print(f"El {key} pasa por {value}.")

print("\nNombres de los ríos:")
for key in rios_paises.keys():
    print(key)

print("\nNombres de los países:")
for value in rios_paises.values():
    print(value)
