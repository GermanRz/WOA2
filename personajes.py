
import random
from resources import *
import colorama
from colorama import Fore, Style

colorama.init()#esto es necesario para iniciar la clase colorama


from resources import text_speed
from tqdm import tqdm

class Personaje:
    def __init__(self, nombre, titulo, clan = None):
        self.nombre = nombre
        self.titulo = titulo
        self.clan = clan
        self.lst_protectores = []
        self.lst_protegidos = []

    def asignar_clan(self, clan):
        self.clan = clan
        
    '''
    se agregan dos parametros acicionales
    txtAtaque : descripcion del ataque recibido (flecha venenosa, ataque meteorito, etc...)  default = " "
    intensidadAtaque: valor entero de la intensidad del ataque.   default = 5
    '''
    def realizar_ataque(self, objetivo, txtAtaque=" ", intensidadAtaque=5):
        sonidos = {
            "Founder": pygame.mixer.Sound("Efectos-sonido/ataque-magico-fundador.wav"),
            "Sorcerer": pygame.mixer.Sound("Efectos-sonido/ataque-magico-mago.wav"),
            "Warrior": pygame.mixer.Sound("Efectos-sonido/Espadazo.flac"),
            "Archer": pygame.mixer.Sound("Efectos-sonido/Flechazo.mp3")
        }
        
        if self.titulo in sonidos.keys():
            sonidos[self.titulo].play()
        
        # verificar si el objetivo tiene protectores
        if len(objetivo.lst_protectores)>0 and txtAtaque!="accurate arrow":
            objetivo = objetivo.lst_protectores.pop(0)  #el nuevo objetivo es el primer protector

        print(f"{self.nombre} has carried out an attack!  {txtAtaque}")
        # 1. Calculamos el poder del ataque usando solo fuerza y ataque del atacante
        poder_ataque = (self.fuerza + self.ataque)
        # 2. Calculamos el poder de la defensa usando solo fuerza y defensa del objetivo
        poder_defensa = (objetivo.fuerza + objetivo.defensa)
        # 3. Calculamos la diferencia de poder
        diferencia_poder = poder_ataque - poder_defensa
        # 4. Calculamos el porcentaje de daño base
        if diferencia_poder > 0:
            # Si el ataque es más fuerte que la defensa
            factor_ataque = intensidadAtaque + (diferencia_poder * 0.5)  # 0.5% por cada punto de diferencia
        else:
            # Si la defensa es más fuerte o igual que el ataque
            factor_ataque = intensidadAtaque  # Daño mínimo de intensidadAtaque%
        # 6. Calculamos el daño final
        damage = int((objetivo.vida_original * factor_ataque) / 100)
        estado=objetivo.recibir_ataque(damage)
        #Se agrega el objetivo en el return, ya que el objetivo puede cambiar durante el ataque por un protector
        return estado, objetivo


    def recibir_ataque(self, damage):
        # print("damage :", damage)
        self.puntos_vida = max(0, self.puntos_vida - damage)
        #calculamos el porcentaje de vida resultante
        porcentaje_vida = self.puntos_vida / self.vida_original
        # print(f"{porcentaje_vida} = {self.puntos_vida} / {self.vida_original}")
        # Los atributos se disminuyen proporcionalmente a la vida perdida
        self.fuerza = max(1,int(self.fuerza_original * porcentaje_vida))
        self.defensa = max(1,int(self.defensa_original * porcentaje_vida))
        self.ataque = max(1,int(self.ataque_original * porcentaje_vida))
        # print(f"fuerza {self.fuerza} - defensa {self.defensa} - ataque {self.ataque}")
        if self.puntos_vida > 0:
            print(f"{self.nombre} has received an attack hit points = {self.puntos_vida}")
            input("ENTER to continue...")
            return 1 #live
        else:
            if self.titulo=="Warrior":
                print(f"The {Fore.RED} {self.titulo} {Style.RESET_ALL} {self.nombre} has died")
            elif self.titulo=="Sorcerer":
                print(f"The {Fore.GREEN} {self.titulo} {Style.RESET_ALL} {self.nombre} has died")
            elif self.titulo=="Archer":
                print(f"The {Fore.CYAN} {self.titulo} {Style.RESET_ALL} {self.nombre} has died")
            else:
                print(f"The {Fore.BLUE} {self.titulo} {Style.RESET_ALL} {self.nombre} has died")

            #si el titulo del objetivo fallecido es un guerrero se debe verificar su lista de protegidos para eliminarse de cada uno de ellos como protector
            if self.titulo == "Warrior":
                if len(self.lst_protegidos)>0:
                    for protegido in self.lst_protegidos:
                        if protegido in self.lst_protectores:
                            protegido.lst_protectores.remove(self)
            input("ENTER to continue...")
            
            '''
            si matan a un personaje que tiene protectores se debe eliminar el personaje de la lista de proteguidos de cada uno de sus protectores
            '''
            if self.lst_protectores:
                for protector in self.lst_protectores:
                    if protector in protector.lst_protegidos:
                        protector.lst_protegidos.remove(self)
                    
            return 0 #death
    
    # APLICANDO EFECTO DEL VENENO AL OBJETIVO QUITANDO DE A 1 PUNTO DE VIDA
    
    def restar_punto_vida(self):
        if self.puntos_vida != 0:
            self.puntos_vida -= 1
        if self.puntos_vida > 0:
            print("you are under the attack of a poinsoned arrow")
        if   self.puntos_vida == 0:
            print(f"{self.nombre} is dead")
    
    
    
    #FIN

    def protector(self, objetivo):
        objetivo.lst_protectores.append(self)

    def __str__(self):
        return (f"{self.titulo}: {self.nombre} - "
                f"Strength: {self.fuerza}, Life Points: {self.puntos_vida}, "
                f"Defense: {self.defensa}, Attack: {self.ataque}, "
                f"Clan: {self.clan}")
                # f"Clan: {self.clan}, Mana Bar: {self.barra_mana}")

        
