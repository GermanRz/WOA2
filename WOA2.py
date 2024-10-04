import random, os

class Clan:
    cantidadMiembros = 0
    def __init__(self, nombre, fundador):
        self.miembros = []
        self.nombre = nombre
        self.fundador = fundador.nombre
        self.miembros.append(fundador)
        self.cantidadMiembros += 1
        
    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)
        self.cantidadMiembros += 1
        
    def listar_miembros(self):
        print()
        print("*** *** *** *** ***")
        print(f"El clan {self.nombre} tiene {self.cantidadMiembros} miembros")
        for miembro in self.miembros:
            print(miembro)

#***********************************************************************

class Personaje:
    def __init__(self, nombre, titulo, clan = None):
        self.nombre = nombre
        self.titulo = titulo
        #self.slot_pocion = slot_pocion = []
        self.clan = clan

    def asignar_clan(self, clan):
        self.clan = clan

    def realizar_ataque(self, objetivo):
        f"{self.nombre} ha realizado un ataque!"
        damage = ((self.fuerza + self.ataque) / ((self.vida_original-self.puntos_vida) + self.vida_original)) / 10
        objetivo.recibir_ataque(damage)

    def recibir_ataque(self, damage):
        f"{self.nombre} ha recibido daño!"
        factor_damage = (self.defensa * damage) / 100
        self.fuerza = round(self.fuerza / (factor_damage + 1))
        self.puntos_vida = round(self.puntos_vida / (factor_damage + 1))
        self.defensa = round(self.defensa / (factor_damage + 1))
        self.ataque = round(self.ataque / (factor_damage + 1))

        if self.puntos_vida > 0:
            print(f"{self.nombre} ha recibido un ataque puntos de vida = {self.puntos_vida}")
        else:
            print(f"El {self.titulo} {self.nombre} ha muerto")

    def __str__(self):
        return (f"{self.titulo}: {self.nombre}\n"
                f"Fuerza: {self.fuerza}, Puntos de Vida: {self.puntos_vida}, "
                f"Defensa: {self.defensa}, Ataque: {self.ataque}, "
                f"Clan: {self.clan}")
        
#***********************************************************************

class Guerrero(Personaje):
    def __init__(self, nombre, titulo = "Guerrero"):
        super().__init__(nombre, titulo)
        self.fuerza = 90
        self.puntos_vida = 100
        self.defensa = 90
        self.ataque = 100
        self.vida_original = self.puntos_vida
        
#***********************************************************************

class Mago(Personaje):
    def __init__(self, nombre, titulo = "Mago"):
        super().__init__(nombre, titulo)
        self.fuerza = 80
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 90
        self.vida_original = self.puntos_vida

#***********************************************************************

class Arquero(Personaje):
    def __init__(self, nombre, titulo = "Arquero"):
        super().__init__(nombre, titulo)
        self.fuerza = 95
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 120
        self.vida_original = self.puntos_vida

#***********************************************************************

class Fundador(Mago):
    def __init__(self, nombre):
        super().__init__(nombre, "Fundador")
        self.fuerza = 100
        self.puntos_vida = 110
        self.defensa = 110
        self.ataque = 110
        self.vida_original = self.puntos_vida
        print(f"{self.nombre} ha fundado un clan.")
        
#***********************************************************************


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

cantidadJugadores = int(input("Cantidad de jugadores: "))
for i in range(cantidadJugadores):
    if i == 0:
        mago = crearMago("Fundador")
        fundador = crearFundador(mago)
        crearClan(fundador)
    else:
        print()
        print(f"Eligiendo la clase del jugador {i+1}/{cantidadJugadores}: ")
        
        opcionPersonaje = int(input("1.Guerrero\n2.Mago\n3.Arquero\nOpción: "))
        if opcionPersonaje == 1:
            guerrero = crearGuerrero("Guerrero")
            seleccionarClan(guerrero)
        elif opcionPersonaje == 2:
            mago = crearMago("Mago")
            opcionCrearClan = int(input("Desea crear su propio clan?\n1. SI\n2. NO\nOpción: "))
            if opcionCrearClan == 1:
                fundador = crearFundador(mago)
                crearClan(fundador)
            else:
                seleccionarClan(mago)
        elif opcionPersonaje == 3:
            arquero = crearArquero("Arquero")
            seleccionarClan(arquero)


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
        print("2. Curar.")
        opc = int(input("Opción: "))
        if opc == 1:
            pj.realizar_ataque(objetivo)
    elif pj.titulo == "Guerrero":
        print("1. Atacar.")
        print("2. Defender.")
        opc = int(input("Opción: "))
        if opc == 1:
            pj.realizar_ataque(objetivo)
    elif pj.titulo == "Mago":
        print("1. Atacar.")
        print("2. Crear potis.")
        opc = int(input("Opción: "))
        if opc == 1:
            pj.realizar_ataque(objetivo)
    elif pj.titulo == "Arquero":
        print("1. Atacar.")
        print("2. Flechazo certero.")
        if opc == 1:
            pj.realizar_ataque(objetivo)
        opc = int(input("Opción: "))
    print(objetivo)