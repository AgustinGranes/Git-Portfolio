lugares_favoritos = {
    "Ana": ["París", "Roma", "Tokio"],
    "Luis": ["Playa del Carmen", "San Carlos de Bariloche"],
    "María": ["Nueva York", "Venecia", "Machu Picchu"]
}

for nombre, lugares in lugares_favoritos.items():
    print("Nombre: ", nombre)
    print("Lugares favoritos: ", ", ".join(lugares))
    print("-" * 20)
