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
    nombre = input(f"Nombre del {titulo}: ").upper()
    guerrero = Guerrero(nombre)
    guerreros.append(guerrero)
    return guerrero

def crearMago(titulo):
    nombre = input(f"Nombre del {titulo}: ").upper()
    mago = Mago(nombre)
    magos.append(mago)
    return mago

def crearArquero(titulo):
    nombre = input(f"Nombre del {titulo}: ").upper()
    arquero = Arquero(nombre)
    arqueros.append(arquero)
    return arquero

def crearFundador(mago):
    text_speed("Tu destino es ser fundador en estas baldías tierras Pythonias...")
    fundador = Fundador(mago.nombre)
    fundadores.append(fundador)
    magos.remove(mago)
    return fundador

def crearClan(fundador):
    nombreClan = input("Nombre del clan: ").upper()
    clan = Clan(nombreClan, fundador)
    clanes.append(clan)
    fundador.asignar_clan(nombreClan)

def seleccionarClan(personaje):
    asignado = False
    while not asignado:
        for index, clan in enumerate(clanes):
            text_speed(f"{index+1} : {clan.nombre}")
        print()
        nombreClan = input("Digite el nombre del clan -> ").upper()
        for clan in clanes:
            if clan.nombre == nombreClan:
                personaje.asignar_clan(nombreClan)
                clan.agregar_miembro(personaje)
                input(f"{personaje.nombre} ha sido agregado al clan {clan.nombre} <ENTER PARA CONTINUAR>")
                asignado = True
        if asignado == False:
            text_speed(f"El clan {nombreClan} no existe...")
            print()


def seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros):
    text_speed("-- Modo de selección --", 0)
    text_speed("-- Selecciona tu objetivo --", 0)
    text_speed("1. Por clan.", 0)
    text_speed("2. Listar todos los personajes.", 0)
    text_speed("3. Atacar por titulo.", 0)
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        text_speed("lista de clanes")
        for index, clan in enumerate(clanes):
            print(f"{index+1} {clan.nombre}")
        indexClan = int(input("Selecciona el número del clan: ")) - 1
        if 0 <= indexClan < len(clanes):# es igual que indexClan >= 0 or indexClan < len(clanes)
            clan = clanes[indexClan]
            text_speed(f"Miembros del clan {clan.nombre}")
            clan.listar_miembros()
            nombreObjetivo = input("Escriba el nombre de su objetivo: ").upper()
            for miembro in clan.miembros:
                if nombreObjetivo == miembro.nombre:
                    return miembro
            return None
        else:
            print("Clan no válido")

    if opcion == 2:
        listaPersonajes = fundadores + magos + guerreros + arqueros
        text_speed("lista de todos los personajes")
        for miembro in listaPersonajes:
            print(miembro)
            print()
        nombreObjetivo = input("Escriba el nombre de su objetivo: ").upper()
        for miembro in listaPersonajes:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    if opcion == 3:
        text_speed("Titulo a listar", 0)
        text_speed("1. Fundadores", 0)
        text_speed("2. Magos", 0)
        text_speed("3. Guerreros", 0)
        text_speed("4. Arqueros", 0)
        tipo = int(input("Digite su opción: "))
        if tipo == 1:
            listaObjetivos = fundadores
        elif tipo == 2:
            listaObjetivos = magos
        elif tipo == 3:
            listaObjetivos = guerreros
        elif tipo == 4:
            listaObjetivos = arqueros
        text_speed("Personajes:")
        for personaje in listaObjetivos:
            print(personaje)
        nombreObjetivo = input("Escriba el nombre de su objetivo: ").upper()
        for miembro in listaObjetivos:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    text_speed("Opción no válida")
    return None


def organizarTurno(lst_pjs):
    input("Se seleccionará al azar el turno de los personajes\n<ENTER PARA CONTINUAR> ")
    limpiar_consola()
    turnos_ordenados = lst_pjs[:]
    random.shuffle(turnos_ordenados)
    
    text_speed("Así será el orden de los turnos por jugador: ")
    for index, pj in enumerate(turnos_ordenados):
        text_speed(f"{index+1} | Titulo: {pj.titulo} | Nombre: {pj.nombre}")
    return turnos_ordenados

#--FIN FUNCIONES--

#--INICIO PROCEDIMIENTOS--

def listarTodoElStaff():
    global lista_personajes
    #Agregar a lista_personajes todos las clases según se vayan creando
    lista_personajes = fundadores + magos + guerreros + arqueros
    text_speed("Lista de todos los peronajes presentes en la partida: ")
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

    cantidadJugadores = int(input("Cantidad de jugadores: "))
    limpiar_consola()
    for i in range(cantidadJugadores):
        if i == 0:
            mago = crearMago("Fundador")
            fundador = crearFundador(mago)
            crearClan(fundador)
            limpiar_consola()
        else:
            print()
            text_speed(f"Eligiendo la clase del jugador {i+1}/{cantidadJugadores}: ")
            
            opcionPersonaje = int(input("1.Guerrero\n2.Mago\n3.Arquero\nOpción: "))
            if opcionPersonaje == 1:
                guerrero = crearGuerrero("Guerrero")
                seleccionarClan(guerrero)
                limpiar_consola()
            elif opcionPersonaje == 2:
                mago = crearMago("Mago")
                opcionCrearClan = int(input("Desea crear su propio clan?\n1. SI\n2. NO\nOpción: "))
                if opcionCrearClan == 1:
                    fundador = crearFundador(mago)
                    crearClan(fundador)
                    limpiar_consola()
                else:
                    seleccionarClan(mago)
            elif opcionPersonaje == 3:
                arquero = crearArquero("Arquero")
                seleccionarClan(arquero)
                limpiar_consola()


    listarTodoElStaff()

    turnos_ordenados = organizarTurno(lista_personajes)

    limpiar_consola()

    cont_turnos = 0

    for pj in turnos_ordenados:
        cont_turnos += 1
        limpiar_consola()
        text_speed(f"*** Turno: {cont_turnos} ***")
        text_speed(f"Es el turno de {pj.titulo} | {pj.nombre}")
        objetivo = seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros)
        print()
        text_speed("-- Elige una opción --")
        if pj.titulo == "Fundador":
            text_speed("1. Atacar.")
            text_speed("2. Crear pociones. (EN DESARROLLO)")
            opc = int(input("Opción: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
            if opc == 2:
                pj.crear_pociones()
                pj.conceder_curacion(lista_personajes, objetivo)
        elif pj.titulo == "Guerrero":
            print()
            text_speed("1. Atacar.")
            text_speed("2. Defender. (NO IMPLEMENTADO)")
            text_speed("3. Danza espada. (NO IMPLEMENTADO)")
            opc = int(input("Opción: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
                print()
        elif pj.titulo == "Mago":
            text_speed("1. Atacar.")
            text_speed("2. Curar. (NO IMPLEMENTADO)")
            text_speed("3. Meteorite storm ☄")
            opc = int(input("Opción: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
        elif pj.titulo == "Arquero":
            print()
            text_speed("1. Atacar.")
            text_speed("2. Flechazo certero. (NO IMPLEMENTADO)")
            text_speed("3. arrow storm. (NO IMPLEMENTADO)")
            opc = int(input("Opción: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
        print(objetivo)