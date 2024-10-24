
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
        print(f"{cantidad} Archers --> fuerza({fuerza}), vida({vida}) defensa({defensa}) ataque({ataque})")
        cantidad, fuerza, vida, defensa, ataque = self.info_miembros("Warrior")   
        print(f"{cantidad} Warrior --> fuerza({fuerza}), vida({vida}) defensa({defensa}) ataque({ataque})")        
        cantidad, fuerza, vida, defensa, ataque = self.info_miembros("Sorcerer")   
        print(f"{cantidad} Sorcerer --> fuerza({fuerza}), vida({vida}) defensa({defensa}) ataque({ataque})") 
        print()
        cantidad, fuerza, vida, defensa, ataque = self.info_miembros("Founder")  
        print(f"Founder {self.nombre} --> fuerza({fuerzaClan}), vida({vidaClan}) defensa({defensaClan}) ataque({ataqueClan})")  
            

#***********************************************************************

if __name__=="__main__":
    pass