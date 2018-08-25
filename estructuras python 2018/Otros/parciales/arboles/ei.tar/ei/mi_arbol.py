# Autores = [Jose Calpa - David Jaramillo]

from random import random
from mis_recorridos import pre_orden, in_orden


class NodoArbBin:

    def __init__(self, clave):

        self.clave = clave
        self.izq = None
        self.der = None

    def tiene_hijos(self):

        if (self.der is not None or self.izq is not None):

            return True

        else:
            return False


class ArbolBinario:

    def __init__(self):

        self.raiz = None
        self.can = 0

    def es_vacio(self):

        if (self.raiz is None):

            return True

        else:
            return False

    def insertar(self, nueva_clave):

        self.raiz = self.__insertar(self.raiz, nueva_clave)

    def __insertar(self, sub_raiz, nueva_clave):

        if (sub_raiz is None):

            sub_raiz = NodoArbBin(nueva_clave)

        # Por Izquierda
        elif (random() <= 0.5):

            sub_raiz.izq = self.__insertar(sub_raiz.izq, nueva_clave)

        # Por Derecha

        else:
            sub_raiz.der = self.__insertar(sub_raiz.der, nueva_clave)

        return sub_raiz

    def __len__(self):

        return (self.__numero_nodos(self.raiz))

    def __numero_nodos(self, sub_raiz):

        if (sub_raiz is None):
            return 0

        else:

            return(1 + self.__numero_nodos(sub_raiz.izq) + self.__nu
                   mero_nodos(sub_raiz.der))


"""
arbol = ArbolBinario()
arbol.insertar(7)
arbol.insertar(9)
arbol.insertar(5)
arbol.insertar(10)
arbol.insertar(20)
arbol.insertar(30)


#print (len(arbol))
pre_orden(arbol)
#in_orden (arbol)
"""
