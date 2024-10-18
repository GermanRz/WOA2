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
        
    def ataque_meteoro (self,objetivo):
        if self.contHechizo == 0:
            COSTO_ATAQUE_METEORO = 100
            if self.barra_mana >= COSTO_ATAQUE_METEORO:
                damage_meteor = round((self.fuerza + self.ataque) / ((self.vida_original - self.puntos_vida) + self.vida_original)) / 2
                print(f"{self.nombre} lanza meteoritos y causa {damage_meteor} de daño.")
                self.barra_mana -= COSTO_ATAQUE_METEORO  # Restar maná
                objetivo.recibir_ataque(damage_meteor)
                self.contHechizo = 2
            else:
                print(f"{self.nombre} no tiene suficiente mana para lanzar meteoritos.")
        else:
            print(f"{self.nombre} no puede realizar este ataque. {self.contHechizo} turnos restantes.")
            self.contHechizo -= 1
         
    def ataque_doble(self, objetivo):
        COSTO_ATAQUE_DOBLE = 100
        if self.barra_mana >= COSTO_ATAQUE_DOBLE:
            print(f"{self.nombre} lanza Ataque Doble a {objetivo.nombre}!")
            damage_doble = round (((self.fuerza + self.ataque) / ((self.vida_original - self.puntos_vida) + self.vida_original)) / 4)
            self.barra_mana -= COSTO_ATAQUE_DOBLE # Restar maná
            objetivo.recibir_ataque(damage_doble) 
            print(f"{objetivo.nombre} recibe un daño de {damage_doble}!")
        else:
            print(f"{self.nombre} no tiene suficiente mana para realizar el Ataque Doble.")

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

    def __str__(self):
        return (f"{self.titulo}: {self.nombre}\n"
                f"strength: {self.fuerza}, Life Points: {self.puntos_vida}, "
                f"Defense: {self.defensa}, attack: {self.ataque}, "
                f"Clan: {self.clan}")
        
    def recibir_meteoro(self,damage_meteor):
        f"El {self.titulo}{self.nombre} ha recibido el ataque meteorito"
        factor_damage_meteor = (self.defensa * damage_meteor) / 100
        self.fuerza = round(self.fuerza / (factor_damage_meteor + 1))
        self.puntos_vida = round(self.puntos_vida / (factor_damage_meteor + 1))
        self.defensa = round(self.defensa / (factor_damage_meteor + 1))
        self.ataque = round(self.ataque / (factor_damage_meteor + 1))
        0
        if self.puntos_vida > 0:
            print(f"{self.nombre} ha recibido un ataque puntos de vida = {self.puntos_vida}")
        else:
            print(f"El {self.titulo} {self.nombre} ha muerto")
            
    def recibir_ataque_doble(self,damage_doble):
        f"El {self.titulo}{self.nombre} ha recibido el ataque meteorito"
        damage_doble = (self.defensa * damage_doble) / 100
        self.fuerza = round(self.fuerza / (damage_doble + 1))
        self.puntos_vida = round(self.puntos_vida / (damage_doble + 1))
        self.defensa = round(self.defensa / (damage_doble + 1))
        self.ataque = round(self.ataque / (damage_doble + 1))
        
        if self.puntos_vida > 0:
            print(f"{self.nombre} ha recibido un ataque puntos de vida = {self.puntos_vida}")
        else:
            print(f"El {self.titulo} {self.nombre} ha muerto")
            
        
    
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
        self.barra_mana = 50
        self.vida_original = self.puntos_vida
        self.contHechizo = 0
        
    def regeneracion(self):
        regeneracion = random.randint(5, 25)
        self.barra_mana += regeneracion
        if self.barra_mana > 100:
            self.barra_mana = 100
            print(f"{self.nombre} ha regenerado {regeneracion} de mana. Barra de mana: {self.barra_mana}")

    def __str__(self):
        return (super().__str__() +  # Llama al método __str__ de la clase base
                f", Barra de Mana: {self.barra_mana}")
        
#***********************************************************************

class Arquero(Personaje):
    def __init__(self, nombre, titulo = "Archer"):
        super().__init__(nombre, titulo)
        self.fuerza = 95
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 120
        self.vida_original = self.puntos_vida

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

if __name__ == "__main__":
        mago = Mago("vera") 
        mago.barra_mana = 100
        fundador = Fundador("cristian")
        fundador2 = Fundador("jensen")
        print(fundador)
        mago.ataque_meteoro(fundador)
        print(fundador)
        print(mago)