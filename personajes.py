import random
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

if __name__ == "__main__":
        mago = Mago("vera") 
        mago.barra_mana = 100
        fundador = Fundador("cristian")
        fundador2 = Fundador("jensen")
        print(fundador)
        mago.ataque_meteoro(fundador)
        print(fundador)
        print(mago)