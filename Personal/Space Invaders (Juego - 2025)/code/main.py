import pygame, sys
import json
import os
from player import Player
import obstacle
from alien import Alien, Extra
from random import choice, randint
from laser import Laser

# Obtener el directorio actual del script
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)

def get_resource_path(filename):
    """Obtiene la ruta completa de un archivo de recursos"""
    return os.path.join(PARENT_DIR, filename)

# Aumentar el tamaño de la pantalla
ancho_pantalla = 800
alto_pantalla = 700

# Definir colores para facilitar su uso
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS_OSCURO = (30, 30, 30)
ROJO = (241, 79, 80)
VERDE = (80, 241, 80)

# Configuración de volumen
niveles_volumen = {
    "musica": 0.2,
    "efectos": 0.5
}

# Cargar/crear archivo de puntuaciones
def cargar_puntuacion_maxima():
    archivo_puntuacion = get_resource_path('highscore.json')
    if os.path.exists(archivo_puntuacion):
        try:
            with open(archivo_puntuacion, 'r') as archivo:
                datos = json.load(archivo)
                return datos.get('puntuacion_maxima', 0)
        except:
            return 0
    return 0

def guardar_puntuacion_maxima(puntuacion, nombre="Jugador"):
    archivo_puntuacion = get_resource_path('highscore.json')
    try:
        # Leer ranking existente
        ranking = []
        if os.path.exists(archivo_puntuacion):
            with open(archivo_puntuacion, 'r') as archivo:
                datos = json.load(archivo)
                if isinstance(datos, dict) and 'ranking' in datos:
                    ranking = datos['ranking']
                elif 'puntuacion_maxima' in datos:
                    ranking = [("Jugador", datos['puntuacion_maxima'])]
        # Agregar nueva puntuación
        ranking.append((nombre, puntuacion))
        # Ordenar y dejar top 10
        ranking = sorted(ranking, key=lambda x: x[1], reverse=True)[:10]
        with open(archivo_puntuacion, 'w') as archivo:
            json.dump({'ranking': ranking}, archivo)
    except Exception as e:
        print(f"Error al guardar puntuación: {e}")

class Boton:
    def __init__(self, texto, ancho, alto, pos, fuente, color_fondo=(40, 40, 40, 180), color_hover=(80, 80, 80, 220), color_borde=(255,255,255,80), radio=16):
        self.texto = texto
        self.ancho = ancho
        self.alto = alto
        self.pos = pos
        self.fuente = fuente
        self.rect = pygame.Rect(pos[0], pos[1], ancho, alto)
        self.click = False
        self.color_fondo = color_fondo
        self.color_hover = color_hover
        self.color_borde = color_borde
        self.radio = radio
        self.hover = False

    def dibujar(self, pantalla):
        pos_raton = pygame.mouse.get_pos()
        self.hover = self.rect.collidepoint(pos_raton)
        color = self.color_hover if self.hover else self.color_fondo
        # Crear superficie con alpha para transparencia
        boton_surface = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA)
        pygame.draw.rect(boton_surface, color, (0, 0, self.ancho, self.alto), border_radius=self.radio)
        pygame.draw.rect(boton_surface, self.color_borde, (0, 0, self.ancho, self.alto), 2, border_radius=self.radio)
        pantalla.blit(boton_surface, self.pos)
        # Centrar texto
        superficie_texto = self.fuente.render(self.texto, True, (255,255,255) if self.hover else (220,220,220))
        x_texto = self.pos[0] + (self.ancho - superficie_texto.get_width()) // 2
        y_texto = self.pos[1] + (self.alto - superficie_texto.get_height()) // 2
        pantalla.blit(superficie_texto, (x_texto, y_texto))
        return self.hover