#***********************************************************************

class Guerrero(Personaje):
    def __init__(self, nombre, titulo = "Warrior", color = Fore.RED):
        super().__init__(nombre, titulo)
        self.fuerza = 90
        self.puntos_vida = 100
        self.defensa = 90
        self.ataque = 100
        self.color = color
        # Guardamos los valores máximos/iniciales de cada atributo
        self.fuerza_original = self.fuerza
        self.vida_original = self.puntos_vida        
        self.defensa_original = self.defensa
        self.ataque_original = self.ataque
        self.lst_protegidos = []

    def protegido(self, protegido):
        self.lst_protegidos.append(protegido)
        
#***********************************************************************

class Mago(Personaje):
    cont_pociones_mago = 0
    def __init__(self, nombre, titulo="Sorcerer", color=Fore.GREEN):
        super().__init__(nombre, titulo)
        self.fuerza = 80
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 90
        self.color = color
        self.bolsillo_pociones_mago = []
        self.barra_mana = 50
        # Guardamos los valores máximos/iniciales de cada atributo
        self.fuerza_original = self.fuerza
        self.vida_original = self.puntos_vida        
        self.defensa_original = self.defensa
        self.ataque_original = self.ataque
        # Solo mostrar la barra de mana si es un Mago directamente
        if type(self) is Mago:
            print(f"\n{Fore.CYAN}✧ {self.nombre}'s Mana ✧{Style.RESET_ALL}")
            self.mostrar_barra_mana()

    def mostrar_barra_mana(self):
        # Solo mostrar si es la clase Mago directamente
        if type(self) == Mago:
            with tqdm(total=100, 
                    bar_format='{desc}{percentage:3.0f}%|{bar}|',
                    desc=f"{Fore.CYAN}🔮 {Style.RESET_ALL}",
                    ncols=50,
                    colour='blue') as pbar:
                pbar.n = self.barra_mana
                pbar.refresh()
    
    def regeneracion_mana(self):
        regeneracion = random.randint(5, 25)
        self.barra_mana += regeneracion
        if self.barra_mana > 100:
            self.barra_mana = 100
        print(f"{self.nombre} genereated {regeneracion} of mana. mana's bar: {self.barra_mana}")
        

    def usar_hechizo(self, costo_mana):
        if self.barra_mana >= costo_mana:
            self.barra_mana -= costo_mana
            print(f"{self.nombre} used a spell. Mana cost: {costo_mana}. Mana's bar: {self.barra_mana}")
        else:
            print(f"{self.nombre} haven't enough mana to use this spell.")


    def ataque_doble(self, objetivo):
        if self.barra_mana == 100:
            print(f"{self.nombre} launches double attack {objetivo.nombre}!")
            estado_objetivo = self.realizar_ataque(objetivo,"double attack",10)

    def __str__(self):
        return (f"{self.titulo}: {self.nombre}\n"
                f"Strength: {self.fuerza}, Life Points: {self.puntos_vida}, "
                f"Defense: {self.defensa}, Attack: {self.ataque}, "
                f"Clan: {self.clan}, Mana Bar: {self.barra_mana}")
        
    def conceder_curacion(self, lst_pjs, pj_receptor):
        for index, pj in enumerate(lst_pjs):
            print(f"{index + 1} | {pj.titulo} {pj.nombre}")
        
        while True:
            try:
                opc = input(f"Select number of the character that you wanna heal with the potion (or type 'exit' to cancel): ")
                if opc.lower() == 'exit':
                    print("Operation cancelled.")
                    return pj_receptor  # Salir de la función si el usuario cancela
                
                opc = int(opc) - 1  # Convertir a entero y ajustar el índice
                if 0 <= opc < len(lst_pjs):  # Verifica que la opción esté en la lista
                    if self.cont_pociones_mago > 0:
                        pj_receptor = lst_pjs[opc]  # En la posición que se eligió en la opción
                        self.pj_receptor = pj_receptor  # PJ como un objeto
                        curacion = self.bolsillo_pociones_mago.pop()  # Saca la poción del bolsillo
                        self.cont_pociones_mago -= 1  # Decrementa el contador de pociones
                        text_speed(f"{self.nombre} has used a healing potion 🥤 on {self.pj_receptor.nombre}")
                        pj_receptor.fuerza += curacion
                        pj_receptor.puntos_vida += curacion
                        pj_receptor.defensa += curacion
                        pj_receptor.ataque += curacion
                        if pj_receptor.fuerza > pj_receptor.fuerza_original:
                            pj_receptor.fuerza = pj_receptor.fuerza_original
                        if pj_receptor.puntos_vida > pj_receptor.vida_original:
                            pj_receptor.puntos_vida = pj_receptor.vida_original
                        if pj_receptor.defensa > pj_receptor.defensa_original:
                            pj_receptor.defensa = pj_receptor.defensa_original
                        if pj_receptor.ataque > pj_receptor.ataque_original:
                            pj_receptor.ataque = pj_receptor.ataque_original 
                        input("Press ENTER to continue! ")
                    else:
                        input("No more potions left!")
                    return pj_receptor
                else:
                    input("That character doesn't even exist!")
            except ValueError:
                input("Invalid option, please enter a number.")

        

