import random, os
from personajes import *
from clanes import *

#--INICIO FUNCIONES--

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
    print("Tu destino es ser fundador en estas baldías tierras Pythonias...")
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
            print(f"{index+1} : {clan.nombre}")
        print()
        nombreClan = input("Digite el nombre del clan -> ").upper()
        for clan in clanes:
            if clan.nombre == nombreClan:
                personaje.asignar_clan(nombreClan)
                clan.agregar_miembro(personaje)
                input(f"{personaje.nombre} ha sido agregado al clan {clan.nombre} <ENTER PARA CONTINUAR>")
                asignado = True
        if asignado == False:
            print(f"El clan {nombreClan} no existe...")
            print()


def seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros):
    print("-- Modo de selección --")
    print("-- Selecciona tu objetivo --")
    print("1. Por clan.")
    print("2. Listar todos los personajes.")
    print("3. Atacar por titulo.")
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        print("lista de clanes")
        for index, clan in enumerate(clanes):
            print(f"{index+1} {clan.nombre}")
        indexClan = int(input("Selecciona el número del clan: ")) - 1
        if 0 <= indexClan < len(clanes):# es igual que indexClan >= 0 or indexClan < len(clanes)
            clan = clanes[indexClan]
            print(f"Miembros del clan {clan.nombre}")
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
        print("lista de todos los personajes")
        for miembro in listaPersonajes:
            print(miembro)
            print()
        nombreObjetivo = input("Escriba el nombre de su objetivo: ").upper()
        for miembro in listaPersonajes:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    if opcion == 3:
        print("Titulo a listar")
        print("1. Fundadores")
        print("2. Magos")
        print("3. Guerreros")
        print("4. Arqueros")
        tipo = int(input("Digite su opción: "))
        if tipo == 1:
            listaObjetivos = fundadores
        elif tipo == 2:
            listaObjetivos = magos
        elif tipo == 3:
            listaObjetivos = guerreros
        elif tipo == 4:
            listaObjetivos = arqueros
        print("Personajes:")
        for personaje in listaObjetivos:
            print(personaje)
        nombreObjetivo = input("Escriba el nombre de su objetivo: ").upper()
        for miembro in listaObjetivos:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    print("Opción no válida")
    return None


def organizarTurno(lst_pjs):
    input("Se seleccionará al azar el turno de los personajes\n<ENTER PARA CONTINUAR> ")
    limpiar_consola()
    turnos_ordenados = lst_pjs[:]
    random.shuffle(turnos_ordenados)
    
    print("Así será el orden de los turnos por jugador: ")
    for index, pj in enumerate(turnos_ordenados):
        print(f"{index+1} | Titulo: {pj.titulo} | Nombre: {pj.nombre}")
    return turnos_ordenados

#--FIN FUNCIONES--

#--INICIO PROCEDIMIENTOS--

def listarTodoElStaff():
    global lista_personajes
    #Agregar a lista_personajes todos las clases según se vayan creando
    lista_personajes = fundadores + magos + guerreros + arqueros
    print("Lista de todos los peronajes presentes en la partida: ")
    print("--***---***--***---***--***---***")
    for pj in lista_personajes:
        print(pj.nombre)
    print("--***---***--***---***--***---***")
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
            print(f"Eligiendo la clase del jugador {i+1}/{cantidadJugadores}: ")
            
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
        print(f"*** Turno: {cont_turnos} ***")
        print(f"Es el turno de {pj.titulo} | {pj.nombre}")
        objetivo = seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros)
        print("-- Elige una opción --")
        if pj.titulo == "Fundador":
            print("1. Atacar.")
            print("2. Crear pociones. (NO IMPLEMENTADO)")
            print("3. Entregar pociones. (NO IMPLEMENTADO)")
            opc = int(input("Opción: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
        elif pj.titulo == "Guerrero":
            print("1. Atacar.")
            print("2. Defender. (NO IMPLEMENTADO)")
            print("3. Danza espada. (NO IMPLEMENTADO)")
            opc = int(input("Opción: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
        elif pj.titulo == "Mago":
            print("1. Atacar.")
            print("2. Curar. (NO IMPLEMENTADO)")
            print("3. Ataque doble")
            opc = int(input("Opción: "))
            if opc == 1:
                pj.realizar_ataque(objetivo)
        elif pj.titulo == "Arquero":
            print("1. Atacar.")
            print("2. Flechazo certero. (NO IMPLEMENTADO)")
            print("3. arrow storm. (NO IMPLEMENTADO)")
            if opc == 1:
                pj.realizar_ataque(objetivo)
            opc = int(input("Opción: "))
        print(objetivo)