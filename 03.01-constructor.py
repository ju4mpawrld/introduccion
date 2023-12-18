class Juanito:  # defino mi clase
    def __init__(
        self, nombre, edad, altura
    ):  # definir init, que es un método especial  que se llama cuando creas una nueva instancia de la clase.
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def hablar(self):  # defino el metodo
        print(f"{self.nombre} dice : soy como messi! ")


# Crear una instancia de la clase Juanito
JuanitoHabla = Juanito(nombre="Juanito", edad=29, altura=181)
# Llamar al método habla()
JuanitoHabla.hablar()