#***********************************************************************

class Arquero(Personaje):
    def __init__(self, nombre, titulo = "Archer", color = Fore.CYAN):
        super().__init__(nombre, titulo)
        self.fuerza = 95
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 120
        self.color = color
        # Guardamos los valores máximos/iniciales de cada atributo
        self.fuerza_original = self.fuerza
        self.vida_original = self.puntos_vida        
        self.defensa_original = self.defensa
        self.ataque_original = self.ataque
        self.vida_original = self.puntos_vida
        self.count_venenosa = 2
        self.count_certera = 1
        self.cont_flechas_curativas = 2
        
        
    def mostrar_flechas(self):
        print(f"{self.nombre} have: {self.count_venenosa} poison arrows.")
        print(f"{self.nombre} have: {self.cont_flechas_curativas} healing arrows.")
        
        
    def crear_flecha_venenosa(self):
        if self.count_venenosa < 2:
            self.count_venenosa+=1
        else:
            print("The maximum capacity is: 2 poison arrows")
            input("Press ENTER to continue.")
            
        
    def flecha_venenosa(self, objetivo ):
        if self.count_venenosa>0:
            estadoObjetivo, objetivo = self.realizar_ataque(objetivo,"poision arrow", 3)
            self.count_venenosa -=1
            return estadoObjetivo, objetivo
        else:
            return 1, None
        
    
    def flecha_curativa(self, objetivo):        
        curacion = round(self.vida_original * 0.01)  
        objetivo.puntos_vida += curacion
        self.cont_flechas_curativas -= 1
        # Asegurarnos de que no supere los puntos de vida originales
        if objetivo.puntos_vida < objetivo.vida_original:
            objetivo.puntos_vida +=1
        print(f"{self.nombre} shoot a healing arrow to {objetivo.nombre} and restored an amount of one life points!")
        
    def crear_flecha_curativa(self):
        if self.cont_flechas_curativas < 2:
            self.cont_flechas_curativas+= 1
            print(f"{self.nombre} create a healing arrow, now you have {self.cont_flechas_curativas} healing arrows")
        else:
            print("you can only have two healing arrows")
        
    def flecha_certera(self, objetivo, ronda):
        if ronda % 1 !=0:
            return 1, objetivo, 1 #ronda no valida
        elif self.count_certera < 1:
            return 1, objetivo, 2 #no hay flechas certeras disponibles
        if  objetivo.lst_protectores:
            print(f"{objetivo.nombre} was protected")
        else:
            print(f"{objetivo.nombre} was notprotected")
            estadoObjetivo, objetivo = self.realizar_ataque(objetivo, "accurate arrow")
            self.count_certera -= 1
            return estadoObjetivo, objetivo, 0  #estado 0, no se presentaon errores
        
        
    def crear_flecha_certera(self, ronda):
        if ronda % 1 != 0:
            return 1 #ronda no valida para la creacion de la flecha certera
        elif self.count_certera >= 1:
            return 2 #Ya tiene una fleha certera
        else:
            self.count_certera = 1
            return 0
            
            
            


