class Carti:
    def __init__(self, nombre, edad, year):
        self.nombre = nombre
        self.edad = edad
        self.year = year

    def cantar(self):
        print(f"{self.nombre} canta : HXMICIDE HXMICIDE HXMICIDE! ")


# INSTANCIA
CartiCanta = Carti(nombre="Carti", edad=27, year=2024)
# llamar al metodo
CartiCanta.cantar()
