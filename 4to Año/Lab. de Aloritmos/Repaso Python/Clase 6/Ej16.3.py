lenguajes_favoritos = {'Juan': 'python', 'Sara': 'c', 'Eduardo': 'rust', 'Agustina': 'c#'}
personas = ['Juan', 'Sara', 'Eduardo', 'Agustina', 'María', 'Pedro', 'Lucía', 'Carlos']

for persona in personas:
    if persona in lenguajes_favoritos:
        print(f"Gracias, {persona}, por responder la encuesta sobre tu lenguaje favorito.")
    else:
        print(f"Hola, {persona}, ¿te gustaría participar en la encuesta sobre lenguajes de programación?")