#***********************************************************************

class Fundador(Mago):
    cont_pociones_fundador = 0
    def __init__(self, nombre, color = Fore.BLUE):
        Personaje.__init__(self, nombre, "Founder")
        self.fuerza = 100
        self.puntos_vida = 110
        self.defensa = 110
        self.ataque = 110
        self.color = color
        self.fuerza_original = self.fuerza
        self.vida_original = self.puntos_vida        
        self.defensa_original = self.defensa
        self.ataque_original = self.ataque
        self.bolsillo_pociones_fundador = []
        self.estado_ataque_final = False
        self.barra_mana = None
        text_speed(f"{self.nombre} has founded a clan.")

    def crear_pociones(self):
        cura_aleatoria = random.randint(10, 25)
        if self.cont_pociones_fundador <= 3:
            self.bolsillo_pociones_fundador.append(cura_aleatoria)
            self.cont_pociones_fundador += 1#Se aumenta el contador de las pociones
            for pocion in self.bolsillo_pociones_fundador:
                text_speed(f"{self.nombre} 🧙‍♂️🧙‍♀️ Potions: ({self.cont_pociones_fundador} 🥤| Healing: {pocion} 💗)")
            input("PREES ENTER to continue")
        else:
            text_speed(f"Oops! You can´t have more than 3 potions in your pockets 🥤! {list(self.cont_pociones_fundador)}")
            input("PREES ENTER to continue")

    def entregar_pocion(self, lst_magos, pj_receptor):
        for index, pj in enumerate(lst_magos):
            print(f"{index+1} | {pj.titulo} {pj.nombre}")
        opc = int(input(f"Select number of the {pj.titulo} that you give the heal potion: ")) - 1
        if 0 <= opc < len(lst_magos):#VERIFICA QUE LA OPC ESTÉ EN LA LISTA
            pj_receptor = lst_magos[opc]#EN LA POSICIÓN QUE SE ELIGIÓ EN LA OPC
            self.pj_receptor = pj_receptor#PJ COMO UN OBJETO
            if self.bolsillo_pociones_fundador:
                pocion = self.bolsillo_pociones_fundador.pop()#SACA LA POCIÓN DEL BOLSILLO DEL FUNDADOR
                self.cont_pociones_fundador -= 1 # Se resta la poción al mago
                text_speed(f"The {self.titulo} {self.nombre} has given a potion to the {self.pj_receptor.titulo} {self.pj_receptor.nombre}")
                self.pj_receptor.bolsillo_pociones_mago.append(pocion) # Recibe la poción
                self.pj_receptor.cont_pociones_mago += 1 # Se suma la poción al mago
                text_speed(f"The {self.pj_receptor.titulo} | {self.pj_receptor.nombre} has recieved a healing potion 🥤")
                text_speed(f"Potion/s: 🥤 {self.pj_receptor.cont_pociones_mago} | Healing 💗: {list(self.pj_receptor.bolsillo_pociones_mago)} 🧙‍♂️")
                input("Press ENTER to continue! ")
            else:
                text_speed("No potions available to give!")
                input("Press ENTER to continue! ")
        else:
            text_speed(f"That character does'nt even exist!")
            input("Press ENTER to continue! ")
        return pj_receptor
        
    def elegir_ataque_desesperado(self):
        text_speed(f"The {self.titulo} {self.nombre} it's the last member standing in the clan!")
        text_speed("These are my spells!\n")
        ataques = {
            1: "Magnificent destruction of fire 🔥",
            2: "Divine Pillars of Light 👼",
            3: "Domain expansion: Malevolent shrine 🤘",
            4: "Domain expansion: Incommensurable void 🤞",
            5: "Great Chaos Fire Orb 🌋"
        }
    
        for num, ataque in ataques.items():
            text_speed(f"{num} | {ataque}")
        
        estado = True
    
        while estado:
            try:
                opc = int(input("Deciding your final attack: "))
                if opc < 1 or opc > 5:
                    text_speed("I don´t have that attack!")
                else:
                    self.ataque_desesperado = ataques[opc]
                    estado = False
            except ValueError:
                text_speed("Please, enter a valid option...")
    
    def fundador_ataque_desesperado(self, clanes,lst_personaje): # Ataque desesperado
        text_speed(f"...Y'all will gonna suffer the fury of our clan {self.clan}, ...{Fore.RED} The fury... of the fallens! {Style.RESET_ALL}")
        text_speed(f"The {self.titulo} {self.nombre} has gonna begin the final attack!")
        text_speed(f"{Fore.RED} {self.ataque_desesperado} {Style.RESET_ALL}\n", 0.07)
        
        # * Método para filtrar el clan del fundador y asi no esté en su lista de clanes objetivos *
        clanes_filtrado = [clan_objetivo for clan_objetivo in clanes if clan_objetivo.nombre != self.clan]
        lst_personaje_filtrado = [personaje for personaje in lst_personaje if personaje.nombre != self.nombre]
        
        self.fuerza = self.fuerza_original * 1.5
        self.ataque = self.ataque_original * 1.5
        
        # * Selección del modo de ataque del fundador *
        while True:
            try:
                text_speed("¿How would you like to attack?\n1. By select.\n2. Randomly.\n3. Attack Randomly all of them.")
                opc = int(input("Choosing option: "))
                if opc == 1:
                    self._seleccionar_clan(clanes_filtrado)
                    break
                elif opc == 2:
                    self._atacar_desesperado_clan_aleatorio(clanes_filtrado)
                    break
                elif opc == 3:
                    self._seleccionar_personaje_aleatorio(lst_personaje_filtrado)
                    break
                else:
                    text_speed("That option doesn't even exist...")
            except ValueError:
                text_speed("Please, enter a valid option.")
        
    def _seleccionar_clan(self, clanes):
        for index, clan_objetivo in enumerate(clanes):
            text_speed(f"{index+1} | {Fore.MAGENTA} {clan_objetivo.nombre} {Style.RESET_ALL}")
        while True:
            try:
                elegir_clan = int(input("Select by number of the clan that gonna suffer: ")) -1
                if 0 <= elegir_clan < len(clanes):
                    clan = clanes[elegir_clan] #Se elige el clan a atacar
                    miembros_clan = clan.miembros # Se instancian los miembros
                    text_speed(f"The founder has casting his fury in all members of clan {clan.nombre}!\n")
                    
                    for miembro in miembros_clan:
                        self.realizar_ataque(miembro, self.ataque_desesperado, 1)
                        print()
                        text_speed(f"{miembro.nombre} of the clan {clan.nombre} has been attacked with {self.ataque_desesperado} of the {self.titulo} {self.nombre} !\n")
                        text_speed(f"-Strenght: {miembro.fuerza}\n-Life Points: {miembro.puntos_vida}\n-Defense: {miembro.defensa}\n-Attack: {miembro.ataque}\n")
                    self.estado_ataque_final = True # El fundador ya realizó su ataque final
                    self._reducir_atributos()
                    return self.estado_ataque_final
                else:
                    text_speed(f"{clanes[elegir_clan]} doesn't even exist!")
            except ValueError:
                text_speed("Please, select by number")


                
    def _atacar_desesperado_clan_aleatorio(self, clanes_filtrado):
        clan_random = random.choice(clanes_filtrado) # * Selección del clan de manera aleatoria *
        clan = clan_random.miembros
        for miembro in clan:
            self.realizar_ataque(miembro, self.ataque_desesperado, 1)
            text_speed(f"\n{miembro.nombre} of the clan {clan_random.nombre} has been attacked with {self.ataque_desesperado} of the {self.titulo} {self.nombre} !\n")
            text_speed(f"-Strenght: {miembro.fuerza}\n-Life Points: {miembro.puntos_vida}\n-Defense: {miembro.defensa}\n-Attack: {miembro.ataque}\n")

        text_speed(f"I've taken my choice randomly and I decide to attack {Fore.MAGENTA} {clan_random.nombre} {Style.RESET_ALL}")
        text_speed(f"The {self.titulo} {self.nombre} has casted the definitive attack {self.ataque_desesperado} and now the {self.titulo} is exhausted...")
        self._reducir_atributos()

    def _seleccionar_personaje_aleatorio(self,lst_personajes):
        # con esta variable calculo la cantidad de personajer que hay en la lista_personajes
        cantidad_aleatoria_objetivo = random.randint(1,len(lst_personajes))
        # toma la cantidad arrojada en el random y lo guarta en la variable cantidad_aleatoria_objetivo
        objetivos_aleatorio = random.sample(lst_personajes,cantidad_aleatoria_objetivo)

        for objetivo in objetivos_aleatorio:
            self.realizar_ataque(objetivo,self.ataque_desesperado,1)
            text_speed(f"\n{objetivo.nombre} of the clan {objetivo.clan} has been attacked with {self.ataque_desesperado} of the {self.titulo} {self.nombre} !\n  ")
            text_speed(f"-Strenght: {objetivo.fuerza}\n-Life points: {objetivo.puntos_vida}\n-Defense: {objetivo.defensa}\n-Attack: {objetivo.ataque}\n")
        
        text_speed(f"I have randomly attacked a number of {cantidad_aleatoria_objetivo}")
        self._reducir_atributos()


    
    def _reducir_atributos(self):
        self.estado_ataque_final = True
        self.fuerza = self.fuerza_original // 2
        self.puntos_vida //= 2
        self.defensa //= 2
        self.ataque = self.ataque_original // 2
        text_speed(f"The {self.titulo} {self.nombre} has casted the definitive attack {self.ataque_desesperado} and now the {self.titulo} is exhausted...")
        text_speed(f"The {self.titulo} {self.nombre} has decreased his/her life by half...")
        text_speed(f"-Strength: {self.fuerza}\n-Life Points: {self.puntos_vida}\n-Defense: {self.defensa}\n-Attack: {self.ataque}")
#***********************************************************************


if __name__ == "__main__":
 pass
