'''
Se importan las librerias de sys y time para que funcionen con text_speed
'''
import random, os
import threading
from personajes import *
from clanes import *

from colorama import Fore, Style
'''LOS FUNDADORES TENDRAN COLOR AZUL
LOS MAGOS TENDRAN UN COLOR VERDE
LOS GUERRREROS TENDRAN COLOR ROJO
LOS ARQUEROS TENDRAN UN COLOR CYAN
LOS CLANES TENDRÁN UN COLOR MORADO'''

#--INICIO FUNCIONES--

def crearGuerrero(titulo, color = Fore.RED):
    nombre = input(f"Name of the {color} {titulo} {Style.RESET_ALL}: ").upper()
    guerrero = Guerrero(nombre)
    guerreros.append(guerrero)
    return guerrero

def crearMago(titulo, color = Fore.GREEN):
    nombre = input(f"Name of the {color}  {titulo} {Style.RESET_ALL}: ").upper()
    mago = Mago(nombre)
    magos.append(mago)
    return mago

def crearArquero(titulo,color = Fore.CYAN):
    nombre = input(f"Name of the {color} {titulo} {Style.RESET_ALL}: ").upper()
    arquero = Arquero(nombre)
    arqueros.append(arquero)
    return arquero

def crearFundador(mago,color = Fore.BLUE):
    text_speed(f"Your destiny is to be a {color} founder {Style.RESET_ALL} in these wastelands of Pythonias...")
    fundador = Fundador(mago.nombre)
    fundadores.append(fundador)
    magos.remove(mago)
    return fundador

def crearClan(fundador):
    nombreClan = input("clan's name: ").upper()
    clan = Clan(nombreClan, fundador)
    clanes.append(clan)
    fundador.asignar_clan(nombreClan)
    
def buscarClan(clanes, jugador):
    for clan_personaje in clanes:
        if clan_personaje.nombre == jugador.clan:
            return clan_personaje 
    

def seleccionarClan(personaje):
    asignado = False
    while not asignado:
        for index, clan in enumerate(clanes):
            text_speed(f"{index+1} : {Fore.MAGENTA} {clan.nombre} {Style.RESET_ALL}")
        print()
        nombreClan = input("Enter the name of the clan -> ").upper()
        for clan in clanes:
            if clan.nombre == nombreClan:
                personaje.asignar_clan(nombreClan)
                clan.agregar_miembro(personaje)
                input(f"{personaje.nombre} has been added to the clan {Fore.MAGENTA} {clan.nombre} {Style.RESET_ALL} <ENTER TO CONTINUE>")
                asignado = True
        if asignado == False:
            text_speed(f"The clan {nombreClan} does not exist...")
            print()


def seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros, jugadorTurno):
    while True:
        try:
            text_speed("-- Selection mode --", 0)
            text_speed("-- Select your goal --", 0)
            text_speed("1. By clan.", 0)
            text_speed("2. List all characters.", 0)
            text_speed("3. Attack by title.", 0)
            opcion = int(input("Choose an option: "))
            if opcion <1 or opcion >3 :
                text_speed("invalid opcion, plase select")
            else:
                 break
        except ValueError:
                         text_speed("please enter a valid option ")
            
    limpiar_consola()
    if opcion == 1:
        text_speed("clan list")
        for index, clan in enumerate(clanes):
            print(f"{index+1} {Fore.MAGENTA} {clan.nombre} {Style.RESET_ALL}")
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
        text_speed(f"player turn : {jugadorTurno.nombre}")
        imprimirTodosPersonajes(listaPersonajes)
        nombreObjetivo = input("Enter the name of your target: ").upper()
        for miembro in listaPersonajes:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    if opcion == 3:
        text_speed("Title to list", 0)
        text_speed(Fore.BLUE + "1. Founders", 0)
        text_speed(Fore.GREEN + "2. Sorcerers", 0)
        text_speed(Fore.RED + "3. warriors", 0)
        text_speed(Fore.CYAN + f"4. Archers {Style.RESET_ALL}", 0)
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
        imprimirTodosPersonajes(listaObjetivos)
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
        if pj.titulo == "Warrior":
            text_speed(f"{index+1} | Title: {pj.color} {pj.titulo} {Style.RESET_ALL} | Name: {pj.nombre}")
        elif pj.titulo == "Sorcerer":
            text_speed(f"{index+1} | Title: {pj.color} {pj.titulo} {Style.RESET_ALL} | Name: {pj.nombre}")
        elif pj.titulo == "Archer":
            text_speed(f"{index+1} | Title: {pj.color} {pj.titulo} {Style.RESET_ALL} | Name: {pj.nombre}")
        else:
            text_speed(f"{index+1} | Title: {pj.color} {pj.titulo} {Style.RESET_ALL} | Name: {pj.nombre}")
    # time.sleep(2)
    input("ENTER to continue...")
            
    return turnos_ordenados

