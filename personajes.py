import random
import math
from resources import text_speed

class Personaje:
    def __init__(self, nombre, titulo, clan = None):
        self.nombre = nombre
        self.titulo = titulo
        self.clan = clan

    def asignar_clan(self, clan):
        self.clan = clan
        
    def realizar_ataque(self, objetivo):
        print(f"{self.nombre} has carried out an attack!")
        # 1. Calculamos el poder del ataque usando solo fuerza y ataque del atacante
        poder_ataque = (self.fuerza + self.ataque)
        
        # 2. Calculamos el poder de la defensa usando solo fuerza y defensa del objetivo
        poder_defensa = (objetivo.fuerza + objetivo.defensa)
        
        # 3. Calculamos la diferencia de poder
        diferencia_poder = poder_ataque - poder_defensa
        
        # 4. Calculamos el porcentaje de daño base
        if diferencia_poder > 0:
            # Si el ataque es más fuerte que la defensa
            factor_ataque = 5 + (diferencia_poder * 0.5)  # 0.5% por cada punto de diferencia
        else:
            # Si la defensa es más fuerte o igual que el ataque
            factor_ataque = 5  # Daño mínimo del 5%
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
            print(f"The {self.titulo} {self.nombre} has died")
            return 0 #death
                   


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
        # Guardamos los valores máximos/iniciales de cada atributo
        self.fuerza_original = self.fuerza
        self.vida_original = self.puntos_vida        
        self.defensa_original = self.defensa
        self.ataque_original = self.ataque
        
#***********************************************************************

class Mago(Personaje):
    def __init__(self, nombre, titulo = "Sorcerer"):
        super().__init__(nombre, titulo)
        self.fuerza = 80
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 90
        # Guardamos los valores máximos/iniciales de cada atributo
        self.fuerza_original = self.fuerza
        self.vida_original = self.puntos_vida        
        self.defensa_original = self.defensa
        self.ataque_original = self.ataque

#***********************************************************************

class Arquero(Personaje):
    def __init__(self, nombre, titulo = "Archer"):
        super().__init__(nombre, titulo)
        self.fuerza = 95
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 120
        # Guardamos los valores máximos/iniciales de cada atributo
        self.fuerza_original = self.fuerza
        self.vida_original = self.puntos_vida        
        self.defensa_original = self.defensa
        self.ataque_original = self.ataque

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
    # m1 = Mago("F1")
    f1 = Fundador("F1")
    # m2 = Mago("F2")
    f2 = Fundador("F2")
    g1 = Guerrero("g1")
    print()
    print()
    for i in range(1,10):
        g1.realizar_ataque(f2)
        print(f2)
    
    