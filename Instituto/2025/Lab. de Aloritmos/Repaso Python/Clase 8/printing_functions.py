def imprimir_modelos(disenos_no_imprimidos, modelos_completados):
  while disenos_no_imprimidos:
      diseno_actual = disenos_no_imprimidos.pop()
      print(f"Imprimiendo modelo: {diseno_actual}")
      modelos_completados.append(diseno_actual)

def mostrar_modelos_completados(modelos_completados):
  print("\nLos siguientes modelos han sido impresos:")
  for modelo_completado in modelos_completados:
      print(modelo_completado)