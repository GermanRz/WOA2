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
    self.fuerza = 100
        self.puntos_vida = 110
        self.defensa = 110
        self.ataque = 110
    '''
    def realizar_ataque(self, objetivo, txtAtaque=" ", intensidadAtaque=5):
        # verificar si el objetivo tiene protectores
        if len(objetivo.lst_protectores)>0 and txtAtaque!="accurate arrow":
            objetivo = objetivo.lst_protectores.pop(0)  #el nuevo objetivo es el primer protector

        print(f"{self.nombre} has carried out an attack!  {txtAtaque}")
        # 1. Calculamos el poder del ataque usando solo fuerza y ataque del atacante
        poder_ataque = (self.fuerza + self.ataque)
        #420
        
        # 2. Calculamos el poder de la defensa usando solo fuerza y defensa del objetivo
        poder_defensa = (objetivo.fuerza + objetivo.defensa)
        #220
        
        # 3. Calculamos la diferencia de poder
        diferencia_poder = poder_ataque - poder_defensa
        #200
        
        # 4. Calculamos el porcentaje de daño base
        if diferencia_poder > 0:
            # Si el ataque es más fuerte que la defensa
            factor_ataque = intensidadAtaque + (diferencia_poder * 0.5)  # 0.5% por cada punto de diferencia
            #diferencia_poder = 100
            #intensidadAtaque = 5
            #factor_ataque = 105
        else:
            # Si la defensa es más fuerte o igual que el ataque
            factor_ataque = intensidadAtaque  # Daño mínimo de intensidadAtaque%
        # 6. Calculamos el daño final
        damage = int((objetivo.vida_original * factor_ataque) / 100)
        #damage = 105
        estado=objetivo.recibir_ataque(damage)
        return estado


    def recibir_ataque(self, damage):
        # print("damage :", damage)
        self.puntos_vida = max(0, self.puntos_vida - damage)
        #calculamos el porcentaje de vida resultante
        porcentaje_vida = self.puntos_vida / self.vida_original
        # print(f"{porcentaje_vida} = {self.puntos_vida} / {self.vida_original}")
        # Los atributos se disminuyen proporcionalmente a la vida perdida
        self.fuerza = max(1,int(self.fuerza_original * porcentaje_vida))#-50
        self.defensa = max(1,int(self.defensa_original * porcentaje_vida))#-55
        self.ataque = max(1,int(self.ataque_original * porcentaje_vida))#-55
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
    def __init__(self, nombre, titulo = "Sorcerer", color = Fore.GREEN):
        super().__init__(nombre, titulo)
        self.fuerza = 80
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 90
        self.color = color
        # Guardamos los valores máximos/iniciales de cada atributo
        self.fuerza_original = self.fuerza
        self.vida_original = self.puntos_vida        
        self.defensa_original = self.defensa
        self.ataque_original = self.ataque

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
        status= self.realizar_ataque(objetivo,"poision arrow", 3)
        return status
    
    def flecha_curativa(self, objetivo):
        
        curacion = round(self.vida_original * 0.01)  
        objetivo.puntos_vida += curacion

        # Asegurarnos de que no supere los puntos de vida originales
        if objetivo.puntos_vida > objetivo.vida_original:
            objetivo.puntos_vida = objetivo.vida_original

        print(f"{self.nombre} ha disparado una flecha curativa a {objetivo.nombre} y le ha restaurado {curacion} punto de vida!")

    def accurate_arrow(self, objetivo):
        status= self.realizar_ataque(objetivo, "accurate arrow", 4)
        return status

#***********************************************************************

class Fundador(Mago):
    cont_pociones = 0
    def __init__(self, nombre):
        super().__init__(nombre, "Founder")
        self.fuerza = 100
        self.puntos_vida = 110
        self.defensa = 110
        self.ataque = 110
        # Guardamos los valores máximos/iniciales de cada atributo
        self.fuerza_original = self.fuerza
        self.vida_original = self.puntos_vida        
        self.defensa_original = self.defensa
        self.ataque_original = self.ataque
        self.slot_pociones = []
        text_speed(f"{self.nombre} has founded a clan.")
        
    def crear_pociones(self):
        cura_aleatoria = random.randint(10, 25)
        if len(self.slot_pociones) < 3:
            self.slot_pociones.append(cura_aleatoria)
            self.cont_pociones += 1#Se aumenta el contador de las pociones
            for pocion in self.slot_pociones:
                text_speed(f"{self.nombre} 🧙‍♂️🧙‍♀️ Potions: ({self.cont_pociones} 🥤| Healing: {pocion} 💗)")
        else:
            text_speed(f"Oops! You can´t have more than 3 potions in your pockets 🥤! {list(self.cont_pociones)}")

    def conceder_curacion(self, lst_pjs, pj_receptor):
        for index, pj in enumerate(lst_pjs):
            print(f"{index+1} | {pj.titulo} {pj.nombre}")
        opc = int(input(f"Select number of the character that you wanna heal with the pocion: ")) - 1
        if 0 <= opc < len(lst_pjs):#VERIFICA QUE LA OPC ESTÉ EN LA LISTA
            pj_receptor = lst_pjs[opc]#EN LA POSICIÓN QUE SE ELIGIÓ EN LA OPC
            self.pj_receptor = pj_receptor#PJ COMO UN OBJETO
            curacion = self.slot_pociones.pop()#SACA LA POCIÓN DEL BOLSILLO
            self.cont_pociones -= 1
            text_speed(f"{self.nombre} has using a healing potion 🥤 in {self.pj_receptor.nombre}")
            pj_receptor.fuerza += curacion
            pj_receptor.puntos_vida += curacion
            pj_receptor.defensa += curacion
            pj_receptor.ataque += curacion
            input("Press ENTER to continue! ")
        else:
            text_speed(f"That character does´nt even exist!")
        return pj_receptor
        
        
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