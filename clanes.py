# Definición de la clase Miembro para probar si esta bien
class Miembro:
    def __init__(self, nombre, titulo, fuerza, puntos_vida, defensa, ataque):
        self.nombre = nombre
        self.titulo = titulo
        self.fuerza = fuerza
        self.puntos_vida = puntos_vida
        self.defensa = defensa
        self.ataque = ataque
        
    def __repr__(self):
        return f"{self.titulo} {self.nombre}"


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
        print(f"{cantidad} Archers --> Strength({fuerza}), Life({vida}) Defense({defensa}) strike force({ataque})")
        cantidad, fuerza, vida, defensa, ataque = self.info_miembros("Warrior")   
        print(f"{cantidad} Warrior --> Strength({fuerza}), Life({vida}) Defense({defensa}) strike force({ataque})")
        cantidad, fuerza, vida, defensa, ataque = self.info_miembros("Sorcerer")   
        print(f"{cantidad} Sorcerer --> Strength({fuerza}), Life({vida}) Defense({defensa}) strike force({ataque})")
        print()
        cantidad, fuerza, vida, defensa, ataque = self.info_miembros("Founder")
        print(f"Clan {self.nombre} statistics") 
        print(f"Founder {self.fundador} | Strength({fuerzaClan}), Life({vidaClan}) Defense({defensaClan}) strike force({ataqueClan})")
            

# Función que verifica que estan los fundadores en los clanes
def verificar_fundadores(lista_clanes):
    for clan in lista_clanes:
        # retificar si el fundador está en la lista de miembros
        if not any(miembro.titulo == "Founder" for miembro in clan.miembros):
            print(f"En el clan {clan.nombre}, el fundador ha muerto. Tu destino está en las crueles manos de un asesino.")
        else:
            print(f"El clan {clan.nombre} aún tiene a su fundador, {clan.fundador}, en sus filas.")

# código de prueba
if __name__ == "__main__":
    # Creación de miembros de ejemplo
    fundador1 = Miembro("Fundador1", "Founder", 100, 1000, 200, 300)
    fundador2 = Miembro("Fundador2", "Founder", 150, 1200, 250, 350)
    miembro1 = Miembro("Miembro1", "Warrior", 80, 500, 150, 200)
    miembro2 = Miembro("Miembro2", "Archer", 70, 400, 100, 180)

    # se crean los clanes de prueba
    clan_con_fundador = Clan("Clan Con Fundador", fundador1)
    clan_con_fundador.agregar_miembro(miembro1)

    clan_sin_fundador = Clan("Clan Sin Fundador", fundador2)
    clan_sin_fundador.remover_miembro(fundador2)  # Remueve el fundador para simular su ausencia
    clan_sin_fundador.agregar_miembro(miembro2)

    # realizo una lista de clanes para retificar
    lista_clanes = [clan_con_fundador, clan_sin_fundador]

    # llamo a el metodo para probar
    verificar_fundadores(lista_clanes)