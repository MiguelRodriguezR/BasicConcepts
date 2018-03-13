from random import random
from recorridos import pre_orden, in_orden, post_orden


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


class ArbolBin:

    def __init__(self):
        self.raiz = None

    def insertar(self, nueva_clave):
        self.raiz = self.__insertar(self.raiz, nueva_clave)

    def __insertar(self, sub_raiz, nueva_clave):
        if sub_raiz is None:
            sub_raiz = NodoABin(nueva_clave)
        elif random() <= 0.5:
            # crear un nuevo enlace o nodo por la izq
            por_izq = self.__insertar(sub_raiz.izq, nueva_clave)
            sub_raiz.izq = por_izq
        else:
            por_der = self.__insertar(sub_raiz.der, nueva_clave)
            sub_raiz.der = por_der
        return sub_raiz

    def buscar(self, clave_buscar):
        return self.__buscar(self.raiz, clave_buscar)

    def __buscar(self, sub_raiz, clave_buscar):
        if sub_raiz is not None:
            print(str(sub_raiz.clave )+ '<-->' + str(clave_buscar))
            if (sub_raiz.clave == clave_buscar):
                return True
            else:
                if self.__buscar(sub_raiz.izq, clave_buscar):
                    return True
                elif self.__buscar(sub_raiz.der, clave_buscar):
                    return True
                return False
        else:
            return False


if __name__ == '__main__':
    arb = ArbolBin()
    arb.insertar(10)
    arb.insertar(20)
    arb.insertar(30)
    arb.insertar(40)
    arb.insertar(50)
    arb.buscar(50)
    print('Pre-Orden')
    pre_orden(arb)
    print('In-Orden')
    in_orden(arb)
    print('Post-Orden')
    post_orden(arb)
