import random
from WOA2 import text_speed
from WOA2 import lista_personajes

class Personaje:
    def __init__(self, nombre, titulo, clan = None):
        self.nombre = nombre
        self.titulo = titulo
        self.clan = clan

    def asignar_clan(self, clan):
        self.clan = clan

    def realizar_ataque(self, objetivo):
        f"{self.nombre} has carried out an attack!"
        damage = ((self.fuerza + self.ataque) / ((self.vida_original-self.puntos_vida) + self.vida_original)) / 10
        objetivo.recibir_ataque(damage)

    def recibir_ataque(self, damage):
        f"{self.nombre}has received damage!"
        factor_damage = (self.defensa * damage) / 100
        self.fuerza = round(self.fuerza / (factor_damage + 1))
        self.puntos_vida = round(self.puntos_vida / (factor_damage + 1))
        self.defensa = round(self.defensa / (factor_damage + 1))
        self.ataque = round(self.ataque / (factor_damage + 1))

        if self.puntos_vida > 0:
            print(f"{self.nombre} has received an attack hit points = {self.puntos_vida}")
        else:
            print(f"The {self.titulo} {self.nombre} has died")
    
    # APLICANDO EFECTO DE ATAQUE FLECHA VENENOSA AL OBJETIVO
    
    def recibir_venenoso(self,damage, objetivo):
        print(f"{objetivo.nombre} ha recibido daño!")
        factor_damage = round(objetivo.defensa * damage) / 100 +1
        objetivo.fuerza = int(round( objetivo.fuerza + self.fuerza) / (factor_damage + 1))
        objetivo.puntos_vida = int(round(objetivo.puntos_vida  + self.ataque) / (factor_damage + 1))
        objetivo.defensa = int(round(objetivo.defensa + self.ataque) / (factor_damage + 1))
        objetivo.ataque = int(round(objetivo.defensa + self.ataque) / (factor_damage + 1))
    
     # FIN

     # APLICANDO EFECTO DEL VENENO AL OBJETIVO QUITANDO DE A 1 PUNTO DE VIDA
    
    def restar_punto_vida(self):
        if self.puntos_vida != 0:
            self.puntos_vida -= 1
        if self.puntos_vida > 0:
         print("estas bajo el ataque de flecha venenosa ")
        if   self.puntos_vida == 0:
            print(f"{self.nombre} ha muerto")
      
    
       #FIN


    def __str__(self):
        return (f"{self.titulo}: {self.nombre}\n"
                f"strength: {self.fuerza}, Life Points: {self.puntos_vida}, "
                f"Defense: {self.defensa}, attack: {self.ataque}, "
                f"Clan: {self.clan}")
        
#***********************************************************************

class Guerrero(Personaje):
    def __init__(self, nombre, titulo = "Warrior"):
        super().__init__(nombre, titulo)
        self.fuerza = 90
        self.puntos_vida = 100
        self.defensa = 90
        self.ataque = 100
        self.vida_original = self.puntos_vida
        
#***********************************************************************

class Mago(Personaje):
    def __init__(self, nombre, titulo = "Sorcerer"):
        super().__init__(nombre, titulo)
        self.fuerza = 80
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 90
        self.vida_original = self.puntos_vida

#***********************************************************************

class Arquero(Personaje):
    def __init__(self, nombre, titulo = "Archer"):
        super().__init__(nombre, titulo)
        self.fuerza = 95
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 120
        self.vida_original = self.puntos_vida
    
    def flecha_venenosa(self, objetivo ):
        damage = ((self.fuerza + self.ataque) / ((self.vida_original - self.puntos_vida) + self.vida_original)) / 10
        objetivo.recibir_venenoso( damage,objetivo)
        print(f"{self.nombre} ha disparado una flecha venenosa a {objetivo.nombre}!")
    
    def flecha_curativa(self, objetivo):
        
        curacion = round(self.vida_original * 0.01)  
        objetivo.puntos_vida += curacion

        # Asegurarnos de que no supere los puntos de vida originales
        if objetivo.puntos_vida > objetivo.vida_original:
            objetivo.puntos_vida = objetivo.vida_original

        print(f"{self.nombre} ha disparado una flecha curativa a {objetivo.nombre} y le ha restaurado {curacion} punto de vida!")


#***********************************************************************

class Fundador(Mago):
    def __init__(self, nombre):
        super().__init__(nombre, "Founder")
        self.fuerza = 100
        self.puntos_vida = 110
        self.defensa = 110
        self.ataque = 110
        self.vida_original = self.puntos_vida
        self.slot_pociones = []
        text_speed(f"{self.nombre} has founded a clan.")
       
        
    def crear_pociones(self):
        cura_aleatoria = random.randint(10, 25)
        if len(self.slot_pociones) < 3:
            self.slot_pociones.append(cura_aleatoria)
            for pocion in self.slot_pociones:
                text_speed(f"{self.nombre} 🧙‍♂️ Potions: ({list(self.slot_pociones)} 🥤| Healing: {pocion} 💗)")
        else:
            text_speed(f"Oops! You can´t have more than 3 potions in your pockets 🥤! {list(self.slot_pociones)}")

    def conceder_curacion(self, lst_pjs, pj_receptor):
        for index, pj in enumerate(lst_pjs):
            print(f"{index+1} | {pj.titulo} {pj.nombre}")
        opc = int(input(f"Select number of the character that you wanna heal with the pocion: ")) - 1
        if 0 <= opc < len(lst_pjs):#VERIFICA QUE LA OPC ESTÉ EN LA LISTA
            pj_receptor = lst_pjs[opc]#EN LA POSICIÓN QUE SE ELIGIÓ EN LA OPC
            self.pj_receptor = pj_receptor#PJ COMO UN OBJETO
            curacion = self.slot_pociones.pop()#SACA LA POCIÓN DEL BOLSILLO
            text_speed(f"{self.nombre} has using a healing potion 🥤! in {self.pj_receptor.nombre}")
            pj_receptor.fuerza += curacion
            pj_receptor.puntos_vida += curacion
            pj_receptor.defensa += curacion
            pj_receptor.ataque += curacion
        else:
            text_speed(f"That character does´nt even exist!")
        return pj_receptor
        
        
#***********************************************************************

if __name__=="__main__":
    pass