
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
        
    def listar_miembros(self):
        print()
        print("*** *** *** *** ***")
        print(f"The clan {self.nombre}, has an amount of {self.cantidadMiembros} members")
        print(f"The clan {self.nombre} has {self.cantidadMiembros} members")
        for miembro in self.miembros:
            print(miembro)

#***********************************************************************

if __name__=="__main__":
    pass