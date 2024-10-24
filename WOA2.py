'''
Se importan las librerias de sys y time para que funcionen con text_speed
'''
import random, os, sys, time
from personajes import *
from clanes import *

from colorama import Fore
'''LOS FUNDADORES TENDRAN COLOR AZUL
LOS MAGOS TENDRAN UN COLOR VERDE
LOS GUERRREROS TENDRAN COLOR ROJO
LOS ARQUEROS TENDRAN UN COLOR CYAN'''

#--INICIO FUNCIONES--

'''Función para mostrar el texto de manera incremental.
text: Es el texto a mostrar
velocity: La velocidad en la que se va mostrar (por defecto es de 0.05)
'''
def text_speed(text, velocity = 0.05):
    for ca in text:
        sys.stdout.write(ca)
        sys.stdout.flush()
        time.sleep(velocity)
    print()

def crearGuerrero(titulo):
    nombre = input(f"Name of the {Fore.RED} {titulo} {Style.RESET_ALL}: ").upper()
    guerrero = Guerrero(nombre)
    guerreros.append(guerrero)
    return guerrero

def crearMago(titulo):
    nombre = input(f"Name of the {Fore.GREEN} {titulo} {Style.RESET_ALL}: ").upper()
    mago = Mago(nombre)
    magos.append(mago)
    return mago

def crearArquero(titulo):
    nombre = input(f"Name of the {Fore.CYAN} {titulo} {Style.RESET_ALL}: ").upper()
    arquero = Arquero(nombre)
    arqueros.append(arquero)
    return arquero

def crearFundador(mago):
    text_speed("Your destiny is to be a founder in these wastelands of Pythonias...")
    fundador = Fundador(mago.nombre)
    fundadores.append(fundador)
    magos.remove(mago)
    return fundador

def crearClan(fundador):
    nombreClan = input("clan's name: ").upper()
    clan = Clan(nombreClan, fundador)
    clanes.append(clan)
    fundador.asignar_clan(nombreClan)

def seleccionarClan(personaje):
    asignado = False
    while not asignado:
        for index, clan in enumerate(clanes):
            text_speed(f"{index+1} : {clan.nombre}")
        print()
        nombreClan = input("Enter the name of the clan -> ").upper()
        for clan in clanes:
            if clan.nombre == nombreClan:
                personaje.asignar_clan(nombreClan)
                clan.agregar_miembro(personaje)
                input(f"{personaje.nombre} has been added to the clan {clan.nombre} <ENTER TO CONTINUE>")
                asignado = True
        if asignado == False:
            text_speed(f"The clan {nombreClan} does not exist...")
            print()


def seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros):
    text_speed("-- Selection mode --", 0)
    text_speed("-- Select your goal --", 0)
    text_speed("1. By clan.", 0)
    text_speed("2. List all characters.", 0)
    text_speed("3. Attack by title.", 0)
    opcion = int(input("Choose an option: "))
    
    if opcion == 1:
        text_speed("clan list")
        for index, clan in enumerate(clanes):
            print(f"{index+1} {clan.nombre}")
        indexClan = int(input("Select clan number: ")) - 1
        if 0 <= indexClan < len(clanes):# es igual que indexClan >= 0 or indexClan < len(clanes)
            clan = clanes[indexClan]
            text_speed(f"clan's members {clan.nombre}")
            clan.listar_miembros()
            nombreObjetivo = input("Enter the name of your target : ").upper()
            for miembro in clan.miembros:
                if nombreObjetivo == miembro.nombre:
                    return miembro
            return None
        else:
            print("Invalid clan")

    if opcion == 2:
        listaPersonajes = fundadores + magos + guerreros + arqueros
        text_speed("list of all characters")
        for miembro in listaPersonajes:
            print(miembro)
            print()
        nombreObjetivo = input("Enter the name of your target: ").upper()
        for miembro in listaPersonajes:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    if opcion == 3:
        text_speed("Title to list", 0)
        text_speed( Fore.BLUE + "1. Founders", 0)
        text_speed( Fore.GREEN + "2. Sorcerers", 0)
        text_speed(Fore.RED + "3. warriors", 0)
        text_speed(Fore.CYAN + "4. Archers", 0)
        tipo = int(input("Enter your option: "))
        if tipo == 1:
            listaObjetivos = fundadores
        elif tipo == 2:
            listaObjetivos = magos
        elif tipo == 3:
            listaObjetivos = guerreros
        elif tipo == 4:
            listaObjetivos = arqueros
        text_speed("Characters:")
        for personaje in listaObjetivos:
            print(personaje)
        nombreObjetivo = input("Enter the name of your target: ").upper()
        for miembro in listaObjetivos:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    text_speed("Invalid option")
    return None


