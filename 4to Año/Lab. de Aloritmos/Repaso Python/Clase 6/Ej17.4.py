ciudades = {
    "Buenos Aires": {
        "país": "Argentina",
        "población": "15 millones",
        "dato": "Es conocida como la 'París de Sudamérica' por su arquitectura y cultura."
    },
    "Tokio": {
        "país": "Japón",
        "población": "37 millones",
        "dato": "Es la ciudad más poblada del mundo y un centro de innovación tecnológica."
    },
    "París": {
        "país": "Francia",
        "población": "11 millones",
        "dato": "La Torre Eiffel, su icono, fue considerada una estructura controvertida en su inauguración."
    }
}

for ciudad, info in ciudades.items():
    print("Ciudad: ", ciudad)
    print("País: ", info["país"])
    print("Población: ", info["población"])
    print("Dato interesante: ", info["dato"])
    print("-" * 20)
