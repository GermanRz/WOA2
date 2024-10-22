'''
Archivo para recursos generales de WOA2
'''
import sys, time

def text_speed(text, velocity = 0.05):
    for ca in text:
        sys.stdout.write(ca)
        sys.stdout.flush()
        time.sleep(velocity)
    print()