def organizarTurno(lst_pjs):
    input("The characters' turn will be selected at random\n<ENTER TO CONTINUE>")
    limpiar_consola()
    turnos_ordenados = lst_pjs[:]
    random.shuffle(turnos_ordenados)
    
    text_speed("This will be the order of turns per player: ")
    for index, pj in enumerate(turnos_ordenados):
        text_speed(f"{index+1} | Title: {pj.titulo} | Name: {pj.nombre}")
    return turnos_ordenados

#--FIN FUNCIONES--

#--INICIO PROCEDIMIENTOS--

def listarTodoElStaff():
    global lista_personajes
    #Agregar a lista_personajes todos las clases según se vayan creando
    lista_personajes = fundadores + magos + guerreros + arqueros
    text_speed("List of all the characters present in the game: ")
    text_speed("--***---***--***---***--***---***", 0)
    for pj in lista_personajes:
        text_speed(pj.nombre)
    text_speed("--***---***--***---***--***---***", 0)
    print()

def limpiar_consola():
    os.system("cls") if os.name == "nt" else os.system("clear")

#--FIN PROCEDIMIENTOS--

#--INICIO ARREGLOS--

guerreros = []
magos = []
arqueros = []
fundadores = []
clanes = []

lista_personajes = fundadores + magos + guerreros + arqueros

#--FIN ARREGLOS

#INICIO CÓDIGO PRINCIPAL

if __name__=="__main__":

    cantidadJugadores = int(input("Number of players: "))
    limpiar_consola()
    for i in range(cantidadJugadores):
        if i == 0:
            mago = crearMago("Founder")
            fundador = crearFundador(mago)
            crearClan(fundador)
            limpiar_consola()
        else:
            print()
            text_speed(f"Choosing the player class {i+1}/{cantidadJugadores}: ")
            
            opcionPersonaje = int(input("1.Warrior\n2.Sorcerers\n3.Archer\nOption: "))
            if opcionPersonaje == 1:
                guerrero = crearGuerrero("warrior")
                seleccionarClan(guerrero)
                limpiar_consola()
            elif opcionPersonaje == 2:
                mago = crearMago("Sorcerer")
                opcionCrearClan = int(input("Do you want to create your own clan?\n1.YES\n2.NO\nOption: "))
                if opcionCrearClan == 1:
                    fundador = crearFundador(mago)
                    crearClan(fundador)
                    limpiar_consola()
                else:
                    seleccionarClan(mago)
            elif opcionPersonaje == 3:
                arquero = crearArquero("Archer")
                seleccionarClan(arquero)
                limpiar_consola()


    listarTodoElStaff()

    turnos_ordenados = organizarTurno(lista_personajes)

    limpiar_consola()

    cont_turnos = 0

    for pj in turnos_ordenados:
        cont_turnos += 1
        limpiar_consola()
        text_speed(f"*** Turn: {cont_turnos} ***")
        text_speed(f"It's the turn of {pj.titulo} | {pj.nombre}")
        objetivo = seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros)
        print()
        text_speed("-- Choose an option --")
        if pj.titulo == "Founder":
            text_speed("1. Attack.")
            text_speed("2. Create potions.")
            opc = int(input("Option: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
            if opc == 2:
                pj.crear_pociones()
                pj.conceder_curacion(lista_personajes, objetivo)
        elif pj.titulo == "Warrior":
            print()
            text_speed("1. Attack.")
            text_speed("2. Defend. (NO IMPLEMENTADO)")
            text_speed("3. sword dance. (NO IMPLEMENTADO)")
            opc = int(input("Option: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
                print()
        elif pj.titulo == "Sorcerer":
            text_speed("1. Attack.")
            text_speed("2. cure. (NO IMPLEMENTADO)")
            text_speed("3. Meteorite storm ☄")
            opc = int(input("Option: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
        elif pj.titulo == "Arquero":
            print()
            text_speed("1. Attack.")
            text_speed("2. Accurate arrow. (NOT IMPLEMENTED)")
            text_speed("3. arrow storm. (NO IMPLEMENTADO)")
            opc = int(input("Option: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
        print(objetivo)