def mostrar_menu():
    pantalla.fill(GRIS_OSCURO)
    pos_raton = pygame.mouse.get_pos()
    # Overlay semitransparente
    overlay = pygame.Surface((ancho_pantalla, alto_pantalla), pygame.SRCALPHA)
    overlay.fill((20, 20, 20, 180))
    pantalla.blit(overlay, (0, 0))
    # Logo centrado
    try:
        logo = pygame.image.load(get_resource_path('graphics/logo.png')).convert_alpha()
        ancho_logo = min(320, ancho_pantalla * 0.6)
        alto_logo = ancho_logo * (logo.get_height() / logo.get_width())
        logo = pygame.transform.smoothscale(logo, (int(ancho_logo), int(alto_logo)))
        x_logo = (ancho_pantalla - logo.get_width()) // 2
        y_logo = 60
        pantalla.blit(logo, (x_logo, y_logo))
        inicio_y = y_logo + logo.get_height() + 40
    except:
        inicio_y = 100
    # Opciones de menú ampliadas
    opciones_menu = ["Jugar", "Multijugador", "Opciones", "Ranking", "Créditos", "Salir"]
    ancho_boton = 260
    alto_boton = 48
    espacio_boton = 18
    botones = []
    fuente_menu = pygame.font.Font(get_resource_path('font/Pixeled.ttf'), 22)
    for i, opcion in enumerate(opciones_menu):
        x_boton = (ancho_pantalla - ancho_boton) // 2
        y_boton = inicio_y + i * (alto_boton + espacio_boton)
        boton = Boton(opcion, ancho_boton, alto_boton, (x_boton, y_boton), fuente_menu)
        boton.dibujar(pantalla)
        botones.append((boton, opcion))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for boton, opcion in botones:
                if boton.rect.collidepoint(pos_raton):
                    if opcion == "Salir":
                        pygame.quit()
                        sys.exit()
                    elif opcion == "Jugar":
                        iniciar_cuenta_atras()
                        return {"accion": "jugar", "modo": "individual"}
                    elif opcion == "Multijugador":
                        iniciar_cuenta_atras()
                        return {"accion": "jugar", "modo": "multi"}
                    elif opcion == "Opciones":
                        return {"accion": "opciones"}
                    elif opcion == "Ranking":
                        return {"accion": "ranking"}
                    elif opcion == "Créditos":
                        return {"accion": "creditos"}
    return {"accion": "menu"}

