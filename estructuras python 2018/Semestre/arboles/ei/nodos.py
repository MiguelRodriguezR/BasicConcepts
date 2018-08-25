class NodoABin:

    def __init__(self, clave, izq=None, der=None):
        self.clave = clave
        self.izq = izq
        self.der = der

    def tiene_hijos(self):
        if self.izq is not None or self.der is not None:
            return True
        else:
            return False
