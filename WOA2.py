'''
Se importan las librerias de sys y time para que funcionen con text_speed
'''
from resources import *
import random, os
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
        if pj.titulo == "Warrior":
            text_speed(f"{index+1} | Title: {pj.color} {pj.titulo} {Style.RESET_ALL} | Name: {pj.nombre}")
        elif pj.titulo == "Sorcerer":
            text_speed(f"{index+1} | Title: {pj.color} {pj.titulo} {Style.RESET_ALL} | Name: {pj.nombre}")
        elif pj.titulo == "Archer":
            text_speed(f"{index+1} | Title: {pj.color} {pj.titulo} {Style.RESET_ALL} | Name: {pj.nombre}")
        else:
            text_speed(f"{index+1} | Title: {pj.color} {pj.titulo} {Style.RESET_ALL} | Name: {pj.nombre}")
    time.sleep(2)
            
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
        if pj.titulo == "Warrior":
            text_speed(f"Title: {pj.color} {pj.titulo} {Style.RESET_ALL} | Name: {pj.nombre}")
        elif pj.titulo == "Sorcerer":
            text_speed(f"Title: {pj.color} {pj.titulo} {Style.RESET_ALL} | Name: {pj.nombre}")
        elif pj.titulo == "Archer":
            text_speed(f"Title: {pj.color} {pj.titulo} {Style.RESET_ALL} | Name: {pj.nombre}")
        else:
            text_speed(f"Title: {pj.color} {pj.titulo} {Style.RESET_ALL} | Name: {pj.nombre}")
    time.sleep(2)
    text_speed("--***---***--***---***--***---***", 0)
    print()

def limpiar_consola():
    os.system("cls") if os.name == "nt" else os.system("clear")
    
def nombrarGanador(fundadores, rondas):
    limpiar_consola()
    text_speed(f"You have conquered the kingdom after {rondas} tough battles, the king in the Python. Long live the king {fundadores[0]}")
    
def eliminarPersonaje(objetivo, asesino):
    if objetivo.titulo=="Founder":
        text_speed('''
                ⚔️ The Fall of the Founder ⚔️
                
                Today, the kingdom is tinged with shadows with the death of {objetivo.nombre}, 
                founder of the glorious {objetivo.clan} clan. His days of leadership 
                and bravery have come to an end, slain in battle by the {asesino.clan} clan.
                
                According to the ancient laws of the kingdom, the members of the {objetivo.clan} clan must now bow to their new destiny, 
                becoming part of the victorious {asesino.clan} clan. May your spirit live under a new banner.''')
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
            text_speed(f"Choosing the player class {i+1}/{cantidadJugadores}: ")
            
            opcionPersonaje = int(input(f"1. {Fore.RED} Warrior {Style.RESET_ALL} \n2. {Fore.GREEN} Sorcerers {Style.RESET_ALL} \n3. {Fore.CYAN} Archer {Style.RESET_ALL} \nOption: "))
            if opcionPersonaje == 1:
                guerrero = crearGuerrero("Warrior")
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
                    limpiar_consola()
            elif opcionPersonaje == 3:
                arquero = crearArquero("Archer")
                seleccionarClan(arquero)
                limpiar_consola()


    listarTodoElStaff()
    turnos_ordenados = organizarTurno(lista_personajes)
    limpiar_consola()
    rondas = 0
    #Mientras que existe más de un fundador
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
            text_speed(f"*** Turn: {cont_turnos} ***")
            text_speed(f"It's the turn of {jugadorEnTurno.titulo} | {jugadorEnTurno.nombre}")
            objetivo = seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros)
            print()
            text_speed("-- Choose an option --")
            
            # Filtrar el clan del fundador para verificar si está solo.
            clan = next((clan_personaje for clan_personaje in clanes if clan_personaje.nombre == jugadorEnTurno.clan), None)
            
            if jugadorEnTurno.titulo == "Founder":
                if clan and len(clan.miembros) <= 1 and not jugadorEnTurno.estado_ataque_final:
                        audio = "Gael"
                        reproducir_musica(audio)
                        jugadorEnTurno.elegir_ataque_desesperado()# Elegir el ataque a gusto por el fundador para hacer sufrir a sus enemigos por la caida de sus hermanos.
                        jugadorEnTurno.fundador_ataque_desesperado(clanes)
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
                text_speed("3. sword dance. (NO IMPLEMENTADO)")
                opc = int(input("Option: "))
                if opc == 1:
                    estadoObjetivo=jugadorEnTurno.realizar_ataque(objetivo)
                    if estadoObjetivo == 0:
                        eliminarPersonaje(objetivo, jugadorEnTurno)
                    print()
                elif opc == 2:
                    jugadorEnTurno.protector(objetivo)  #el jugador en turno entra en la lista del objetivo (lista de protectores)
                    jugadorEnTurno.protegido(objetivo)  #el objetivo entra en la lista del jugador en turno (lista de protegidos)
            
            elif jugadorEnTurno.titulo == "Sorcerer":
                jugadorEnTurno.regeneracion_mana()
                input("aqui estoy regenerando")
                text_speed("1. Attack.")
                # text_speed("2. cure. (NO IMPLEMENTADO)")
                text_speed("3. Meteorite storm ☄")
                text_speed("4. Double attack")
                opc = int(input("Option: "))
                if opc == 1:
                    estadoObjetivo = jugadorEnTurno.realizar_ataque(objetivo)
                    if estadoObjetivo == 0:
                        eliminarPersonaje(objetivo, jugadorEnTurno)
                elif opc == 3:
                    estadoObjetivo = jugadorEnTurno.realizar_ataque(objetivo,"storm meteorite",5)
                    eliminarPersonaje(objetivo, jugadorEnTurno)
                elif opc == 4:
                    estadoObjetivo = jugadorEnTurno.ataque_doble(objetivo,"double attack",10)
                    if estadoObjetivo == 0:
                        eliminarPersonaje(objetivo, jugadorEnTurno)

            elif jugadorEnTurno.titulo == "Archer":
                print()
                text_speed("1. Attack.")
                text_speed("2. Poison Arrow")
                text_speed("3. healing arrow")
                opc = int(input("Option: "))
                if opc == 1:
                    estadoObjetivo=jugadorEnTurno.realizar_ataque(objetivo)
                    if estadoObjetivo == 0:
                        eliminarPersonaje(objetivo, jugadorEnTurno)
                elif opc == 2:
                    jugadorEnTurno.flecha_venenosa(objetivo)
                    lista_envenenados.append(objetivo)
                elif opc == 3:
                    jugadorEnTurno.flecha_curativa(objetivo)
                    lista_envenenados.remove(objetivo)
            
        print(objetivo)
        rondas +=1
        # Fin de la ronda (for jugadorEnTurno in turnos_ordenados:)
    nombrarGanador(fundadores, rondas)