def mostrar_opciones():
    pantalla.fill(GRIS_OSCURO)
    overlay = pygame.Surface((ancho_pantalla, alto_pantalla), pygame.SRCALPHA)
    overlay.fill((20, 20, 20, 200))
    pantalla.blit(overlay, (0, 0))
    titulo = fuente_grande.render("OPCIONES", True, BLANCO)
    rect_titulo = titulo.get_rect(center=(ancho_pantalla//2, 90))
    pantalla.blit(titulo, rect_titulo)
    fuente_opciones = pygame.font.Font(get_resource_path('font/Pixeled.ttf'), 18)
    texto_musica = fuente_opciones.render(f"Música: {int(niveles_volumen['musica']*100)}%", True, BLANCO)
    rect_texto_musica = texto_musica.get_rect(center=(ancho_pantalla//2, 200))
    pantalla.blit(texto_musica, rect_texto_musica)
    texto_efectos = fuente_opciones.render(f"Efectos: {int(niveles_volumen['efectos']*100)}%", True, BLANCO)
    rect_texto_efectos = texto_efectos.get_rect(center=(ancho_pantalla//2, 270))
    pantalla.blit(texto_efectos, rect_texto_efectos)
    # Botones de volumen
    boton_musica_menos = Boton("-", 48, 48, (ancho_pantalla//2 - 120, 180), fuente_grande)
    boton_musica_menos.dibujar(pantalla)
    boton_musica_mas = Boton("+", 48, 48, (ancho_pantalla//2 + 72, 180), fuente_grande)
    boton_musica_mas.dibujar(pantalla)
    boton_efectos_menos = Boton("-", 48, 48, (ancho_pantalla//2 - 120, 250), fuente_grande)
    boton_efectos_menos.dibujar(pantalla)
    boton_efectos_mas = Boton("+", 48, 48, (ancho_pantalla//2 + 72, 250), fuente_grande)
    boton_efectos_mas.dibujar(pantalla)
    # Botón volver
    boton_volver = Boton("Volver", 200, 48, ((ancho_pantalla - 200)//2, 370), fuente_grande)
    boton_volver.dibujar(pantalla)
    pos_raton = pygame.mouse.get_pos()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver.rect.collidepoint(pos_raton):
                return {"accion": "menu"}
            if boton_musica_menos.rect.collidepoint(pos_raton):
                niveles_volumen["musica"] = max(0.0, round(niveles_volumen["musica"] - 0.1, 1))
                actualizar_volumenes()
            elif boton_musica_mas.rect.collidepoint(pos_raton):
                niveles_volumen["musica"] = min(1.0, round(niveles_volumen["musica"] + 0.1, 1))
                actualizar_volumenes()
            if boton_efectos_menos.rect.collidepoint(pos_raton):
                niveles_volumen["efectos"] = max(0.0, round(niveles_volumen["efectos"] - 0.1, 1))
                actualizar_volumenes()
            elif boton_efectos_mas.rect.collidepoint(pos_raton):
                niveles_volumen["efectos"] = min(1.0, round(niveles_volumen["efectos"] + 0.1, 1))
                actualizar_volumenes()
    return {"accion": "opciones"}

def actualizar_volumenes():
    # Actualizar volúmenes en tiempo real
    pygame.mixer.music.set_volume(niveles_volumen["musica"])
    
    # Verificar que juego existe y no es None antes de acceder a sus atributos
    if 'juego' in globals() and juego is not None:
        juego.musica.set_volume(niveles_volumen["musica"])
        juego.sonido_laser.set_volume(niveles_volumen["efectos"])
        juego.sonido_explosion.set_volume(niveles_volumen["efectos"])

def iniciar_cuenta_atras():
    for cuenta in range(3, 0, -1):
        pantalla.fill(GRIS_OSCURO)
        texto_cuenta = fuente_grande.render(str(cuenta), True, BLANCO)
        rect_texto = texto_cuenta.get_rect(center=(ancho_pantalla//2, alto_pantalla//2))
        pantalla.blit(texto_cuenta, rect_texto)
        pygame.display.flip()
        pygame.time.delay(1000)  # Esperar 1 segundo

# Clase personalizada para el modo multijugador
class JugadorMulti(Player):
    def __init__(self, pos, constraint, speed, es_jugador_uno=True):
        super().__init__(pos, constraint, speed)
        self.es_jugador_uno = es_jugador_uno
        # Establecer teclas dependiendo del jugador
        if es_jugador_uno:
            self.tecla_izquierda = pygame.K_LEFT
            self.tecla_derecha = pygame.K_RIGHT
            self.tecla_disparo = pygame.K_SPACE
        else:
            self.tecla_izquierda = pygame.K_a
            self.tecla_derecha = pygame.K_d
            self.tecla_disparo = pygame.K_w
    
    def input_jugador(self):
        keys = pygame.key.get_pressed()
        
        # Movimiento horizontal
        if keys[self.tecla_izquierda]:
            self.rect.x -= self.speed
        elif keys[self.tecla_derecha]:
            self.rect.x += self.speed
            
        # Disparo
        if keys[self.tecla_disparo] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
    
    def update(self):
        self.input_jugador()
        self.constraint()
        self.recharge()
        self.lasers.update()

class Juego:
    def __init__(self, modo="individual"):
        # Modo de juego (individual o multi)
        self.modo = modo
        self.game_over_active = False
        self.victoria_active = False
        
        # Configuración del jugador
        if modo == "individual":
            jugador_sprite = Player((ancho_pantalla / 2, alto_pantalla - 10), ancho_pantalla, 5)
            self.jugador = pygame.sprite.GroupSingle(jugador_sprite)
            self.jugador2 = None
        else:  # modo == "multi"
            # Usar la clase personalizada para multijugador
            jugador1_sprite = JugadorMulti((ancho_pantalla / 3, alto_pantalla - 10), ancho_pantalla, 5, True)
            self.jugador = pygame.sprite.GroupSingle(jugador1_sprite)
            
            jugador2_sprite = JugadorMulti((ancho_pantalla * 2/3, alto_pantalla - 10), ancho_pantalla, 5, False)
            self.jugador2 = pygame.sprite.GroupSingle(jugador2_sprite)

        # Configuración de vidas y puntuación
        self.vidas = 3
        self.superficie_vida = pygame.image.load(get_resource_path('graphics/player.png')).convert_alpha()
        self.pos_x_inicial_vida = ancho_pantalla - (self.superficie_vida.get_size()[0] * 2 + 20)
        self.puntuacion = 0
        self.puntuacion_maxima = cargar_puntuacion_maxima()
        self.fuente = pygame.font.Font(get_resource_path('font/Pixeled.ttf'), 20)

        # Configuración de obstáculos
        self.forma = obstacle.shape
        self.tamaño_bloque = 6
        self.bloques = pygame.sprite.Group()
        self.cantidad_obstaculos = 4
        self.posiciones_x_obstaculos = [num * (ancho_pantalla / self.cantidad_obstaculos) for num in range(self.cantidad_obstaculos)]
        self.crear_multiples_obstaculos(*self.posiciones_x_obstaculos, x_inicio=ancho_pantalla / 15, y_inicio=alto_pantalla - 120)

        # Configuración de aliens
        self.aliens = pygame.sprite.Group()
        self.lasers_aliens = pygame.sprite.Group()
        self.configurar_aliens(filas=6, cols=8)
        self.direccion_alien = 1

        # Configuración de extras
        self.extra = pygame.sprite.GroupSingle()
        self.tiempo_aparicion_extra = randint(40, 80)

        # Audio
        pygame.mixer.init()  # Inicializar el sistema de audio
        self.musica = pygame.mixer.Sound(get_resource_path('audio/music.wav'))
        self.sonido_laser = pygame.mixer.Sound(get_resource_path('audio/laser.wav'))
        self.sonido_explosion = pygame.mixer.Sound(get_resource_path('audio/explosion.wav'))
        
        # Aplicar volúmenes iniciales
        self.musica.set_volume(niveles_volumen["musica"])
        self.sonido_laser.set_volume(niveles_volumen["efectos"])
        self.sonido_explosion.set_volume(niveles_volumen["efectos"])
        self.musica.play(loops=-1)

    def crear_obstaculo(self, x_inicio, y_inicio, offset_x):
        for indice_fila, fila in enumerate(self.forma):
            for indice_col, col in enumerate(fila):
                if col == 'x':
                    x = x_inicio + indice_col * self.tamaño_bloque + offset_x
                    y = y_inicio + indice_fila * self.tamaño_bloque
                    bloque = obstacle.Block(self.tamaño_bloque, ROJO, x, y)
                    self.bloques.add(bloque)

    def crear_multiples_obstaculos(self, *offset, x_inicio, y_inicio):
        for offset_x in offset:
            self.crear_obstaculo(x_inicio, y_inicio, offset_x)

    def configurar_aliens(self, filas, cols, distancia_x=60, distancia_y=48, offset_x=70, offset_y=100):
        # Ajustar la posición horizontal en función del ancho de la pantalla
        offset_x = (ancho_pantalla - (cols * distancia_x)) // 2
        
        for indice_fila, fila in enumerate(range(filas)):
            for indice_col, col in enumerate(range(cols)):
                x = indice_col * distancia_x + offset_x
                y = indice_fila * distancia_y + offset_y
                
                if indice_fila == 0: sprite_alien = Alien('yellow', x, y)
                elif 1 <= indice_fila <= 2: sprite_alien = Alien('green', x, y)
                else: sprite_alien = Alien('red', x, y)
                self.aliens.add(sprite_alien)

    def verificar_posicion_aliens(self):
        todos_aliens = self.aliens.sprites()
        for alien in todos_aliens:
            if alien.rect.right >= ancho_pantalla:
                self.direccion_alien = -1
                self.mover_aliens_abajo(2)
            elif alien.rect.left <= 0:
                self.direccion_alien = 1
                self.mover_aliens_abajo(2)

    def mover_aliens_abajo(self, distancia):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distancia

    def disparo_alien(self):
        if self.aliens.sprites():
            # Encontrar aliens en la fila inferior
            aliens_por_columna = {}
            for alien in self.aliens:
                col = alien.rect.centerx
                if col not in aliens_por_columna or alien.rect.bottom > aliens_por_columna[col].rect.bottom:
                    aliens_por_columna[col] = alien
            
            # Disparar desde un alien aleatorio de la fila inferior
            if aliens_por_columna:
                alien_disparador = choice(list(aliens_por_columna.values()))
                laser_sprite = Laser(alien_disparador.rect.center, 6, alto_pantalla)
                self.lasers_aliens.add(laser_sprite)
                self.sonido_laser.play()

    def temporizador_alien_extra(self):
        self.tiempo_aparicion_extra -= 1
        if self.tiempo_aparicion_extra <= 0:
            self.extra.add(Extra(choice(['right', 'left']), ancho_pantalla))
            self.tiempo_aparicion_extra = randint(400, 800)

    def verificar_colisiones_laser_jugador(self, sprite_jugador):
        if sprite_jugador.lasers:
            for laser in sprite_jugador.lasers:
                # Colisiones con obstáculos
                if pygame.sprite.spritecollide(laser, self.bloques, True):
                    laser.kill()
                
                # Colisiones con aliens
                aliens_golpeados = pygame.sprite.spritecollide(laser, self.aliens, True)
                if aliens_golpeados:
                    for alien in aliens_golpeados:
                        self.puntuacion += alien.value
                    laser.kill()
                    self.sonido_explosion.play()
                
                # Colisión con extra
                if pygame.sprite.spritecollide(laser, self.extra, True):
                    self.puntuacion += 500
                    laser.kill()

    def verificar_colisiones(self):
        # Láseres del jugador 1
        self.verificar_colisiones_laser_jugador(self.jugador.sprite)
        
        # Láseres del jugador 2 (si existe)
        if self.jugador2:
            self.verificar_colisiones_laser_jugador(self.jugador2.sprite)

        # Láseres de aliens
        if self.lasers_aliens:
            for laser in self.lasers_aliens:
                # Colisiones con obstáculos
                if pygame.sprite.spritecollide(laser, self.bloques, True):
                    laser.kill()

                # Colisión con jugador 1
                if pygame.sprite.spritecollide(laser, self.jugador, False):
                    laser.kill()
                    self.vidas -= 1
                    if self.vidas <= 0:
                        self.game_over_active = True
                        # Detener la música cuando el jugador pierde
                        self.musica.stop()
                
                # Colisión con jugador 2 (si existe)
                if self.jugador2 and pygame.sprite.spritecollide(laser, self.jugador2, False):
                    laser.kill()
                    self.vidas -= 1
                    if self.vidas <= 0:
                        self.game_over_active = True
                        # Detener la música cuando el jugador pierde
                        self.musica.stop()

        # Colisión de aliens con la parte inferior de la pantalla
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= alto_pantalla - 50:
                self.game_over_active = True
                # Detener la música cuando los aliens llegan abajo
                self.musica.stop()
                break

        # Aliens
        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.bloques, True)

                # Colisión con jugador 1
                if pygame.sprite.spritecollide(alien, self.jugador, False):
                    self.game_over_active = True
                    # Detener la música cuando hay colisión con alien
                    self.musica.stop()
                
                # Colisión con jugador 2 (si existe)
                if self.jugador2 and pygame.sprite.spritecollide(alien, self.jugador2, False):
                    self.game_over_active = True
                    # Detener la música cuando hay colisión con alien
                    self.musica.stop()
    
    def detener_todos_sonidos(self):
        # Detener todos los sonidos del juego
        self.musica.stop()
        self.sonido_laser.stop()
        self.sonido_explosion.stop()
        # Limpiar grupos de sprites para evitar disparos posteriores
        self.lasers_aliens.empty()
        if self.jugador:
            self.jugador.sprite.lasers.empty()
        if self.jugador2:
            self.jugador2.sprite.lasers.empty()

    def mostrar_game_over(self, pantalla):
        self.detener_todos_sonidos()
        if self.puntuacion > self.puntuacion_maxima:
            # Pedir nombre minimalista
            nombre = "Jugador"
            input_box = pygame.Rect((ancho_pantalla-300)//2, alto_pantalla//2+60, 300, 48)
            activo = True
            texto_nombre = ""
            while activo:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_RETURN:
                            if texto_nombre.strip():
                                nombre = texto_nombre.strip()
                                activo = False
                        elif evento.key == pygame.K_BACKSPACE:
                            texto_nombre = texto_nombre[:-1]
                        elif len(texto_nombre) < 12 and evento.unicode.isprintable():
                            texto_nombre += evento.unicode
                pantalla.fill(GRIS_OSCURO)
                s = pygame.Surface((ancho_pantalla, alto_pantalla), pygame.SRCALPHA)
                s.set_alpha(180)
                s.fill((0, 0, 0))
                pantalla.blit(s, (0, 0))
                texto_game_over = fuente_grande.render('GAME OVER', True, ROJO)
                rect_game_over = texto_game_over.get_rect(center=(ancho_pantalla//2, alto_pantalla//2 - 50))
                pantalla.blit(texto_game_over, rect_game_over)
                texto_puntuacion = fuente.render(f'Puntuacion: {self.puntuacion}', True, BLANCO)
                rect_puntuacion = texto_puntuacion.get_rect(center=(ancho_pantalla//2, alto_pantalla//2))
                pantalla.blit(texto_puntuacion, rect_puntuacion)
                # Input box
                pygame.draw.rect(pantalla, (40,40,40,220), input_box, border_radius=12)
                pygame.draw.rect(pantalla, (255,255,255,80), input_box, 2, border_radius=12)
                texto_input = fuente.render(texto_nombre or "Ingresa tu nombre...", True, BLANCO)
                pantalla.blit(texto_input, (input_box.x+12, input_box.y+12))
                pygame.display.flip()
            guardar_puntuacion_maxima(self.puntuacion, nombre)
            self.puntuacion_maxima = self.puntuacion
        else:
            guardar_puntuacion_maxima(self.puntuacion)
        # ...existing code...

    def mostrar_victoria(self, pantalla):
        if not self.aliens.sprites():
            self.detener_todos_sonidos()
            if not self.victoria_active:
                self.victoria_active = True
            if self.puntuacion > self.puntuacion_maxima:
                # Pedir nombre minimalista
                nombre = "Jugador"
                input_box = pygame.Rect((ancho_pantalla-300)//2, alto_pantalla//2+60, 300, 48)
                activo = True
                texto_nombre = ""
                while activo:
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif evento.type == pygame.KEYDOWN:
                            if evento.key == pygame.K_RETURN:
                                if texto_nombre.strip():
                                    nombre = texto_nombre.strip()
                                    activo = False
                            elif evento.key == pygame.K_BACKSPACE:
                                texto_nombre = texto_nombre[:-1]
                            elif len(texto_nombre) < 12 and evento.unicode.isprintable():
                                texto_nombre += evento.unicode
                    pantalla.fill(GRIS_OSCURO)
                    s = pygame.Surface((ancho_pantalla, alto_pantalla), pygame.SRCALPHA)
                    s.set_alpha(180)
                    s.fill((0, 0, 0))
                    pantalla.blit(s, (0, 0))
                    texto_victoria = fuente_grande.render('HAS GANADO!', True, VERDE)
                    rect_victoria = texto_victoria.get_rect(center=(ancho_pantalla//2, alto_pantalla//2 - 50))
                    pantalla.blit(texto_victoria, rect_victoria)
                    texto_puntuacion = fuente.render(f'Puntuacion: {self.puntuacion}', True, BLANCO)
                    rect_puntuacion = texto_puntuacion.get_rect(center=(ancho_pantalla//2, alto_pantalla//2))
                    pantalla.blit(texto_puntuacion, rect_puntuacion)
                    pygame.draw.rect(pantalla, (40,40,40,220), input_box, border_radius=12)
                    pygame.draw.rect(pantalla, (255,255,255,80), input_box, 2, border_radius=12)
                    texto_input = fuente.render(texto_nombre or "Ingresa tu nombre...", True, BLANCO)
                    pantalla.blit(texto_input, (input_box.x+12, input_box.y+12))
                    pygame.display.flip()
                guardar_puntuacion_maxima(self.puntuacion, nombre)
                self.puntuacion_maxima = self.puntuacion
            else:
                guardar_puntuacion_maxima(self.puntuacion)
            
            # Crear un rectangulo semitransparente para oscurecer el fondo
            s = pygame.Surface((ancho_pantalla, alto_pantalla))
            s.set_alpha(180)
            s.fill((0, 0, 0))
            pantalla.blit(s, (0, 0))
            
            # Mostrar texto de victoria
            texto_victoria = fuente_grande.render('HAS GANADO!', True, VERDE)
            rect_victoria = texto_victoria.get_rect(center=(ancho_pantalla//2, alto_pantalla//2 - 50))
            pantalla.blit(texto_victoria, rect_victoria)
            
            # Mostrar puntuacion final
            texto_puntuacion = fuente.render(f'Puntuacion: {self.puntuacion}', True, BLANCO)
            rect_puntuacion = texto_puntuacion.get_rect(center=(ancho_pantalla//2, alto_pantalla//2))
            pantalla.blit(texto_puntuacion, rect_puntuacion)
            
            # Mostrar mensaje si se batio record
            if self.puntuacion >= self.puntuacion_maxima:
                texto_record = fuente.render('Nueva puntuacion maxima!', True, VERDE)
                rect_record = texto_record.get_rect(center=(ancho_pantalla//2, alto_pantalla//2 + 40))
                pantalla.blit(texto_record, rect_record)
            
            # Boton para volver al menu
            boton_menu = Boton("Volver al Menu", 250, 50, ((ancho_pantalla - 250)//2, alto_pantalla//2 + 100), fuente)
            boton_menu.dibujar(pantalla)
            
            # Verificar clic en boton
            pos_raton = pygame.mouse.get_pos()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Solo clic izquierdo
                    if boton_menu.rect.collidepoint(pos_raton):
                        return True
        
        return False

    def mostrar_vidas(self):
        for vida in range(self.vidas - 1):
            x = self.pos_x_inicial_vida + (vida * (self.superficie_vida.get_size()[0] + 10))
            pantalla.blit(self.superficie_vida, (x, 8))

    def mostrar_puntuacion(self):
        superficie_puntuacion = self.fuente.render(f'Puntos: {self.puntuacion}', False, 'white')
        rect_puntuacion = superficie_puntuacion.get_rect(topleft=(10, 8))
        pantalla.blit(superficie_puntuacion, rect_puntuacion)
        
        # Mostrar puntuacion maxima
        superficie_max = self.fuente.render(f'Max: {self.puntuacion_maxima}', False, 'white')
        rect_max = superficie_max.get_rect(midtop=(ancho_pantalla // 2, 8))
        pantalla.blit(superficie_max, rect_max)

    def ejecutar(self):
        if self.game_over_active:
            return self.mostrar_game_over(pantalla)
        
        if not self.aliens.sprites() and not self.victoria_active:
            self.victoria_active = True
            
        if self.victoria_active:
            return self.mostrar_victoria(pantalla)
        
        # Juego normal
        # Actualizar jugador 1
        self.jugador.update()
        
        # Actualizar jugador 2 (si existe)
        if self.jugador2:
            self.jugador2.update()
        
        self.lasers_aliens.update()
        self.extra.update()
        
        self.aliens.update(self.direccion_alien)
        self.verificar_posicion_aliens()
        self.temporizador_alien_extra()
        self.verificar_colisiones()
        
        # Dibujar jugador 1 y sus láseres
        self.jugador.sprite.lasers.draw(pantalla)
        self.jugador.draw(pantalla)
        
        # Dibujar jugador 2 y sus láseres (si existe)
        if self.jugador2:
            self.jugador2.sprite.lasers.draw(pantalla)
            self.jugador2.draw(pantalla)
        
        self.bloques.draw(pantalla)
        self.aliens.draw(pantalla)
        self.lasers_aliens.draw(pantalla)
        self.extra.draw(pantalla)
        self.mostrar_vidas()
        self.mostrar_puntuacion()
        
        # Verificar victoria
        if not self.aliens.sprites() and not self.victoria_active:
            self.victoria_active = True
        
        # Devolver True si el juego ha terminado y debemos volver al menú
        return False

def mostrar_ranking():
    pantalla.fill(GRIS_OSCURO)
    overlay = pygame.Surface((ancho_pantalla, alto_pantalla), pygame.SRCALPHA)
    overlay.fill((20, 20, 20, 210))
    pantalla.blit(overlay, (0, 0))
    titulo = fuente_grande.render("RANKING", True, BLANCO)
    rect_titulo = titulo.get_rect(center=(ancho_pantalla//2, 80))
    pantalla.blit(titulo, rect_titulo)
    # Leer top 5 del archivo de puntuaciones
    archivo_puntuacion = get_resource_path('highscore.json')
    ranking = []
    if os.path.exists(archivo_puntuacion):
        try:
            with open(archivo_puntuacion, 'r') as archivo:
                datos = json.load(archivo)
                if isinstance(datos, dict) and 'ranking' in datos:
                    ranking = datos['ranking']
                elif 'puntuacion_maxima' in datos:
                    ranking = [("Jugador", datos['puntuacion_maxima'])]
        except:
            ranking = []
    fuente_rank = pygame.font.Font(get_resource_path('font/Pixeled.ttf'), 20)
    y_base = 140
    for i, entry in enumerate(ranking[:5]):
        nombre = entry[0] if isinstance(entry, (list, tuple)) else "Jugador"
        punt = entry[1] if isinstance(entry, (list, tuple)) else entry
        texto = fuente_rank.render(f"{i+1}. {nombre} - {punt}", True, VERDE if i==0 else BLANCO)
        rect = texto.get_rect(center=(ancho_pantalla//2, y_base + i*48))
        pantalla.blit(texto, rect)
    if not ranking:
        texto = fuente_rank.render("No hay puntuaciones aún.", True, BLANCO)
        rect = texto.get_rect(center=(ancho_pantalla//2, y_base + 24))
        pantalla.blit(texto, rect)
    boton_volver = Boton("Volver", 200, 48, ((ancho_pantalla - 200)//2, alto_pantalla - 100), fuente_grande)
    boton_volver.dibujar(pantalla)
    pos_raton = pygame.mouse.get_pos()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver.rect.collidepoint(pos_raton):
                return {"accion": "menu"}
    return {"accion": "ranking"}

def mostrar_creditos():
    pantalla.fill(GRIS_OSCURO)
    overlay = pygame.Surface((ancho_pantalla, alto_pantalla), pygame.SRCALPHA)
    overlay.fill((20, 20, 20, 210))
    pantalla.blit(overlay, (0, 0))
    titulo = fuente_grande.render("CRÉDITOS", True, BLANCO)
    rect_titulo = titulo.get_rect(center=(ancho_pantalla//2, 90))
    pantalla.blit(titulo, rect_titulo)
    fuente_cred = pygame.font.Font(get_resource_path('font/Pixeled.ttf'), 18)
    creditos = [
        "Space Invaders (2025)",
        "Desarrollador: Tu Nombre",
        "Gráficos: OpenGameArt, Pixeled Font",
        "Sonidos: freesound.org",
        "Inspirado en SHADCN UI"
    ]
    for i, linea in enumerate(creditos):
        texto = fuente_cred.render(linea, True, BLANCO)
        rect = texto.get_rect(center=(ancho_pantalla//2, 170 + i*38))
        pantalla.blit(texto, rect)
    boton_volver = Boton("Volver", 200, 48, ((ancho_pantalla - 200)//2, alto_pantalla - 100), fuente_grande)
    boton_volver.dibujar(pantalla)
    pos_raton = pygame.mouse.get_pos()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver.rect.collidepoint(pos_raton):
                return {"accion": "menu"}
    return {"accion": "creditos"}

if __name__ == '__main__':
    pygame.init()
    ancho_pantalla = 800
    alto_pantalla = 700
    pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
    pygame.display.set_caption("Space Invaders")
    reloj = pygame.time.Clock()
    fuente = pygame.font.Font(get_resource_path('font/Pixeled.ttf'), 18)
    fuente_grande = pygame.font.Font(get_resource_path('font/Pixeled.ttf'), 36)
    puntuacion_maxima = cargar_puntuacion_maxima()
    estado_juego = {"accion": "menu", "modo": "individual"}
    juego = None
    DISPARO_ALIEN = pygame.USEREVENT + 1
    pygame.time.set_timer(DISPARO_ALIEN, 800)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == DISPARO_ALIEN and estado_juego["accion"] == "jugar" and juego:
                juego.disparo_alien()
        if estado_juego["accion"] == "menu":
            estado_juego = mostrar_menu()
            if estado_juego["accion"] == "jugar":
                juego = Juego(modo=estado_juego["modo"])
        elif estado_juego["accion"] == "opciones":
            estado_juego = mostrar_opciones()
        elif estado_juego["accion"] == "ranking":
            estado_juego = mostrar_ranking()
        elif estado_juego["accion"] == "creditos":
            estado_juego = mostrar_creditos()
        elif estado_juego["accion"] == "jugar":
            pantalla.fill(GRIS_OSCURO)
            if juego.ejecutar():
                juego.musica.stop()
                estado_juego = {"accion": "menu"}
        pygame.display.flip()
        reloj.tick(60)