#--FIN FUNCIONES--

#--INICIO PROCEDIMIENTOS--

def listarTodoElStaff():
    global lista_personajes
    lista_personajes = fundadores + magos + guerreros + arqueros
    text_speed("List of all the characters present in the game: ")
    text_speed("--***---***--***---***--***---***", 0)
    for pj in lista_personajes:
        if pj.titulo == "Warrior":
            text_speed(f"Title: {pj.color}{pj.titulo}{Style.RESET_ALL} | Name: {pj.nombre}")
        elif pj.titulo == "Sorcerer":
            text_speed(f"Title: {pj.color}{pj.titulo}{Style.RESET_ALL} | Name: {pj.nombre}")
        elif pj.titulo == "Archer":
            text_speed(f"Title: {pj.color}{pj.titulo}{Style.RESET_ALL} | Name: {pj.nombre}")
        else:
            text_speed(f"Title: {pj.color}{pj.titulo}{Style.RESET_ALL} | Name: {pj.nombre}")
        text_speed(f"Strength: {pj.fuerza}, Life Points: {pj.puntos_vida}, Defense: {pj.defensa}, Attack: {pj.ataque}")
        text_speed(pj.mostrar_barra_mana())
        text_speed("---------------------------")
    text_speed("--***---***--***---***--***---***", 0)
    input("ENTER to continue...")
    print()

def limpiar_consola():
    os.system("cls") if os.name == "nt" else os.system("clear")
    
def nombrarGanador(fundadores, rondas):
    limpiar_consola()
    text_speed(f"You have conquered the kingdom after {rondas} tough battles, the king in the Python. Long live the king {fundadores[0]}")
    
def eliminarPersonaje(objetivo, asesino):
    if objetivo.titulo=="Founder":
        text_speed(f"⚔️ The Fall of the Founder ⚔️\n\n Today, the kingdom is tinged with shadows with the death of {objetivo.nombre},\n founder of the glorious {objetivo.clan} clan. His days of leadership \n and bravery have come to an end, slain in battle by the {asesino.clan} clan.\n\n        According to the ancient laws of the kingdom, \n the members of the {objetivo.clan} clan\n must now bow to their new destiny, becoming part of the victorious {asesino.clan} clan. \nMay your spirit live under a new banner.",0.02)
        fundadores.remove(objetivo)
        #en este punto se debe implementar ya sea la muerte de los miembros del clan derrotado o el paso de los mismos al clan asesino
        print()
        input("ENTER to continue...")
    elif objetivo.titulo=="Archer":
        arqueros.remove(objetivo)
    elif objetivo.titulo=="Sorcerer":
        magos.remove(objetivo)
    else:
        guerreros.remove(objetivo)
        #en este punto se debe inhablitar la defensa de los protegidos por este guerrero
        
    #remover de los jugadores activos        
    turnos_ordenados.remove(objetivo)
    # remover del clan
    for clan in clanes:
        if clan.nombre == objetivo.clan:
            clan.remover_miembro(objetivo)
            
