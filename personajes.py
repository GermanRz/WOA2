
class Personaje:
    def __init__(self, nombre, titulo, clan = None):
        self.nombre = nombre
        self.titulo = titulo
        self.clan = clan
        self.lista_protectores = []

#******************
    def listar_protectores (self):
        for protector in self.lista_protectores:
            print (protector)
#******************

    def asignar_clan(self, clan):
        self.clan = clan

    def realizar_ataque(self):
        f"{self.nombre} ha realizado un ataque!"
        damage = ((self.fuerza + self.ataque) / ((self.vida_original-self.puntos_vida) + self.vida_original)) / 10
        #Se retiro el "recibir_ataque(damage)" 

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

#***********************************************************************

class Guerrero(Personaje):
    def __init__(self, nombre, titulo = "Guerrero"):
        super().__init__(nombre, titulo)
        self.fuerza = 90
        self.puntos_vida = 100
        self.defensa = 90
        self.ataque = 100
        self.vida_original = self.puntos_vida
        self.lista_protegido = []
#******************
    def protegido (self, objetivo):
        objetivo.lista_protectores.append(self.nombre)
        print(f"El {self.titulo} | {self.nombre} va a proteger al {objetivo.titulo} | {objetivo.nombre}")
        #Se añaden a la lista de protectores el objetivo "atacado"
#******************
# # solo de guerrero
#     def listas_protegidos (self, protegido,lista_protectores, lista_protegido):
#         if protegido.self.puntos_vida > 0 :
#             protegido.lista_protegido.append(self.nombre)
#         else :
#             lista_protegido.remove(protegido)
#             lista_protectores.remove(protegido)
#******************
    def proteger_df (self, lista_protectores, objetivo, damage, lista_protegido, protegido):
        if  len(lista_protectores) > 0:
            sacar_protector = lista_protectores.pop(0)  # Obtener el primer protector
            sacar_protector.recibir_ataque(damage)
            print(f"{sacar_protector} te ha protegido y quedo con: {self.puntos_vida}")
        else:
            objetivo.recibir_ataque(damage)

        if protegido.self.puntos_vida > 0 :
            protegido.lista_protegido.append(self.nombre)
        else :
            lista_protegido.remove(protegido)
            lista_protectores.remove(protegido)
            #Se trajo "recibir_ataque(damage)" del "def realizar_ataque(self)" para poder comparar a quien hacerle el daño

#******************
    def proteger_df(self, lista_protectores, objetivo, damage):
        if  len(lista_protectores) > 0:
            while lista_protectores:  # Mientras haya protectores
                protector = lista_protectores.pop(0)  # Obtener el primer protector
                if protector.puntos_vida > 0:  # Si el protector está vivo
                    protector.recibir_ataque(damage)  # El protector recibe el daño
                    print(f"{protector.nombre} te ha protegido y quedó con: {protector.puntos_vida} puntos de vida.")
                    if protector.puntos_vida <= 0:
                        lista_protectores.pop(0)  # Si el protector murió, se elimina de la lista
                    return  # Salir de la función porque el daño ya fue absorbido
                else:
                    lista_protectores.pop(0)  # Si el protector está muerto, lo eliminamos de la lista
            # Si no quedan protectores o están todos muertos, el objetivo recibe el daño
            objetivo.recibir_ataque(damage)
            print(f"{objetivo.nombre} ha recibido el ataque directamente.")
        # Si no hay protectores el objetivo recibe el daño
        objetivo.recibir_ataque(damage)
        print(f"{objetivo.nombre} ha recibido un ataque. Puntos de vida: {self.puntos_vida}")
#******************

#***********************************************************************

class Mago(Personaje):
    def __init__(self, nombre, titulo = "Mago"):
        super().__init__(nombre, titulo)
        self.fuerza = 80
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 90
        self.vida_original = self.puntos_vida

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

if __name__=="__main__":
    pass

    f1 = Fundador ("F1")
    g1 = Guerrero ("G1")
    g2 = Guerrero ("G2")
    g3 = Guerrero ("G3")
    
    g1.protegido (f1)
    g2.protegido(f1)
    g1.protegido(f1)

    g1.proteger_df (f1)
    g2.proteger_df(f1)
    g1.proteger_df(f1)

    f1.listar_protectores()
