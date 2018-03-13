from arboles_bin_bus import ArbolBinBus
from recorridos import pre_orden


class Persona:

    def __init__(self, nom, edad):
        self.nombre = nom
        self.edad = edad

    def __str__(self):
        return (str(self.nombre) + ' : ' + str(self.edad))

    def __eq__(self, otra_persona):
        return (isinstance(otra_persona, Persona) and
                (self.nombre == otra_persona.nombre and
                self.edad == otra_persona.edad))

    def __lt__(self, otra_persona):
        # Menor que
        if isinstance(otra_persona, Persona):
            if self.nombre < otra_persona.nombre:
                return True
            elif (self.nombre == otra_persona.nombre and
                  self.edad < otra_persona.edad):
                return True
            return False
        raise TypeError("Tipos no compatibles")

    def __gt__(self, otra_persona):
        # Mayor que
        if isinstance(otra_persona, Persona):
            if self.nombre > otra_persona.nombre:
                return True
            elif (self.nombre == otra_persona.nombre and
                  self.edad > otra_persona.edad):
                return True
            return False
        raise TypeError("Tipos no compatibles")


if __name__ == "__main__":
    personal = ArbolBinBus()
    personal.insertar(Persona("Pedro", 20))
    personal.insertar(Persona("Carlos", 15))
    personal.insertar(Persona("Ken", 30))
    personal.insertar(Persona("Rosa", 25))
    print(personal.num_hojas())
    pre_orden(personal)
