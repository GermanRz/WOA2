'''
Archivo para recursos generales de WOA2
'''
import sys, time, pygame
import colorama
from colorama import Style

#INICIAR LOS EFECTOS DE SONIDO Y LA MÚSICA
pygame.mixer.init() # Inicia la música

# * INICIAR EL COLORAMA *
colorama.init() # Esto es necesario para iniciar la clase colorama

'''Función para mostrar el texto de manera incremental.
text: Es el texto a mostrar
velocity: La velocidad en la que se va mostrar (por defecto es de 0.05)
'''
def text_speed(text, velocity = 0):
    for ca in text:
        sys.stdout.write(ca)
        sys.stdout.flush()
        time.sleep(velocity)
    print()

'''
Función para implementar música en el juego
NOTA: Se debe de instalar pygame ((ctrl + ñ) y seguidamente ejecutar el comando pip install pygame)
'''
# Soundtracks
def reproducir_musica(audio, time = 1500):
    pygame.mixer.init() # Inicia la música
    
    diccionario_audios = {
        1: "Audios/Messmer, The Impaler.mp3",
        2: "Audios/Knight Gael Phase 2.mp3"
    }
    
    match audio:
        case "Messmer":
            ruta_audio = diccionario_audios[1]
            pygame.mixer.music.fadeout(time)
            pygame.mixer.music.load(ruta_audio)
            pygame.mixer.music.play()
        case "Gael":
            ruta_audio = diccionario_audios[2]
            pygame.mixer.music.fadeout(time)
            pygame.mixer.music.load(ruta_audio)
            pygame.mixer.music.play()
            
            
# Visualizaciones
def imprimirTodosPersonajes(personajes, num_columnas=3, ancho_columna=55):
    """
    Imprime personajes en columnas, con la información de cada personaje en múltiples líneas.
    
    Args:
        personajes: Lista de personajes
        num_columnas: Número de columnas a mostrar
        ancho_columna: Ancho de cada columna en caracteres
    """
    num_personajes = len(personajes)
    
    # Procesar los personajes por grupos
    for fila_inicio in range(0, num_personajes, num_columnas):
        # Obtener el grupo de personajes para esta fila
        grupo_actual = personajes[fila_inicio:fila_inicio + num_columnas]
                
        # Primera línea: Título y nombre
        for personaje in grupo_actual:
            print(f"{personaje.color}{personaje.titulo}: {personaje.nombre}{Style.RESET_ALL}".ljust(ancho_columna), end="")
        print()
        
        # Segunda línea: Fuerza y puntos de vida
        for personaje in grupo_actual:
            print(f"{personaje.color}Strength: {personaje.fuerza}, Life Points: {personaje.puntos_vida},{Style.RESET_ALL}".ljust(ancho_columna), end="")
        print()
        
        # Tercera línea: Defensa, ataque y clan
        for personaje in grupo_actual:
            print(f"{personaje.color}Defense: {personaje.defensa}, Attack: {personaje.ataque}, Clan: {personaje.clan}{Style.RESET_ALL}".ljust(ancho_columna), end="")
        print()
        
        # Cuarta línea: Maná
        # for personaje in grupo_actual:
        #     print(f"Defense: {personaje.mana}".ljust(ancho_columna), end="")
        # print()       
        
        # Línea en blanco entre grupos de personajes y reseteo de color
        print(f"{Style.RESET_ALL}")

