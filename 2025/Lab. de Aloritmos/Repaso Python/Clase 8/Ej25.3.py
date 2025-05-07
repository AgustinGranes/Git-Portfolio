def auto(fabricante, modelo, **caracteristicas):
  print(f"el fabricante del auto es {fabricante}, el modelo es {modelo}.")
  for key, value in caracteristicas.items():
    print(f"- {key}: {value}")

auto("Toyota", "Corolla", color="Rojo", placas="ABC123", motor="2.0")