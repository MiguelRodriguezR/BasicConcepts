#!/usr/bin/env python3
#
# Project:
# File: arboles_bin_bus.py
# Authors: (student 1 and student 2)
# Date: 04.05.2016 16:36:05 COT
# Description:

from arboles import *
from recorridos import pre_orden


class ArbolBinBus(ArbolBin):

    def insertar(self, nueva_clave):

        self.raiz = self.__insertar(self.raiz, nueva_clave)

    def __insertar(self, sub_arbol, nueva_clave):

        if sub_arbol is None:

            sub_arbol = NodoABin(nueva_clave)

        elif nueva_clave < sub_arbol.clave:

            sub_arbol.izq = self.__insertar(sub_arbol.izq, nueva_clave)

        elif nueva_clave > sub_arbol.clave:

            sub_arbol.der = self.__insertar(sub_arbol.der, nueva_clave)
        else:
            print("clave duplicada:", nueva_clave)

        return sub_arbol

    def buscar(self, clave_buscar):

        return self.__buscar(self.raiz, clave_buscar)

    def __buscar(self, sub_arbol, clave_buscar):

        if sub_arbol:

            if sub_arbol.clave == clave_buscar:

                return sub_arbol.clave

            elif clave_buscar < sub_arbol:

                return self.__buscar(sub_arbol.izq, clave_buscar)

            else:

                return self.__buscar(sub_arbol.der, clave_buscar)

        return None

    def eliminar(self, clave_eliminar, mayor=True):
        pass

    def buscar_máximo(self):
        pass

    def buscar_mínimo(self):
        pass


if __name__ == '__main__':
    numeros = [20, 30, 15, 17, 25, 5, 28, 10]
    mi_abb = ArbolBinBus()

    for n in numeros:

        mi_abb.insertar(n)

    pre_orden(mi_abb)
    nb = int(input("Numero a buscar"))
    res_bus = mi_abb.buscar(nb)

    if res_bus:
        print("Econtrado:", res_bus)

    else:
        print("No Econtrado:", nb)
