import random, os
from personajes import *
from clanes import *

#--INICIO FUNCIONES--

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
    print("Now you are the founder, within these farlands of ashes...")
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
            print(f"{index+1} : {clan.nombre}")
        print()
        nombreClan = input("¿Which clan do you want to get in? -> ").upper()
        for clan in clanes:
            if clan.nombre == nombreClan:
                personaje.asignar_clan(nombreClan)
                clan.agregar_miembro(personaje)
                input(f"¡{personaje.nombre} joined the clan {clan.nombre}! <PRESS ENTER TO CONTINUE>")
                asignado = True
        if asignado == False:
            print(f"The clan '{nombreClan}' does not exist...")
            print()


def seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros):
    print("-- Select mode --")
    print("-- Select your objective --")
    print("1. Select by clan.")
    print("2. List all players.")
    print("3. Attack by title.")
    opcion = int(input("Select an option: "))
    
    if opcion == 1:
        print("Clan's list")
        for index, clan in enumerate(clanes):
            print(f"{index+1} {clan.nombre}")
        indexClan = int(input("Select by clan's number: ")) - 1
        if 0 <= indexClan < len(clanes):# es igual que indexClan >= 0 or indexClan < len(clanes)
            clan = clanes[indexClan]
            print(f"Members of the clan {clan.nombre}")
            clan.listar_miembros()
            nombreObjetivo = input("¡Write your objective's name! -> ").upper()
            for miembro in clan.miembros:
                if nombreObjetivo == miembro.nombre:
                    return miembro
            return None
        else:
            print("¡INVALID CLAN!")

    if opcion == 2:
        listaPersonajes = fundadores + magos + guerreros + arqueros
        print("PLAYERS LIST")
        for miembro in listaPersonajes:
            print(miembro)
            print()
        nombreObjetivo = input("¡Write your objetive's name! -> ").upper()
        for miembro in listaPersonajes:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    if opcion == 3:
        print("TITLE'S LIST")
        print("1. Founders")
        print("2. Wizards")
        print("3. Warriors")
        print("4. Archers")
        tipo = int(input("SELECT AN OPTION -> "))
        if tipo == 1:
            listaObjetivos = fundadores
        elif tipo == 2:
            listaObjetivos = magos
        elif tipo == 3:
            listaObjetivos = guerreros
        elif tipo == 4:
            listaObjetivos = arqueros
        print("PLAYERS")
        for personaje in listaObjetivos:
            print(personaje)
        nombreObjetivo = input("!Write objective's name! ->").upper()
        for miembro in listaObjetivos:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    print("¡INVALID OPTION!")
    return None


def organizarTurno(lst_pjs):
    input("¡The players turn it's about to get randomly set!\n<PRESS ENTER TO CONTINUE>")
    limpiar_consola()
    turnos_ordenados = lst_pjs[:]
    random.shuffle(turnos_ordenados)
    
    print("¡Players turn already set!")
    for index, pj in enumerate(turnos_ordenados):
        print(f"{index+1} | Title: {pj.titulo} | Name: {pj.nombre}")
    return turnos_ordenados

#--FIN FUNCIONES--

#--INICIO PROCEDIMIENTOS--

def listarTodoElStaff():
    global lista_personajes
    #Agregar a lista_personajes todos las clases según se vayan creando
    lista_personajes = fundadores + magos + guerreros + arqueros
    print("Total players list on actual game: ")
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
        print(f"Selecting player's class {i+1}/{cantidadJugadores}: ")
        
        opcionPersonaje = int(input("1.Warrior\n2.Wizard\n3.Archer\nOption: "))
        if opcionPersonaje == 1:
            guerrero = crearGuerrero("Warrior")
            seleccionarClan(guerrero)
            limpiar_consola()
        elif opcionPersonaje == 2:
            mago = crearMago("Wizard")
            opcionCrearClan = int(input("¿Would you like to create a clan?\n1. Yes\n2. NO\nOption: "))
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
    print(f"*** Turn: {cont_turnos} ***")
    print(f"¡It is {pj.nombre}'s ({pj.titulo}) turn!")
    objetivo = seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros)
    print("-- ¿WHAT DO YOU WANT DO? --")
    if pj.titulo == "Founder":
        print("1. Attack.")
        print("2. Craft potion. (NOT IMPLEMENTED)")
        print("3. Give potion(s). (NOT IMPLEMENTED)")
        opc = int(input("Option: "))
        if opc == 1:
            pj.realizar_ataque(objetivo)
    elif pj.titulo == "Warrior":
        print("1. Attack.")
        print("2. Defend. (NOT IMPLEMENTED)")
        print("3. Sword Dance (.__.). (NOT IMPLEMENTED)")
        opc = int(input("Option: "))
        if opc == 1:
            pj.realizar_ataque(objetivo)
    elif pj.titulo == "Wizard":
        print("1. Attack.")
        print("2. Heal. (NOT IMPLEMENTED)")
        print("3. Meteorite storm ☄ (NOT IMPLEMENTED)")
        opc = int(input("Option: "))
        if opc == 1:
            pj.realizar_ataque(objetivo)
    elif pj.titulo == "Archer":
        print("1. Attack.")
        print("2. Accurate shot. (NOT IMPLEMENTED)")
        print("3. arrow storm. (NOT IMPLEMENTED)")
        if opc == 1:
            pj.realizar_ataque(objetivo)
        opc = int(input("Option: "))
    print(objetivo)