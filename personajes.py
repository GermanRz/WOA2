import random
from WOA2 import text_speed
from WOA2 import lista_personajes
import colorama
from colorama import Fore, Style

colorama.init()#esto es necesario para iniciar la clase colorama


from resources import text_speed

class Personaje:
    def __init__(self, nombre, titulo, clan = None):
        self.nombre = nombre
        self.titulo = titulo
        self.clan = clan
        self.lst_protectores = []

    def asignar_clan(self, clan):
        self.clan = clan
        
    '''
    se agregan dos parametros acicionales
    txtAtaque : descripcion del ataque recibido (flecha venenosa, ataque meteorito, etc...)  default = " "
    intensidadAtaque: valor entero de la intensidad del ataque.   default = 5
    '''
    def realizar_ataque(self, objetivo, txtAtaque=" ", intensidadAtaque=5):
        # verificar si el objetivo tiene protectores
        if len(objetivo.lst_protectores)>0 and txtAtaque!="flecha certera":
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
        return estado


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

            print(f"The {self.titulo} {self.nombre} has died")
            #si el titulo del objetivo fallecido es un guerrero se debe verificar su lista de protegidos para eliminarse de cada uno de ellos como protector
            if self.titulo == "Warrior":
                if len(self.lst_protegidos)>0:
                    for protegido in self.lst_protegidos:
                        protegido.lst_protectores.remove(self)
            return 0 #death
    
     # APLICANDO EFECTO DEL VENENO AL OBJETIVO QUITANDO DE A 1 PUNTO DE VIDA
    
    def restar_punto_vida(self):
        if self.puntos_vida != 0:
            self.puntos_vida -= 1
        if self.puntos_vida > 0:
         print("estas bajo el ataque de flecha venenosa ")
        if   self.puntos_vida == 0:
            print(f"{self.nombre} ha muerto")
      
    
    
    #FIN
    def regeneracion_mana(self):
        regeneracion = random.randint(5, 25)
        self.barra_mana += regeneracion
        if self.barra_mana > 100:
            self.barra_mana = 100
        print(f"{self.nombre} ha regenerado {regeneracion} de mana. Barra de mana: {self.barra_mana}")
        

    def usar_hechizo(self, costo_mana):
        if self.barra_mana >= costo_mana:
            self.barra_mana -= costo_mana
            print(f"{self.nombre} ha usado un hechizo. Costo de mana: {costo_mana}. Barra de mana: {self.barra_mana}")
        else:
            print(f"{self.nombre} no tiene suficiente mana para usar el hechizo.")

    def __str__(self):
        return (super().__str__() + 
                f", Barra de Mana: {self.barra_mana}")

    def ataque_doble(self, objetivo):
        if self.barra_mana == 100:
            print(f"{self.nombre} launches double attack {objetivo.nombre}!")
            estado_objetivo = self.realizar_ataque(objetivo,"double attack",10)

    def protector(self, objetivo):
        objetivo.lst_protectores.append(self)
        # for protector in objetivo.lst_protectores:
        #     print(protector)
        # input("LISTA DE PROTECTORES")

    def protector(self, objetivo):
        objetivo.lst_protectores.append(self)
        # for protector in objetivo.lst_protectores:
        #     print(protector)
        # input("LISTA DE PROTECTORES")


    def __str__(self):
        return (f"{self.titulo}: {self.nombre}\n"
                f"strength: {self.fuerza}, Life Points: {self.puntos_vida}, "
                f"Defense: {self.defensa}, attack: {self.ataque}, "
                f"Clan: {self.clan}")
        
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
    def __init__(self, nombre, titulo = "Sorcerer", color = Fore.GREEN):
        super().__init__(nombre, titulo)
        self.fuerza = 80
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 90
        self.color = color
        self.bolsillo_pociones_mago = []
        # Guardamos los valores máximos/iniciales de cada atributo
        self.fuerza_original = self.fuerza
        self.vida_original = self.puntos_vida        
        self.defensa_original = self.defensa
        self.ataque_original = self.ataque
        self.barra_mana = 50 
    def __str__(self):
        return (f"{self.titulo}: {self.nombre}\n"
                f"Strength: {self.fuerza}, Life Points: {self.puntos_vida}, "
                f"Defense: {self.defensa}, Attack: {self.ataque}, "
                f"Clan: {self.clan}, Mana Bar: {self.barra_mana}")
        

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
    
    def flecha_venenosa(self, objetivo ):
        self.realizar_ataque(objetivo,"poision arrow", 3)
    
    def flecha_curativa(self, objetivo):
        
        curacion = round(self.vida_original * 0.01)  
        objetivo.puntos_vida += curacion

        # Asegurarnos de que no supere los puntos de vida originales
        if objetivo.puntos_vida > objetivo.vida_original:
            objetivo.puntos_vida = objetivo.vida_original

        print(f"{self.nombre} ha disparado una flecha curativa a {objetivo.nombre} y le ha restaurado {curacion} punto de vida!")


#***********************************************************************

class Fundador(Mago):
    cont_pociones_fundador = 0
    def __init__(self, nombre):
        super().__init__(nombre, "Founder")
        self.fuerza = 40 #100
        self.puntos_vida = 40 #110
        self.defensa = 40 #110
        self.ataque = 110
        # Guardamos los valores máximos/iniciales de cada atributo
        self.fuerza_original = self.fuerza
        self.vida_original = self.puntos_vida        
        self.defensa_original = self.defensa
        self.ataque_original = self.ataque
        self.bolsillo_pociones_fundador = []
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
            text_speed(f"That character does´nt even exist!")
            input("Press ENTER to continue! ")
        return pj_receptor
        
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
    
    def fundador_ataque_desesperado(self, clanes): # Ataque desesperado
        text_speed(f"...Y'all will gonna suffer the fury of our clan {self.clan}, ...{Fore.RED} The fury... of the fallens! {Style.RESET_ALL}")
        text_speed(f"The {self.titulo} {self.nombre} has gonna begin the final attack!")
        text_speed(f"{Fore.RED} {self.ataque_desesperado} {Style.RESET_ALL}\n", 0.07)
        
#***********************************************************************

if __name__=="__main__":
    fundador = Fundador("f")
    arquero1 = Arquero("a1")
    guerrero1 = Guerrero("g1")
    guerrero2 = Guerrero("g2")
    mago1 = Mago("m1")
    
    arquero1.flecha_venenosa(guerrero1)
    print(guerrero1)
    print()
    arquero1.realizar_ataque(guerrero2)
    print(guerrero2)    
    
    
    arquero2 = Arquero("a2")
    arquero3 = Arquero("a3")
    arquero4 = Arquero("a4")
    arquero5 = Arquero("a5")

    # arquero1.flecha_venenosa(fundador)
    # print(fundador)
    # arquero2.flecha_venenosa(arquero5)
    # print(arquero5)
    # arquero5.flecha_venenosa(arquero5)
    # print(arquero5)
    # arquero4.flecha_venenosa(arquero5)
    # print(arquero5)
    # arquero4.flecha_venenosa(fundador)
    # print(fundador)
    # arquero4.flecha_venenosa(fundador)
    # print(fundador)
    # arquero4.flecha_venenosa(fundador)
    # print(fundador)
    pass