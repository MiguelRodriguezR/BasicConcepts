class NodoLSE:

    def __init__(self, dato):
        self.dato = dato
        self.sig = None


class NodoLDE:

    def __init__(self, dato):
        self.dato = dato
        self.sig = None
        self.ant = None
    def __eq__(self,otro):
        if(self is not None and isinstance(otro,type(self)) and isinstance(otro.dato,type(self.dato)) ):
            return self.dato == otro.dato
        return False


"""
tarea1:
El metodo agregar tiene que devolver un valor boleano(true si se puede ,false
sino) type me verifica si es o no si es del mismo dato en validación.py

el metodo def posicionar (self,pos,nuevo_dato)
debe devolver un valor boleano,

"""
