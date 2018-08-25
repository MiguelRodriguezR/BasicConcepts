
# !/usr/bin/env python3
#
# Project:arbol binario
# File: arboles.py
# Authors: (Camila Quintero-Geraldin Fajardo)
# Date: 27.04.2016 15:42:25 COT
# Description:


from random import random
from recorridos import pre_orden, in_orden, post_orden


class NodoABin:

    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None

    def tiene_hijos(self):
        if self.izq or self.der:
            return True
        return False

    def __str__(self):
        return str(self.clave)


class ArbolBin:

    def __init__(self):
        self.raiz = None

    def es_vacio(self):
        if self.raiz is None:
            return True
        return False

    def insertar(self, nueva_clave):
        self.raiz = self.__insertar(self.raiz, nueva_clave)

    def __insertar(self, sub_arbol, nueva_clave):

        if (sub_arbol is None):
            sub_arbol = NodoABin(nueva_clave)
        elif random() <= 0.5:  # Me voy x la izq
            nodo_izq = self.__insertar(sub_arbol.izq, nueva_clave)
            sub_arbol.izq = nodo_izq
        else:
            sub_arbol.der = self.__insertar(sub_arbol.der, nueva_clave)
        return sub_arbol

    def buscar(self, clave_buscar):
        return self.__buscar(self.raiz, clave_buscar)

    def __buscar(self, sub_arbol, clave_buscar):
        if sub_arbol is not None:
            if sub_arbol.clave == clave_buscar:
                return sub_arbol.clave
            else:
                bus_izq = self.__buscar(sub_arbol.izq, clave_buscar)
                if bus_izq is not None:
                    return bus_izq
                bus_der = self.__buscar(sub_arbol.der, clave_buscar)
                if bus_der is not None:
                    return bus_der
        return None

    def __len__(self):
        return self.__número_nodos(self.raiz)

    def __número_nodos(self, sub_arbol):
        if sub_arbol:  # sub_arbol is not None
            return 1+self.__número_nodos(sub_arbol.izq)+self.__nú
            mero_nodos(sub_arbol.der)
        return 0

    def número_hojas(self):
        return self.__número_hojas(self.raiz)

    def __número_hojas(self, sub_arbol):
        if sub_arbol:
            if not sub_arbol.tiene_hijos():
                return 1
            return self.__número_hojas(sub_arbol.izq) + self.__nú
            mero_hojas(sub_arbol.der)

        return 0

    def nodos_internos(self):
        pass

    def altura():
        pass


if __name__ == '__main__':

    ar1 = ArbolBin()
    ar1.insertar("A")
    ar1.insertar("B")
    ar1.insertar("C")
    ar1.insertar("D")
    ar1.insertar("E")
    ar1.insertar("F")
    ar1.insertar("G")
    ar1.insertar("H")
    ar1.insertar("I")

    print(len(ar1))
    print(ar1.número_hojas())
    pre_orden(ar1)
