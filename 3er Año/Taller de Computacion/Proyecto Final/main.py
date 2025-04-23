import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
import json
from tkinter import messagebox
import random
import pygame

sesion = 0
cuenta = None


def iniciar_sesion():
    global sesion
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("green")

    app = customtkinter.CTk()
    app.geometry("600x600")
    app.title('Login')

    def button_function():
        app.destroy()
        global sesion
        sesion = 1
        iniciar_juego()

    # Cargar la imagen de fondo
    img1 = ImageTk.PhotoImage(Image.open(
        r"JUEGO COMPLETO\Juego (Main) y Recursos\pattern.png"))
    l1 = customtkinter.CTkLabel(master=app, image=img1)
    l1.place(relwidth=1, relheight=1)

    # Crear un frame para el login
    frame = customtkinter.CTkFrame(
        master=l1, width=320, height=450, corner_radius=15, fg_color="white")
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Cargar y redimensionar la imagen del logo
    img3 = Image.open(r"JUEGO COMPLETO\Juego (Main) y Recursos\logo.png")
    img3 = img3.resize((150, 150))
    logo_img = ImageTk.PhotoImage(img3)

    # Añadir la imagen del logo a un CTkLabel
    logo_label = customtkinter.CTkLabel(master=frame, image=logo_img, text="")
    logo_label.place(relx=0.5, y=20, anchor=tk.N)

    # Etiqueta de título
    l2 = customtkinter.CTkLabel(master=frame, text="Log in/Register Your Account",
                                font=("Helvetica", 22), text_color="black")
    l2.place(relx=0.5, y=200, anchor=tk.CENTER)

    entry1 = customtkinter.CTkEntry(
        master=frame, width=220, placeholder_text='Username')
    entry1.place(relx=0.5, y=250, anchor=tk.CENTER)

    entry2 = customtkinter.CTkEntry(
        master=frame, width=220, placeholder_text='Password', show="*")
    entry2.place(relx=0.5, y=300, anchor=tk.CENTER)

    def login_function():
        username = entry1.get()
        password = entry2.get()

        # Leer el archivo JSON
        try:
            with open('users.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {'users': []}

        # Verificar el usuario en el archivo JSON
        user_found = False
        for user in data['users']:
            if user['username'] == username and user['password'] == password:
                global cuenta
                cuenta = username
                user_found = True
                button_function()
                break

        if not user_found:
            messagebox.showerror(
                "Error", "Usuario o contraseña incorrectos (POSIBLE NECESIDAD DE REGISTRO)")

    def register_function():
        username = entry1.get()
        password = entry2.get()

        if len(username) < 5 or len(password) < 5:
            messagebox.showerror(
                "Error", "El nombre de usuario y la contraseña deben tener al menos 5 caracteres")
            return

        # Leer el archivo JSON
        try:
            with open('users.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {'users': []}

        # Verificar si el usuario ya existe
        for user in data['users']:
            if user['username'] == username:
                messagebox.showerror("Error", "El nombre de usuario ya existe")
                return

        # Agregar el nuevo usuario al archivo JSON
        data['users'].append(
            {"username": username, "password": password, "monedas": 0, "puntos": 0})

        # Guardar el archivo JSON actualizado
        with open('users.json', 'w') as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo(
            "Éxito", f"Usuario {username} registrado exitosamente!")
        button_function()

    button1 = customtkinter.CTkButton(
        master=frame, width=220, text="Login", command=login_function, corner_radius=6)
    button1.place(relx=0.5, y=350, anchor=tk.CENTER)

    button2 = customtkinter.CTkButton(
        master=frame, width=220, text="Register", command=register_function, corner_radius=6)
    button2.place(relx=0.5, y=400, anchor=tk.CENTER)

    app.mainloop()


def iniciar_juego():
    global cuenta, puntaje

    # Configuración de pygame para manejar la música
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(r"Juego (Main) y Recursos\musica.mp3")
        pygame.mixer.music.set_volume(0.5)
    except pygame.error as e:
        print(f"Error al cargar la música: {e}")

    # Lista de Cultura
    preguntas = [
        {"pregunta": "¿Cuál es el club con más títulos de la Liga de Campeones de la UEFA?",
         "opciones": ["Real Madrid", "Barcelona", "Manchester United", "AC Milan"],
         "respuesta": "Real Madrid"},
        {"pregunta": "¿Cuál es el país más grande del mundo por superficie?",
         "opciones": ["Rusia", "Canadá", "China", "Estados Unidos"],
         "respuesta": "Rusia"},
        {"pregunta": "¿Quién escribió 'Cien años de soledad'?",
         "opciones": ["Gabriel García Márquez", "Mario Vargas Llosa", "Julio Cortázar", "Jorge Luis Borges"],
         "respuesta": "Gabriel García Márquez"},
        {"pregunta": "¿Cuál es el río más largo del mundo?",
         "opciones": ["Amazonas", "Nilo", "Yangtsé", "Misisipi"],
         "respuesta": "Amazonas"},
        {"pregunta": "¿En qué año llegó el hombre a la Luna?",
         "opciones": ["1969", "1959", "1979", "1989"],
         "respuesta": "1969"},
        {"pregunta": "¿Cuál es la capital de Australia?",
         "opciones": ["Sídney", "Melbourne", "Canberra", "Brisbane"],
         "respuesta": "Canberra"},
        {"pregunta": "¿Quién pintó 'La última cena'?",
         "opciones": ["Leonardo da Vinci", "Miguel Ángel", "Vincent van Gogh", "Pablo Picasso"],
         "respuesta": "Leonardo da Vinci"},
        {"pregunta": "¿Cuál es el idioma más hablado en el mundo?",
         "opciones": ["Inglés", "Mandarín", "Español", "Hindú"],
         "respuesta": "Mandarín"},
        {"pregunta": "¿Cuál es el metal más abundante en la corteza terrestre?",
         "opciones": ["Hierro", "Aluminio", "Cobre", "Oro"],
         "respuesta": "Aluminio"},
        {"pregunta": "¿Qué país ganó la Copa Mundial de la FIFA 2018?",
         "opciones": ["Francia", "Croacia", "Brasil", "Alemania"],
         "respuesta": "Francia"},
        {"pregunta": "¿Cuál es el océano más grande del mundo?",
         "opciones": ["Atlántico", "Índico", "Ártico", "Pacífico"],
         "respuesta": "Pacífico"},
        {"pregunta": "¿Cuál es el planeta más cercano al sol?",
         "opciones": ["Venus", "Marte", "Mercurio", "Júpiter"],
         "respuesta": "Mercurio"},
        {"pregunta": "¿Quién es el autor de 'Don Quijote de la Mancha'?",
         "opciones": ["Miguel de Cervantes", "Lope de Vega", "Francisco de Quevedo", "Luis de Góngora"],
         "respuesta": "Miguel de Cervantes"},
        {"pregunta": "¿Cuál es el país con la mayor población del mundo?",
         "opciones": ["India", "Estados Unidos", "China", "Indonesia"],
         "respuesta": "China"},
        {"pregunta": "¿En qué continente se encuentra Egipto?",
         "opciones": ["Asia", "África", "Europa", "América"],
         "respuesta": "África"},
        {"pregunta": "¿Cuál es el animal terrestre más rápido del mundo?",
         "opciones": ["León", "Guepardo", "Tigre", "Leopardo"],
         "respuesta": "Guepardo"},
        {"pregunta": "¿Qué elemento químico tiene el símbolo 'O'?",
         "opciones": ["Oro", "Oxígeno", "Osmio", "Oganesón"],
         "respuesta": "Oxígeno"},
        {"pregunta": "¿Cuál es la capital de Japón?",
         "opciones": ["Osaka", "Tokio", "Kioto", "Nagoya"],
         "respuesta": "Tokio"},
        {"pregunta": "¿Quién fue el primer presidente de los Estados Unidos?",
         "opciones": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
         "respuesta": "George Washington"},
        {"pregunta": "¿Cuál es el desierto más grande del mundo?",
         "opciones": ["Sahara", "Gobi", "Kalahari", "Atacama"],
         "respuesta": "Sahara"},
        {"pregunta": "¿Qué país es conocido como la tierra del sol naciente?",
         "opciones": ["China", "Corea del Sur", "Japón", "Tailandia"],
         "respuesta": "Japón"},
        {"pregunta": "¿Cuál es el órgano más grande del cuerpo humano?",
         "opciones": ["Hígado", "Cerebro", "Piel", "Corazón"],
         "respuesta": "Piel"},
        {"pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
         "opciones": ["1939", "1941", "1935", "1945"],
         "respuesta": "1939"},
        {"pregunta": "¿Cuál es el idioma oficial de Brasil?",
         "opciones": ["Español", "Portugués", "Inglés", "Francés"],
         "respuesta": "Portugués"},
        {"pregunta": "¿Qué gas es esencial para la respiración humana?",
         "opciones": ["Nitrógeno", "Oxígeno", "Dióxido de carbono", "Hidrógeno"],
         "respuesta": "Oxígeno"},
        {"pregunta": "¿Cuál es la moneda oficial del Reino Unido?",
         "opciones": ["Euro", "Dólar", "Libra esterlina", "Franco"],
         "respuesta": "Libra esterlina"},
        {"pregunta": "¿Qué país tiene la mayor cantidad de islas en el mundo?",
         "opciones": ["Indonesia", "Filipinas", "Suecia", "Japón"],
         "respuesta": "Suecia"},
        {"pregunta": "¿Cuál es el nombre del famoso reloj en Londres?",
         "opciones": ["Big Ben", "Tower Clock", "London Eye", "Westminster Clock"],
         "respuesta": "Big Ben"},
        {"pregunta": "¿Qué vitamina es producida por el cuerpo cuando se expone al sol?",
         "opciones": ["Vitamina A", "Vitamina B", "Vitamina C", "Vitamina D"],
         "respuesta": "Vitamina D"},
        {"pregunta": "¿Cuál es el país más pequeño del mundo?",
         "opciones": ["Mónaco", "San Marino", "Liechtenstein", "Ciudad del Vaticano"],
         "respuesta": "Ciudad del Vaticano"},
        {"pregunta": "¿Cuál es la montaña más alta del mundo?",
         "opciones": ["K2", "Kangchenjunga", "Everest", "Lhotse"],
         "respuesta": "Everest"},
        {"pregunta": "¿Qué país es famoso por la Torre Eiffel?",
         "opciones": ["Italia", "España", "Francia", "Alemania"],
         "respuesta": "Francia"},
        {"pregunta": "¿Cuál es el océano más pequeño del mundo?",
         "opciones": ["Atlántico", "Índico", "Ártico", "Pacífico"],
         "respuesta": "Ártico"},
        {"pregunta": "¿Quién es conocido como el padre de la física moderna?",
         "opciones": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Niels Bohr"],
         "respuesta": "Albert Einstein"},
        {"pregunta": "¿Cuál es el país más poblado de África?",
         "opciones": ["Egipto", "Nigeria", "Sudáfrica", "Etiopía"],
         "respuesta": "Nigeria"},
        {"pregunta": "¿Qué instrumento musical tiene teclas blancas y negras?",
         "opciones": ["Guitarra", "Violín", "Piano", "Flauta"],
         "respuesta": "Piano"},
        {"pregunta": "¿Cuál es el país de origen de la pizza?",
         "opciones": ["Francia", "España", "Italia", "Grecia"],
         "respuesta": "Italia"},
        {"pregunta": "¿Qué planeta es conocido como el planeta rojo?",
         "opciones": ["Venus", "Marte", "Júpiter", "Saturno"],
         "respuesta": "Marte"},
        {"pregunta": "¿Cuál es el idioma oficial de Egipto?",
         "opciones": ["Inglés", "Francés", "Árabe", "Español"],
         "respuesta": "Árabe"},
        {"pregunta": "¿Qué país es famoso por el sushi?",
         "opciones": ["China", "Corea del Sur", "Japón", "Tailandia"],
         "respuesta": "Japón"},
        {"pregunta": "¿Cuál es el río más largo de África?",
         "opciones": ["Nilo", "Congo", "Níger", "Zambeze"],
         "respuesta": "Nilo"}, {"pregunta": "¿Cuál es el país más grande del mundo por superficie?", "opciones": ["Rusia", "Canadá", "China", "Estados Unidos"], "respuesta": "Rusia"},
        {"pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
            "opciones": ["1935", "1939", "1941", "1945"], "respuesta": "1939"},
        {"pregunta": "¿Cuál es el río más largo del mundo?", "opciones": [
            "Amazonas", "Nilo", "Yangtsé", "Misisipi"], "respuesta": "Nilo"},
        {"pregunta": "¿Quién pintó la Mona Lisa?", "opciones": [
            "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "respuesta": "Leonardo da Vinci"},
        {"pregunta": "¿Cuál es el planeta más grande del sistema solar?", "opciones": [
            "Tierra", "Marte", "Júpiter", "Saturno"], "respuesta": "Júpiter"},
        {"pregunta": "¿Cuál es la capital de Australia?", "opciones": [
            "Sídney", "Melbourne", "Canberra", "Brisbane"], "respuesta": "Canberra"},
        {"pregunta": "¿En qué continente se encuentra Egipto?", "opciones": [
            "Asia", "África", "Europa", "América"], "respuesta": "África"},
        {"pregunta": "¿Cuál es el idioma más hablado en el mundo?", "opciones": [
            "Inglés", "Español", "Chino mandarín", "Hindú"], "respuesta": "Chino mandarín"},
        {"pregunta": "¿Quién escribió 'Cien años de soledad'?", "opciones": [
            "Gabriel García Márquez", "Mario Vargas Llosa", "Julio Cortázar", "Isabel Allende"], "respuesta": "Gabriel García Márquez"},
        {"pregunta": "¿Cuál es el metal más abundante en la corteza terrestre?",
            "opciones": ["Hierro", "Aluminio", "Cobre", "Oro"], "respuesta": "Aluminio"},
        {"pregunta": "¿Cuál es el océano más grande del mundo?", "opciones": [
            "Atlántico", "Índico", "Ártico", "Pacífico"], "respuesta": "Pacífico"},
        {"pregunta": "¿En qué año llegó el hombre a la Luna?", "opciones": [
            "1965", "1969", "1972", "1975"], "respuesta": "1969"},
        {"pregunta": "¿Cuál es el animal terrestre más rápido?", "opciones": [
            "León", "Guepardo", "Tigre", "Caballo"], "respuesta": "Guepardo"},
        {"pregunta": "¿Cuál es el país con más medallas olímpicas?", "opciones": [
            "China", "Rusia", "Estados Unidos", "Alemania"], "respuesta": "Estados Unidos"},
        {"pregunta": "¿Cuál es el desierto más grande del mundo?", "opciones": [
            "Sahara", "Gobi", "Kalahari", "Atacama"], "respuesta": "Sahara"},
        {"pregunta": "¿Quién es el autor de 'Don Quijote de la Mancha'?", "opciones": [
            "Miguel de Cervantes", "Lope de Vega", "Francisco de Quevedo", "Luis de Góngora"], "respuesta": "Miguel de Cervantes"},
        {"pregunta": "¿Cuál es el país más poblado del mundo?", "opciones": [
            "India", "Estados Unidos", "Indonesia", "China"], "respuesta": "China"},
        {"pregunta": "¿Cuál es el elemento químico más abundante en el universo?", "opciones": [
            "Oxígeno", "Hidrógeno", "Carbono", "Nitrógeno"], "respuesta": "Hidrógeno"},
        {"pregunta": "¿Cuál es la montaña más alta del mundo?", "opciones": [
            "K2", "Kangchenjunga", "Everest", "Lhotse"], "respuesta": "Everest"},
        {"pregunta": "¿En qué año se disolvió la Unión Soviética?",
            "opciones": ["1989", "1990", "1991", "1992"], "respuesta": "1991"},
        {"pregunta": "¿Cuál es el país con más islas en el mundo?", "opciones": [
            "Indonesia", "Filipinas", "Suecia", "Japón"], "respuesta": "Suecia"},
        {"pregunta": "¿Cuál es el órgano más grande del cuerpo humano?", "opciones": [
            "Hígado", "Cerebro", "Piel", "Pulmones"], "respuesta": "Piel"},
        {"pregunta": "¿Cuál es el país con más volcanes activos?", "opciones": [
            "Japón", "Indonesia", "Estados Unidos", "Islandia"], "respuesta": "Indonesia"},
        {"pregunta": "¿Cuál es el deporte más popular del mundo?", "opciones": [
            "Baloncesto", "Críquet", "Fútbol", "Tenis"], "respuesta": "Fútbol"},
        {"pregunta": "¿Cuál es el libro más vendido de todos los tiempos?", "opciones": [
            "El Quijote", "La Biblia", "Harry Potter", "El Señor de los Anillos"], "respuesta": "La Biblia"},
        {"pregunta": "¿Cuál es el país más pequeño del mundo?", "opciones": [
            "Mónaco", "San Marino", "Liechtenstein", "Ciudad del Vaticano"], "respuesta": "Ciudad del Vaticano"},
        {"pregunta": "¿Cuál es el único mamífero que puede volar?", "opciones": [
            "Murciélago", "Ardilla voladora", "Colugo", "Pteropus"], "respuesta": "Murciélago"},
        {"pregunta": "¿Cuál es el inventor de la bombilla eléctrica?", "opciones": [
            "Nikola Tesla", "Thomas Edison", "Alexander Graham Bell", "Benjamin Franklin"], "respuesta": "Thomas Edison"},
        {"pregunta": "¿Cuál es el país con más lenguas oficiales?", "opciones": ["India", "Sudáfrica", "Suiza", "Papúa Nueva Guinea"], "respuesta": "India"}, {
            "pregunta": "¿Quién es considerado el máximo exponente del tango argentino?", "opciones": ["Carlos Gardel", "Astor Piazzolla", "Aníbal Troilo", "Osvaldo Pugliese"], "respuesta": "Carlos Gardel"},
        {"pregunta": "¿Cuál es la bebida tradicional de Argentina?",
            "opciones": ["Té", "Café", "Mate", "Chicha"], "respuesta": "Mate"},
        {"pregunta": "¿Qué famoso escritor argentino escribió 'El Aleph'?", "opciones": [
            "Julio Cortázar", "Adolfo Bioy Casares", "Jorge Luis Borges", "Ernesto Sábato"], "respuesta": "Jorge Luis Borges"},
        {"pregunta": "¿Cuál es el baile tradicional de Argentina?", "opciones": [
            "Samba", "Tango", "Cueca", "Joropo"], "respuesta": "Tango"},
        {"pregunta": "¿En qué ciudad se encuentra el Obelisco?", "opciones": [
            "Rosario", "Córdoba", "Buenos Aires", "Mendoza"], "respuesta": "Buenos Aires"},
        {"pregunta": "¿Cuál es el plato típico argentino que consiste en carne asada?",
            "opciones": ["Empanadas", "Asado", "Milanesa", "Locro"], "respuesta": "Asado"},
        {"pregunta": "¿Qué equipo de fútbol argentino es conocido como 'Los Millonarios'?", "opciones": [
            "Boca Juniors", "River Plate", "San Lorenzo", "Independiente"], "respuesta": "River Plate"},
        {"pregunta": "¿Qué famosa avenida de Buenos Aires es conocida por sus teatros?", "opciones": [
            "Avenida Corrientes", "Avenida de Mayo", "Avenida 9 de Julio", "Avenida Santa Fe"], "respuesta": "Avenida Corrientes"},
        {"pregunta": "¿Qué escritor argentino escribió 'Rayuela'?", "opciones": [
            "Jorge Luis Borges", "Adolfo Bioy Casares", "Julio Cortázar", "Ernesto Sábato"], "respuesta": "Julio Cortázar"},
        {"pregunta": "¿Cuál es la montaña más alta de Argentina?", "opciones": [
            "Cerro Torre", "Cerro Fitz Roy", "Aconcagua", "Cerro Catedral"], "respuesta": "Aconcagua"},
        {"pregunta": "¿Qué provincia argentina es famosa por sus viñedos?", "opciones": [
            "Salta", "Mendoza", "San Juan", "La Rioja"], "respuesta": "Mendoza"},
        {"pregunta": "¿Qué famoso revolucionario nació en Rosario, Argentina?", "opciones": [
            "Simón Bolívar", "José de San Martín", "Che Guevara", "Manuel Belgrano"], "respuesta": "Che Guevara"},
        {"pregunta": "¿Cuál es el nombre del famoso barrio de Buenos Aires conocido por sus casas coloridas?",
            "opciones": ["Recoleta", "Palermo", "La Boca", "San Telmo"], "respuesta": "La Boca"},
        {"pregunta": "¿Qué famosa cantante argentina es conocida como 'La Negra'?", "opciones": [
            "Mercedes Sosa", "Soledad Pastorutti", "Gilda", "Valeria Lynch"], "respuesta": "Mercedes Sosa"},
        {"pregunta": "¿Cuál es el nombre del famoso teatro de ópera en Buenos Aires?", "opciones": [
            "Teatro Colón", "Teatro San Martín", "Teatro Gran Rex", "Teatro Nacional Cervantes"], "respuesta": "Teatro Colón"},
        {"pregunta": "¿Qué famoso festival de cine se celebra en Mar del Plata?", "opciones": [
            "Festival de Cannes", "Festival de Berlín", "Festival de Mar del Plata", "Festival de Venecia"], "respuesta": "Festival de Mar del Plata"},
        {"pregunta": "¿Qué famoso pintor argentino es conocido por sus obras surrealistas?", "opciones": [
            "Antonio Berni", "Xul Solar", "Benito Quinquela Martín", "Raúl Soldi"], "respuesta": "Xul Solar"},
        {"pregunta": "¿Cuál es el nombre del famoso estadio de fútbol de Boca Juniors?", "opciones": [
            "Monumental", "La Bombonera", "El Cilindro", "El Nuevo Gasómetro"], "respuesta": "La Bombonera"},
        {"pregunta": "¿Qué famosa escritora argentina escribió 'La casa de los conejos'?", "opciones": [
            "Silvina Ocampo", "María Teresa Andruetto", "Laura Alcoba", "Samanta Schweblin"], "respuesta": "Laura Alcoba"},
        {"pregunta": "¿Qué famoso músico argentino es conocido por su banda 'Soda Stereo'?", "opciones": [
            "Charly García", "Luis Alberto Spinetta", "Gustavo Cerati", "Fito Páez"], "respuesta": "Gustavo Cerati"},
        {"pregunta": "¿Cuál es el nombre del famoso barrio de Buenos Aires conocido por su vida nocturna?",
            "opciones": ["Recoleta", "Palermo", "San Telmo", "Belgrano"], "respuesta": "Palermo"},
        {"pregunta": "¿Qué famoso escritor argentino escribió 'Sobre héroes y tumbas'?", "opciones": [
            "Jorge Luis Borges", "Adolfo Bioy Casares", "Julio Cortázar", "Ernesto Sábato"], "respuesta": "Ernesto Sábato"},
        {"pregunta": "¿Cuál es el nombre del famoso parque en Buenos Aires conocido por su rosedal?", "opciones": [
            "Parque Lezama", "Parque Centenario", "Parque Tres de Febrero", "Parque Chacabuco"], "respuesta": "Parque Tres de Febrero"},
        {"pregunta": "¿Qué famoso cantante argentino es conocido por la canción 'El amor después del amor'?", "opciones": [
            "Charly García", "Luis Alberto Spinetta", "Gustavo Cerati", "Fito Páez"], "respuesta": "Fito Páez"},
        {"pregunta": "¿Cuál es el nombre del famoso barrio de Buenos Aires conocido por su feria de antigüedades?",
            "opciones": ["Recoleta", "Palermo", "San Telmo", "Belgrano"], "respuesta": "San Telmo"},
        {"pregunta": "¿Qué famosa actriz argentina es conocida por su papel en 'La historia oficial'?", "opciones": [
            "Norma Aleandro", "Graciela Borges", "Mercedes Morán", "Cecilia Roth"], "respuesta": "Norma Aleandro"},
        {"pregunta": "¿Cuál es el nombre del famoso barrio de Buenos Aires conocido por su arquitectura francesa?",
            "opciones": ["Recoleta", "Palermo", "San Telmo", "Belgrano"], "respuesta": "Recoleta"},
        {"pregunta": "¿Qué famoso director de cine argentino dirigió 'El secreto de sus ojos'?", "opciones": [
            "Juan José Campanella", "Luis Puenzo", "Pablo Trapero", "Damián Szifron"], "respuesta": "Juan José Campanella"},
        {"pregunta": "¿Cuál es el nombre del famoso barrio de Buenos Aires conocido por su jardín japonés?",
            "opciones": ["Recoleta", "Palermo", "San Telmo", "Belgrano"], "respuesta": "Palermo"},
        {"pregunta": "¿Qué famoso músico argentino es conocido por su banda 'Los Fabulosos Cadillacs'?", "opciones": [
            "Charly García", "Luis Alberto Spinetta", "Vicentico", "Fito Páez"], "respuesta": "Vicentico"}
    ]

    def cargar_monedas():
        global monedas
        try:
            with open('users.json', 'r') as f:
                data = json.load(f)
            for user in data['users']:
                if user['username'] == cuenta:
                    monedas = user['monedas']
                    break
        except FileNotFoundError:
            monedas = 0
        return monedas

    monedas = cargar_monedas()

    def guardar_monedas():
        global cuenta, monedas
        try:
            with open('users.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {'users': []}

        for user in data['users']:
            if user['username'] == cuenta:
                user['monedas'] = monedas
                break

        with open('users.json', 'w') as f:
            json.dump(data, f, indent=4)

    class JuegoApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Juego de preguntas Huergo :)")
            self.root.geometry("800x600")
            self.root.grid_rowconfigure(0, weight=1)
            self.root.grid_columnconfigure(0, weight=1)

            # Fondo de pantalla
            self.background_image = tk.PhotoImage(file=r"Juego (Main) y Recursos\fondo.png")
            self.background_label = tk.Label(root, image=self.background_image)
            self.background_label.place(relwidth=1, relheight=1)

            self.preguntas_resueltas = 0
            self.puntos = 0
            self.monedas = monedas

            # Crea el menú principal
            self.menu = tk.Frame(root, bg="white")
            self.menu.pack(expand=True)

            # Mostrar la cantidad de monedas en la parte superior derecha
            self.monedas_frame = tk.Frame(root, bg="white")
            self.monedas_frame.pack(anchor="ne", padx=10, pady=10)

            self.moneda_image = tk.PhotoImage(file=r"Juego (Main) y Recursos\moneda.png").subsample(30)
            self.moneda_label = tk.Label(
                self.monedas_frame, image=self.moneda_image, bg="white")
            self.moneda_label.pack(side="left")

            self.monedas_text_label = tk.Label(
                self.monedas_frame, text=f"{self.monedas}", font=("Helvetica", 32), bg="white")
            self.monedas_text_label.pack(side="left")

            # Centrar el logo y los botones
            self.logo = tk.PhotoImage(file=r"Juego (Main) y Recursos\logo.png").subsample(2)
            self.logo_label = tk.Label(self.menu, image=self.logo, bg="white")
            self.logo_label.grid(row=0, column=0, pady=10)

            # Botones del menú
            self.jugar_button = tk.Button(self.menu, text="Jugar", command=self.iniciar_juego, font=("Helvetica", 18),
                                          bg="white", fg="black", activebackground="#ececec", borderwidth=0)
            self.jugar_button.grid(row=1, column=0, pady=5)

            self.config_button = tk.Button(self.menu, text="Configuración", command=self.abrir_configuracion, font=("Helvetica", 18),
                                           bg="white", fg="black", activebackground="#ececec", borderwidth=0)
            self.config_button.grid(row=2, column=0, pady=5)

            self.tutorial_button = tk.Button(self.menu, text="Tutorial", command=self.mostrar_tutorial, font=("Helvetica", 18),
                                             bg="white", fg="black", activebackground="#ececec", borderwidth=0)
            self.tutorial_button.grid(row=3, column=0, pady=5)

            self.ranking_button = tk.Button(self.menu, text="Ranking", command=self.mostrar_ranking, font=("Helvetica", 18),
                                             bg="white", fg="black", activebackground="#ececec", borderwidth=0)
            self.ranking_button.grid(row=4, column=0, pady=5)

            self.salir_button = tk.Button(self.menu, text="Salir", command=root.quit, font=("Helvetica", 18),
                                          bg="white", fg="black", activebackground="#ececec", borderwidth=0)
            self.salir_button.grid(row=5, column=0, pady=5)

            # Aplicar efectos de hover en los botones
            for button in [self.jugar_button, self.config_button, self.tutorial_button, self.salir_button]:
                button.bind("<Enter>", self.on_enter)
                button.bind("<Leave>", self.on_leave)

            # Aplicar efectos de hover en los botones
            for button in [self.jugar_button, self.config_button, self.salir_button, self.ranking_button, self.tutorial_button]:
                button.bind("<Enter>", self.on_enter)
                button.bind("<Leave>", self.on_leave)

        def on_enter(self, e):
            e.widget['background'] = '#d1d1d1'

        def on_leave(self, e):
            e.widget['background'] = 'white'

        def iniciar_juego(self):
            self.ocultar_monedas()
            self.puntos = 0
            self.preguntas_resueltas = 0
            self.menu.pack_forget()

            self.juego_frame = tk.Frame(self.root, bg="white")
            self.juego_frame.pack(fill=tk.BOTH, expand=True)  # Cambios aquí

            # Centrar elementos en el frame del juego
            self.puntaje_label = tk.Label(
                self.juego_frame, text=f"Puntos: {self.puntos}", font=("Helvetica", 18), bg="white")
            self.puntaje_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

            self.monedas_label = tk.Label(
                self.juego_frame, text=f"Monedas: {self.monedas}", font=("Helvetica", 18), bg="white")
            self.monedas_label.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

            self.pregunta_label = tk.Label(
                self.juego_frame, text="", wraplength=400, font=("Helvetica", 18), bg="white")
            self.pregunta_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

            # Botones de respuesta
            self.boton_respuesta1 = tk.Button(self.juego_frame, text="", command=lambda: self.verificar_respuesta(0), width=30, font=("Helvetica", 14),
                                              bg="white", activebackground="#ececec", borderwidth=0)
            self.boton_respuesta1.place(
                relx=0.4, rely=0.5, anchor=tk.CENTER, x=-75)

            self.boton_respuesta2 = tk.Button(self.juego_frame, text="", command=lambda: self.verificar_respuesta(1), width=30, font=("Helvetica", 14),
                                              bg="white", activebackground="#ececec", borderwidth=0)
            self.boton_respuesta2.place(
                relx=0.6, rely=0.5, anchor=tk.CENTER, x=75)

            self.boton_respuesta3 = tk.Button(self.juego_frame, text="", command=lambda: self.verificar_respuesta(2), width=30, font=("Helvetica", 14),
                                              bg="white", activebackground="#ececec", borderwidth=0)
            self.boton_respuesta3.place(
                relx=0.4, rely=0.6, anchor=tk.CENTER, x=-75)

            self.boton_respuesta4 = tk.Button(self.juego_frame, text="", command=lambda: self.verificar_respuesta(3), width=30, font=("Helvetica", 14),
                                              bg="white", activebackground="#ececec", borderwidth=0)
            self.boton_respuesta4.place(
                relx=0.6, rely=0.6, anchor=tk.CENTER, x=75)

            self.numero_pregunta_label = tk.Label(
                self.juego_frame, text="Preguntas respondidas: 0/10", font=("Helvetica", 18), bg="white")
            self.numero_pregunta_label.place(
                relx=0.5, rely=0.72, anchor=tk.CENTER)

            # Botón de finalizar
            self.finalizar_button = tk.Button(self.juego_frame, text="Finalizar", command=self.finalizar_juego, font=("Helvetica", 18),
                                              bg="white", activebackground="#ececec", borderwidth=0)
            self.finalizar_button.place(relx=0.5, rely=0.77, anchor=tk.CENTER)

            pygame.mixer.music.play(-1)
            self.siguiente_pregunta()

        def mostrar_ranking(self):
            self.ocultar_monedas()
            self.menu.pack_forget()

            # Crear un frame que ocupe toda la pantalla
            self.ranking_frame = tk.Frame(self.root, bg="white")
            self.ranking_frame.pack(fill=tk.BOTH, expand=True)

            # Crear un canvas para el desplazamiento
            canvas = tk.Canvas(self.ranking_frame, bg="white")
            scroll_y = tk.Scrollbar(self.ranking_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas, bg="white")

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

            canvas.pack(side="left", fill="both", expand=True)
            scroll_y.pack(side="right", fill="y")
            canvas.configure(yscrollcommand=scroll_y.set)

            # Cargar datos del archivo JSON
            try:
                with open('users.json', 'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = {'users': []}

            # Ordenar usuarios por monedas
            usuarios_ordenados = sorted(data['users'], key=lambda x: x['monedas'], reverse=True)

            # Crear cabecera
            tk.Label(scrollable_frame, text="", font=("Helvetica", 18), bg="white").grid(row=0, column=1, padx=20, pady=10)
            tk.Label(scrollable_frame, text="", font=("Helvetica", 18), bg="white").grid(row=0, column=2, padx=20, pady=10)
            tk.Label(scrollable_frame, text="", font=("Helvetica", 18), bg="white").grid(row=0, column=3, padx=20, pady=10)
            tk.Label(scrollable_frame, text="", font=("Helvetica", 18), bg="white").grid(row=0, column=4, padx=20, pady=10)
            tk.Label(scrollable_frame, text="", font=("Helvetica", 18), bg="white").grid(row=0, column=5, padx=20, pady=10)
            tk.Label(scrollable_frame, text="", font=("Helvetica", 18), bg="white").grid(row=0, column=6, padx=20, pady=10)
            tk.Label(scrollable_frame, text="", font=("Helvetica", 18), bg="white").grid(row=0, column=7, padx=20, pady=10)
            tk.Label(scrollable_frame, text="", font=("Helvetica", 18), bg="white").grid(row=0, column=8, padx=20, pady=10)
            tk.Label(scrollable_frame, text="", font=("Helvetica", 18), bg="white").grid(row=0, column=9, padx=20, pady=10)
            tk.Label(scrollable_frame, text="", font=("Helvetica", 18), bg="white").grid(row=0, column=10, padx=20, pady=10)
            tk.Label(scrollable_frame, text="", font=("Helvetica", 18), bg="white").grid(row=0, column=11, padx=20, pady=10)
            tk.Label(scrollable_frame, text="", font=("Helvetica", 18), bg="white").grid(row=0, column=12, padx=20, pady=10)
            tk.Label(scrollable_frame, text="", font=("Helvetica", 18), bg="white").grid(row=0, column=13, padx=20, pady=10)
            tk.Label(scrollable_frame, text="", font=("Helvetica", 18), bg="white").grid(row=0, column=14, padx=20, pady=10)
            tk.Label(scrollable_frame, text="PUESTO", font=("Helvetica", 18), bg="white").grid(row=0, column=15, padx=20, pady=10)
            tk.Label(scrollable_frame, text="USUARIO", font=("Helvetica", 18), bg="white").grid(row=0, column=16, padx=20, pady=10)
            tk.Label(scrollable_frame, text="MONEDAS", font=("Helvetica", 18), bg="white").grid(row=0, column=17, padx=20, pady=10)

            # Agregar los datos al ranking
            for index, user in enumerate(usuarios_ordenados):
                tk.Label(scrollable_frame, text="", font=("Helvetica", 14), bg="white").grid(row=index + 1, column=1, padx=20, pady=5)
                tk.Label(scrollable_frame, text="", font=("Helvetica", 14), bg="white").grid(row=index + 1, column=2, padx=20, pady=5)
                tk.Label(scrollable_frame, text="", font=("Helvetica", 14), bg="white").grid(row=index + 1, column=3, padx=20, pady=5)
                tk.Label(scrollable_frame, text="", font=("Helvetica", 14), bg="white").grid(row=index + 1, column=4, padx=20, pady=5)
                tk.Label(scrollable_frame, text="", font=("Helvetica", 14), bg="white").grid(row=index + 1, column=5, padx=20, pady=5)
                tk.Label(scrollable_frame, text="", font=("Helvetica", 14), bg="white").grid(row=index + 1, column=6, padx=20, pady=5)
                tk.Label(scrollable_frame, text="", font=("Helvetica", 14), bg="white").grid(row=index + 1, column=7, padx=20, pady=5)
                tk.Label(scrollable_frame, text="", font=("Helvetica", 14), bg="white").grid(row=index + 1, column=8, padx=20, pady=5)
                tk.Label(scrollable_frame, text="", font=("Helvetica", 14), bg="white").grid(row=index + 1, column=9, padx=20, pady=5)
                tk.Label(scrollable_frame, text="", font=("Helvetica", 14), bg="white").grid(row=index + 1, column=10, padx=20, pady=5)
                tk.Label(scrollable_frame, text="", font=("Helvetica", 14), bg="white").grid(row=index + 1, column=11, padx=20, pady=5)
                tk.Label(scrollable_frame, text="", font=("Helvetica", 14), bg="white").grid(row=index + 1, column=12, padx=20, pady=5)
                tk.Label(scrollable_frame, text="", font=("Helvetica", 14), bg="white").grid(row=index + 1, column=13, padx=20, pady=5)
                tk.Label(scrollable_frame, text="", font=("Helvetica", 14), bg="white").grid(row=index + 1, column=14, padx=20, pady=5)
                tk.Label(scrollable_frame, text=index + 1, font=("Helvetica", 14), bg="white").grid(row=index + 1, column=15, padx=20, pady=5)
                tk.Label(scrollable_frame, text=user['username'], font=("Helvetica", 14), bg="white").grid(row=index + 1, column=16, padx=20, pady=5)
                tk.Label(scrollable_frame, text=user['monedas'], font=("Helvetica", 14), bg="white").grid(row=index + 1, column=17, padx=20, pady=5)

            # Botón de volver al menú
            volver_button = tk.Button(self.ranking_frame, text="Volver al Menú", command=self.volver_menu, font=("Helvetica", 18),
                                    bg="white", activebackground="#ececec", borderwidth=0)
            volver_button.pack(pady=(10, 20))  # Agrega separación arriba y abajo

        def abrir_configuracion(self):
            self.menu.pack_forget()

            # Ocultar el frame de monedas
            self.monedas_frame.pack_forget()

            self.config_frame = tk.Frame(self.root, bg="white")
            self.config_frame.pack(fill=tk.BOTH, expand=True)

            # Iniciar música en configuración
            pygame.mixer.music.play(-1)

            # Centrar la etiqueta del volumen
            self.volumen_label = tk.Label(
                self.config_frame, text="Volumen de la música (0 a 1):", font=("Helvetica", 18), bg="white")
            self.volumen_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

            # Centrar el slider de volumen
            self.volumen_slider = tk.Scale(self.config_frame, from_=0, to=1, resolution=0.1,
                                        orient=tk.HORIZONTAL, command=self.cambiar_volumen, bg="white")
            self.volumen_slider.set(pygame.mixer.music.get_volume() * 10)  # Ajusta el slider al volumen actual
            self.volumen_slider.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            # Centrar el botón de volver
            self.volver_button = tk.Button(self.config_frame, text="Volver al menú", command=self.volver_menu, font=("Helvetica", 18),
                                        bg="white", activebackground="#ececec", borderwidth=0)
            self.volver_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

            # Efectos de hover en el botón de volver
            self.volver_button.bind("<Enter>", self.on_enter)
            self.volver_button.bind("<Leave>", self.on_leave)

        def cambiar_volumen(self, valor):
            pygame.mixer.music.set_volume(float(valor))

        def volver_menu(self):
            # Detener música al volver al menú
            pygame.mixer.music.stop()

            # Solo oculta config_frame si existe
            if hasattr(self, 'config_frame'):
                self.config_frame.pack_forget()
                
            # Ocultar el frame del tutorial
            if hasattr(self, 'tutorial_frame'):
                self.tutorial_frame.pack_forget()

            # Ocultar el frame del ranking si existe
            if hasattr(self, 'ranking_frame'):
                self.ranking_frame.pack_forget()  # Oculta el ranking frame
                del self.ranking_frame  # Elimina la referencia del ranking frame
                
            self.menu.pack(expand=True)
            self.mostrar_monedas()  # Asegúrate de que las monedas se muestren al volver
            self.actualizar_monedas()

        def mostrar_tutorial(self):
            self.ocultar_monedas()
            self.menu.pack_forget()
            self.tutorial_frame = tk.Frame(self.root, bg="white")
            self.tutorial_frame.pack(fill=tk.BOTH, expand=True)

            self.textos = [
                "Para empezar, tenemos que conocer nuestra interfaz y de que consta la misma, que funcion cumple cada cosa y como poder jugar correctamente.",
                "Contamos con un tutorial (que es la pestaña donde te encuentras actualmente)",
                "Un contador de monedas que se despliega debajo en la esquina inferior derecha, donde podemos ver las monedas que recolectamos.",
                "Un botón de configuración, donde por ejemplo se puede modificar el volumen del juego a como se requiera.",
                "Y por último, el botón de juego, el cual al presionarlo accedes automáticamente al juego y en el cual se deben responder preguntas.",
                "Una pregunta correcta, vale 10 puntos, y por cada punto se te otorga una moneda al final. Te deseamos suerte en tu experiencia, ¡ojalá ganes muchas monedas!"
            ]

            self.indice = 0
            self.contador_siguiente = 0  # Contador para el botón "Siguiente"

            self.texto_label = tk.Label(
                self.tutorial_frame, text=self.textos[self.indice], font=("Helvetica", 18), bg="white", wraplength=700)
            self.texto_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

            self.siguiente_button = tk.Button(self.tutorial_frame, text="Siguiente", command=self.siguiente_texto, font=("Helvetica", 18),
                                            bg="white", activebackground="#ececec", borderwidth=0)
            self.siguiente_button.place(relx=0.5, rely=0.57, anchor=tk.CENTER)

            self.finalizar_button = tk.Button(self.tutorial_frame, text="Finalizar", command=self.volver_menu, font=("Helvetica", 18),
                                            bg="white", activebackground="#ececec", borderwidth=0)
            self.finalizar_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        def siguiente_texto(self):
            self.indice += 1
            self.contador_siguiente += 1  # Incrementar contador al presionar el botón

            # Verificar si se debe mover el botón
            if self.contador_siguiente >= 5:
                self.siguiente_button.place(relx=200, rely=200)  # Mover el botón a una nueva posición

            if self.indice < len(self.textos):
                self.texto_label.config(text=self.textos[self.indice])
                # También puedes ocultar el botón si se llega al último texto
            else:
                self.siguiente_button.pack_forget()  # Asegurarse de ocultar el botón si se supera el índice

        def siguiente_pregunta(self):
            if self.preguntas_resueltas >= 10:
                messagebox.showinfo(
                    "Fin del juego", f"Has respondido 10 preguntas. Tu puntaje final es {self.puntos}.")
                self.finalizar_juego()
                return

            self.preguntas_resueltas += 1
            self.numero_pregunta_label.config(
                text=f"Preguntas respondidas: {self.preguntas_resueltas}/10")

            # Selecciona una pregunta aleatoria de la lista
            self.pregunta_actual = random.choice(preguntas)

            # Actualiza la etiqueta de la pregunta
            self.pregunta_label.config(text=self.pregunta_actual["pregunta"])

            # Mezcla las opciones de respuesta aleatoriamente
            opciones = self.pregunta_actual["opciones"]
            random.shuffle(opciones)

            # Configura el texto de los botones de respuesta
            self.boton_respuesta1.config(text=opciones[0])
            self.boton_respuesta2.config(text=opciones[1])
            self.boton_respuesta3.config(text=opciones[2])
            self.boton_respuesta4.config(text=opciones[3])

        def verificar_respuesta(self, opcion):
            respuesta_usuario = self.pregunta_actual["opciones"][opcion]
            if respuesta_usuario == self.pregunta_actual["respuesta"]:
                self.puntos += 10
                messagebox.showinfo("Correcto", "¡Respuesta correcta!")
            else:
                messagebox.showerror(
                    "Incorrecto", f"Respuesta incorrecta. La respuesta correcta es: {self.pregunta_actual['respuesta']}")

            self.puntaje_label.config(text=f"Puntos: {self.puntos}")
            self.siguiente_pregunta()

        def finalizar_juego(self):
            self.monedas += self.puntos
            global monedas
            monedas = self.monedas
            guardar_monedas()
            messagebox.showinfo(
                "Juego finalizado", f"Has finalizado el juego con {self.puntos} puntos. Ahora tienes {self.monedas} monedas.")
            self.juego_frame.pack_forget()
            pygame.mixer.music.stop()
            self.menu.pack(expand=True)
            self.mostrar_monedas()
            self.actualizar_monedas()

        def actualizar_monedas(self):
            self.monedas_text_label.config(text=f"{self.monedas}")

        def ocultar_monedas(self):
            self.monedas_frame.pack_forget()

        def mostrar_monedas(self):
            self.monedas_frame.pack(anchor="ne", padx=10, pady=10)

    root = tk.Tk()
    app = JuegoApp(root)
    root.mainloop()


# Al iniciar el programa, se verifica el estado de la sesión
if sesion == 0:
    iniciar_sesion()
else:
    iniciar_juego()