from ei.nodos import NodoABin
from random import random
from recorridos2 import pre_orden, in_orden, post_orden

class ABin:
    def __init__(self):
        self.raiz = None

    def es_vacia(self):
        if self.raiz is None:
            return True
        return False

    def __agregar(self, sub_raiz, nueva_clave):
        if sub_raiz is None:
            sub_raiz = NodoABin(nueva_clave)
        elif random() <= 0.5:
            # crear un nuevo enlace o nodo por la izq
            por_izq = self.__agregar(sub_raiz.izq, nueva_clave)
            sub_raiz.izq = por_izq
        else:
            por_der = self.__agregar(sub_raiz.der, nueva_clave)
            sub_raiz.der = por_der
        return sub_raiz

    def agregar(self, nueva_clave):
        self.raiz = self.__agregar(self.raiz, nueva_clave)

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
    arb = ABin()
    arb.agregar(10)
    arb.agregar(20)
    arb.agregar(30)
    arb.agregar(40)
    arb.agregar(50)
    arb.buscar(50)
    print('Pre-Orden')
    pre_orden(arb)
    print('In-Orden')
    in_orden(arb)
    print('Post-Orden')
    post_orden(arb)