def informacionClanes():
    opc = 0
    while opc!=3:
        limpiar_consola()
        print(f"round{rondas}")
        text_speed("After this tough encounter you will find the status of the clans after the battle")
        text_speed("1. All clans.")
        text_speed("2. Specific clan.")
        text_speed("3. Continue with the next battle")
        
        try:
            opc = int(input("Option: "))
            if opc == 1:
                for clan in clanes:
                    clan.listar_miembros()
                    input("ENTER to continue...")
            if opc == 2:
                for index, clan in enumerate(clanes):
                    text_speed(f"{index+1} : {clan.nombre}")
                print()
                nombreClan = input("Enter the name of the clan -> ").upper()
                for clan in clanes:
                    if clan.nombre == nombreClan:
                        clan.listar_miembros()
                        input("ENTER to continue...")
            else:
                text_speed("Invalid option. Please select 1, 2, or 3.")
        except ValueError:
            text_speed("Please enter a valid option")


#--FIN PROCEDIMIENTOS--

#--INICIO ARREGLOS--

guerreros = []
magos = []
arqueros = []
fundadores = []
clanes = []
lista_envenenados = []

lista_personajes = fundadores + magos + guerreros + arqueros

#--FIN ARREGLOS

#INICIO CÓDIGO PRINCIPAL

