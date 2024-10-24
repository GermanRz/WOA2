'''
Archivo para recursos generales de WOA2
'''
import sys, time

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