'''
Archivo para recursos generales de WOA2
'''
import sys, time, pygame

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
Función para implementar música en el juego y que el juego sea mas chimba 🤟
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