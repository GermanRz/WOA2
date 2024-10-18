
class Personaje:
    def __init__(self, nombre, titulo, clan = None):
        self.nombre = nombre
        self.titulo = titulo
        #self.slot_pocion = slot_pocion = []
        self.clan = clan

    def asignar_clan(self, clan):
        self.clan = clan

    def realizar_ataque(self, objetivo):
        f"¡{self.nombre} made an attack!"
        damage = ((self.fuerza + self.ataque) / ((self.vida_original-self.puntos_vida) + self.vida_original)) / 10
        objetivo.recibir_ataque(damage)

    def recibir_ataque(self, damage):
        f"¡{self.nombre} has been injured!"
        factor_damage = (self.defensa * damage) / 100
        self.fuerza = round(self.fuerza / (factor_damage + 1))
        self.puntos_vida = round(self.puntos_vida / (factor_damage + 1))
        self.defensa = round(self.defensa / (factor_damage + 1))
        self.ataque = round(self.ataque / (factor_damage + 1))

        if self.puntos_vida > 0:
            print(f"¡{self.nombre} got wounded!. Remaining life points = {self.puntos_vida}")
        else:
            print(f"The player {self.nombre}({self.titulo}). left this world...")

    def __str__(self):
        return (f"{self.titulo}: {self.nombre}\n"
                f"Strength: {self.fuerza}, Life points: {self.puntos_vida}, "
                f"Defense: {self.defensa}, Attack: {self.ataque}, "
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
    def __init__(self, nombre, titulo = "Wizard"):
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

#***********************************************************************

class Fundador(Mago):
    def __init__(self, nombre):
        super().__init__(nombre, "Founder")
        self.fuerza = 100
        self.puntos_vida = 110
        self.defensa = 110
        self.ataque = 110
        self.vida_original = self.puntos_vida
        print(f"¡{self.nombre} Founded a clan!.")
        
#***********************************************************************

if __name__=="__main__":
    pass