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
        
    def remover_miembro(self, miembro):
        self.miembros.remove(miembro)
        self.cantidadMiembros -= 1
        
        
    #metodo para calcular la fuerza de los miembros por categoria
    def info_miembros(self, titulo):
        cantidad = 0
        fuerza, vida, defensa, ataque = 0, 0, 0, 0
        for miembro in self.miembros:
            if miembro.titulo == titulo:
                cantidad += 1
                fuerza += miembro.fuerza
                vida += miembro.puntos_vida
                defensa += miembro.defensa
                ataque += miembro.ataque
        return cantidad, fuerza, vida, defensa, ataque
        
    def listar_miembros(self):
        fuerzaClan, vidaClan, defensaClan, ataqueClan = 0, 0, 0, 0
        print()
        print("*** *** *** *** ***")
        print(f"The clan {self.nombre} has {self.cantidadMiembros} members")
        for miembro in self.miembros:
            print(miembro)
            fuerzaClan += miembro.fuerza
            vidaClan += miembro.puntos_vida
            defensaClan += miembro.defensa
            ataqueClan += miembro.ataque
        cantidad, fuerza, vida, defensa, ataque = self.info_miembros("Archer")   
        print(f"{cantidad} Archers --> Strength({fuerza}), Life({vida}) Defense({defensa}) strike force({ataque})")
        cantidad, fuerza, vida, defensa, ataque = self.info_miembros("Warrior")   
        print(f"{cantidad} Warrior --> Strength({fuerza}), Life({vida}) Defense({defensa}) strike force({ataque})")
        cantidad, fuerza, vida, defensa, ataque = self.info_miembros("Sorcerer")   
        print(f"{cantidad} Sorcerer --> Strength({fuerza}), Life({vida}) Defense({defensa}) strike force({ataque})")
        print()
        cantidad, fuerza, vida, defensa, ataque = self.info_miembros("Founder")
        print(f"Clan {self.nombre} statistics") 
        print(f"Founder {self.fundador} | Strength({fuerzaClan}), Life({vidaClan}) Defense({defensaClan}) strike force({ataqueClan})")
            

#***********************************************************************

if __name__=="__main__":
    pass