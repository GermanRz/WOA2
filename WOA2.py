'''
Se importan las librerias de sys y time para que funcionen con text_speed
'''
import random, os, sys, time
from personajes import *
from clanes import *

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
    nombre = input(f"¿{titulo}'s name? -> ").upper()
    guerrero = Guerrero(nombre)
    guerreros.append(guerrero)
    return guerrero

def crearMago(titulo):
    nombre = input(f"¿{titulo}'s name? -> ").upper()
    mago = Mago(nombre)
    magos.append(mago)
    return mago

def crearArquero(titulo):
    nombre = input(f"¿{titulo}'s name? -> ").upper()
    arquero = Arquero(nombre)
    arqueros.append(arquero)
    return arquero

def crearFundador(mago):
    text_speed("Now you are the founder, within these farlands of ashes...")
    fundador = Fundador(mago.nombre)
    fundadores.append(fundador)
    magos.remove(mago)
    return fundador

def crearClan(fundador):
    nombreClan = input("¡Set clan's name! -> ").upper()
    clan = Clan(nombreClan, fundador)
    clanes.append(clan)
    fundador.asignar_clan(nombreClan)

def seleccionarClan(personaje):
    asignado = False
    while not asignado:
        for index, clan in enumerate(clanes):
            text_speed(f"{index+1} : {clan.nombre}")
        print()
        nombreClan = input("¿Which clan do you want to get in? -> ").upper()
        for clan in clanes:
            if clan.nombre == nombreClan:
                personaje.asignar_clan(nombreClan)
                clan.agregar_miembro(personaje)
                input(f"¡{personaje.nombre} joined the clan {clan.nombre}! <PRESS ENTER TO CONTINUE>")
                asignado = True
        if asignado == False:
            text_speed(f"The clan '{nombreClan}' does not exist...")
            print()


def seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros):
    text_speed("-- Select mode --", 0)
    text_speed("-- Select your objective --", 0)
    text_speed("1. Select by clan.", 0)
    text_speed("2. List all players.", 0)
    text_speed("3. Attack by title.", 0)
    opcion = int(input("Choose an option: "))
    
    if opcion == 1:
        text_speed("CLAN'S LIST")
        for index, clan in enumerate(clanes):
            print(f"{index+1} {clan.nombre}")
        indexClan = int(input("Select by clan's number: ")) - 1
        if 0 <= indexClan < len(clanes):# es igual que indexClan >= 0 or indexClan < len(clanes)
            clan = clanes[indexClan]
            text_speed(f"Members of the clan {clan.nombre}")
            clan.listar_miembros()
            nombreObjetivo = input("¡Write your objective's name! -> ").upper()
            for miembro in clan.miembros:
                if nombreObjetivo == miembro.nombre:
                    return miembro
            return None
        else:
            print("INVALID CLAN")

    if opcion == 2:
        listaPersonajes = fundadores + magos + guerreros + arqueros
        text_speed("PLAYER'S LIST")
        for miembro in listaPersonajes:
            print(miembro)
            print()
        nombreObjetivo = input("¡Write your objetive's name! -> ").upper()
        for miembro in listaPersonajes:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    if opcion == 3:
        text_speed("TITLE'S LIST", 0)
        text_speed("1. Founders", 0)
        text_speed("2. Wizards", 0)
        text_speed("3. warriors", 0)
        text_speed("4. Archers", 0)
        tipo = int(input("SELECT AN OPTION -> "))
        if tipo == 1:
            listaObjetivos = fundadores
        elif tipo == 2:
            listaObjetivos = magos
        elif tipo == 3:
            listaObjetivos = guerreros
        elif tipo == 4:
            listaObjetivos = arqueros
        text_speed("PLAYERS")
        for personaje in listaObjetivos:
            print(personaje)
        nombreObjetivo = input("!Write objective's name! ->").upper()
        for miembro in listaObjetivos:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    text_speed("INVALID OPTION")
    return None


def organizarTurno(lst_pjs):
    input("¡The players turn it's about to get randomly set!\n<PRESS ENTER TO CONTINUE>")
    limpiar_consola()
    turnos_ordenados = lst_pjs[:]
    random.shuffle(turnos_ordenados)
    
    text_speed("¡Players turn already set!")
    for index, pj in enumerate(turnos_ordenados):
        text_speed(f"{index+1} | Player: {pj.nombre}({pj.titulo})")
    return turnos_ordenados

#--FIN FUNCIONES--

#--INICIO PROCEDIMIENTOS--

def listarTodoElStaff():
    global lista_personajes
    #Agregar a lista_personajes todos las clases según se vayan creando
    lista_personajes = fundadores + magos + guerreros + arqueros
    text_speed("Total players list on actual game: ")
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

    cantidadJugadores = int(input("Insert the amount of players: "))
    limpiar_consola()
    for i in range(cantidadJugadores):
        if i == 0:
            mago = crearMago("Founder")
            fundador = crearFundador(mago)
            crearClan(fundador)
            limpiar_consola()
        else:
            print()
            text_speed(f"Selecting player's class {i+1}/{cantidadJugadores}: ")
            
            opcionPersonaje = int(input("1.Warrior\n2.Wizard\n3.Archer\nOption: "))
            if opcionPersonaje == 1:
                guerrero = crearGuerrero("warrior")
                seleccionarClan(guerrero)
                limpiar_consola()
            elif opcionPersonaje == 2:
                mago = crearMago("Wizard")
                opcionCrearClan = int(input("¿Would you like to create a clan?\n1. Yes\n2. No\nOption: "))
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
        text_speed(f"¡It is {pj.nombre}'s ({pj.titulo}) turn!")
        objetivo = seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros)
        print()
        text_speed("-- ¿WHAT DO YOU WANT DO? --")
        if pj.titulo == "Founder":
            text_speed("1. Attack.")
            text_speed("2. Craft potion.")
            opc = int(input("Option: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
            if opc == 2:
                pj.crear_pociones()
                pj.conceder_curacion(lista_personajes, objetivo)
        elif pj.titulo == "Warrior":
            print()
            text_speed("1. Attack.")
            text_speed("2. Defend. (NOT IMPLEMENTED)")
            text_speed("3. Sword dance. (NOT IMPLEMENTED)")
            opc = int(input("Option: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
                print()
        elif pj.titulo == "Sorcerer":
            text_speed("1. Attack.")
            text_speed("2. Heal. (NOT IMPLEMENTED)")
            text_speed("3. Meteorite storm ☄")
            opc = int(input("Option: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
        elif pj.titulo == "Archer":
            print()
            text_speed("1. Attack.")
            text_speed("2. Accurate shot. (NOT IMPLEMENTED)")
            text_speed("3. Arrow storm. (NOT IMPLEMENTED)")
            opc = int(input("Option: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
        print(objetivo)