if __name__=="__main__":
    audio = "Messmer"
    reproducir_musica(audio)
    limpiar_consola()
    text_speed(f"{Fore.RED}--    WOA2: ¡War for the glory and our honor!    --{Style.RESET_ALL}\n")
    text_speed(f"Once again... Rise, forgetful of the eternal night without hope, and reach the longed-for glory of our lady {Fore.LIGHTCYAN_EX}Nyxara... {Style.RESET_ALL}")
    
    while True:
        try:
            cantidadJugadores = int(input("Number of players: "))
            if cantidadJugadores < 2 or cantidadJugadores > 20:
                text_speed("Amount entered invalid! Please enter a number between 2 and 20")
            else:
                break
        except ValueError:
            text_speed("Please enter a number...")
    limpiar_consola()
    
    for i in range(cantidadJugadores):
        if i == 0:
            mago = crearMago("Founder")
            fundador = crearFundador(mago)
            crearClan(fundador)
            limpiar_consola()
        else:
            print()
            while True:
                try:
                    text_speed(f"Choosing the player class {i+1}/{cantidadJugadores}: ")
                    opcionPersonaje = int(input(f"1. {Fore.RED} Warrior {Style.RESET_ALL} \n2. {Fore.GREEN} Sorcerers {Style.RESET_ALL} \n3. {Fore.CYAN} Archer {Style.RESET_ALL} \nOption: "))
                    limpiar_consola()
                    if opcionPersonaje <=0 or opcionPersonaje >=4:
                        text_speed("Invalid option, please enter a correct option")
                    elif opcionPersonaje == 1:
                        guerrero = crearGuerrero("Warrior")
                        seleccionarClan(guerrero)
                        limpiar_consola()
                        break
                    elif opcionPersonaje == 2:
                        mago = crearMago("Sorcerer")
                        opcionCrearClan = int(input("Do you want to create your own clan?\n1.YES\n2.NO\nOption: "))
                        if opcionCrearClan == 1:
                            fundador = crearFundador(mago)
                            crearClan(fundador)
                            limpiar_consola()
                        else:
                            seleccionarClan(mago)
                        break
                    elif opcionPersonaje == 3:
                        arquero = crearArquero("Archer")
                        seleccionarClan(arquero)
                        limpiar_consola()
                        break
                    else:
                        break
                except ValueError:
                    limpiar_consola()
                    text_speed("Please enter a correct option")

    listarTodoElStaff()
    turnos_ordenados = organizarTurno(lista_personajes)
    limpiar_consola()
    #Mientras que existe más de un fundador
    rondas = 1
    # ?Mientras que existe más de un fundador
    while len(fundadores)>1:

        informacionClanes()
        cont_turnos = 0
        for jugadorEnTurno in turnos_ordenados:
            for envenenados in lista_envenenados:
                envenenados.restar_punto_vida()
                if jugadorEnTurno == envenenados:
                    lista_envenenados.remove(jugadorEnTurno)

            cont_turnos += 1
            limpiar_consola()
            text_speed(f"*** Round: {rondas} ***")
            text_speed(f"*** Turn: {cont_turnos} ***")
            text_speed(f"It's the turn of {jugadorEnTurno.titulo} | {jugadorEnTurno.nombre}")
            objetivo = seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros, jugadorEnTurno)
            print()
            text_speed("-- Choose an option --")
            
            # Filtrar el clan del fundador para verificar si está solo.
            clan = next((clan_personaje for clan_personaje in clanes if clan_personaje.nombre == jugadorEnTurno.clan), None)
            
            if jugadorEnTurno.titulo == "Founder":
                if clan and len(clan.miembros) <= 1 and not jugadorEnTurno.estado_ataque_final:
                        audio = "Gael"
                        reproducir_musica(audio)
                        jugadorEnTurno.elegir_ataque_desesperado()# Elegir el ataque a gusto por el fundador para hacer sufrir a sus enemigos por la caida de sus hermanos.
                        jugadorEnTurno.fundador_ataque_desesperado(clanes,lista_personajes)
                        clan.info_miembros(jugadorEnTurno.titulo)
                        input("Press enter to continue")
                        limpiar_consola()
                else:
                    text_speed("1. Attack.")
                    text_speed("2. Create potions.")
                    text_speed("3. Give potions.")
                    while True:
                        try:
                            opc = int(input("Option: "))
                            if 1 > opc > 3:
                                text_speed("Invalid option. Please select 1, 2, or 3.")
                            else:
                                break
                        except ValueError:
                            text_speed("Please enter a valid option")
                    if opc == 1:
                        # ********************************************************
                        #CODIGO PArA VERIFICAR LA MUERTE DEL OBJETIVO  IMPORTANTE DESPUES DE CADA ATAQUE
                        estadoObjetivo=jugadorEnTurno.realizar_ataque(objetivo)
                        if estadoObjetivo == 0:
                            eliminarPersonaje(objetivo, jugadorEnTurno)
                        # ********************************************************
                    elif opc == 2:
                        jugadorEnTurno.crear_pociones()
                        text_speed(f"My potion/s {fundador.cont_pociones_fundador} | {fundador.bolsillo_pociones_fundador}")
                    elif opc == 3:
                        jugadorEnTurno.entregar_pocion(magos, objetivo)
                    
            elif jugadorEnTurno.titulo == "Warrior":
                print()
                text_speed("1. Attack.")
                text_speed("2. Defend.")
                text_speed("3. Tornado Attack.")
                opc = int(input("Option: "))
                if opc == 1:
                    estadoObjetivo, objetivo=jugadorEnTurno.realizar_ataque(objetivo)
                    if estadoObjetivo == 0:
                        eliminarPersonaje(objetivo, jugadorEnTurno)
                    print()
                elif opc == 2:
                    jugadorEnTurno.protector(objetivo)  #el jugador en turno entra en la lista del objetivo (lista de protectores)
                    jugadorEnTurno.protegido(objetivo)  #el objetivo entra en la lista del jugador en turno (lista de protegidos)
                elif opc == 3:
                    jugadorEnTurno.ataque_tornado(clanes, rondas)
            
            elif jugadorEnTurno.titulo == "Sorcerer":
                jugadorEnTurno.regeneracion_mana()
                text_speed("1. Attack.")
                # text_speed("2. cure. (NO IMPLEMENTADO)")
                text_speed("3. Meteorite storm ☄")
                text_speed("4. Double attack")
                opc = int(input("Option: "))
                if opc == 1:
                    estadoObjetivo, objetivo = jugadorEnTurno.realizar_ataque(objetivo)
                    if estadoObjetivo == 0:
                        eliminarPersonaje(objetivo, jugadorEnTurno)
                elif opc == 3:
                    estadoObjetivo, objetivo = jugadorEnTurno.realizar_ataque(objetivo,"storm meteorite",5)
                    eliminarPersonaje(objetivo, jugadorEnTurno)
                elif opc == 4:
                    estadoObjetivo, objetivo = jugadorEnTurno.ataque_doble(objetivo,"double attack",10)
                    if estadoObjetivo == 0:
                        eliminarPersonaje(objetivo, jugadorEnTurno)

            elif jugadorEnTurno.titulo == "Archer":
                jugadorEnTurno.mostrar_flechas()
                print()
                while True:
                            try:
                                text_speed("1. Attack.")
                                text_speed("2. Poison Arrow")
                                text_speed("3. healing arrow")
                                text_speed("4. create poison arrow")
                                text_speed("5. accurate arrow")
                                text_speed("6. create accurate arrow")
                                text_speed("7. create healing Arrow")
                                opc = int(input("Option: "))
                                if opc<1 or opc >7 :
                                    text_speed("invalid opcion, plase select")
                                else:
                                    break
                            except ValueError:
                                text_speed("please enter a valid option ")
                                                
                
                if opc == 1:
                    estadoObjetivo, objetivo=jugadorEnTurno.realizar_ataque(objetivo)
                    if estadoObjetivo == 0:
                        eliminarPersonaje(objetivo, jugadorEnTurno)
                elif opc == 2:
                    estadoObjetivo, objetivo = jugadorEnTurno.flecha_venenosa(objetivo)
                    if estadoObjetivo == 0:
                        eliminarPersonaje(objetivo, jugadorEnTurno)
                    elif estadoObjetivo == 1 and objetivo!=None:
                        lista_envenenados.append(objetivo)
                    else:
                        print(f"You don't have any poison arrow")
                        input("ENTER to continue...")
                elif opc == 3:
                    if objetivo in lista_envenenados:
                        jugadorEnTurno.flecha_curativa(objetivo)
                        lista_envenenados.remove(objetivo)
                    else:
                        print("the target is not poisoned")
                elif opc == 4:
                    jugadorEnTurno.crear_flecha_venenosa()
                    print("You spent your turn creating a new poision arrow.")
                elif opc == 5:
                    estadoObjetivo, objetivo, error = jugadorEnTurno.flecha_certera(objetivo,rondas)
                    if error == 0:
                        if estadoObjetivo == 0:
                            eliminarPersonaje(objetivo, jugadorEnTurno)
                    elif error == 1:
                        print(f"This battle is invalid for this attack - battle {rondas}")
                    else:
                        print("Your carcaj doesn't have accurate arrows")
                elif opc == 6:
                    estado = jugadorEnTurno.crear_flecha_certera(rondas)
                    if estado == 1:
                        print(f"This battle is invalid for the cration of this arrow - batte {rondas}")
                    elif estado == 2:
                        print(f"You already have this arrow in your carcaj")
                    else:
                        print("You spent your turn creating a new accurate arrow.")
                elif opc ==7:
                    jugadorEnTurno.crear_flecha_curativa()
                    print(f"{jugadorEnTurno.nombre} ahora tiene {jugadorEnTurno.cont_flechas_curativas} flechas curativas")
            input()
            text_speed("ENTER to continue")
                    
                    
            
        print(objetivo)
        rondas +=1
        # Fin de la ronda (for jugadorEnTurno in turnos_ordenados:)
    nombrarGanador(fundadores, rondas)
