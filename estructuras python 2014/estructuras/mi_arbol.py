#!/usr/bin/env python3
#
# Proyecto:
# Archivo: mi_arbol.py
# Autores: (n)
# Fecha: 23.05.2014 07:59:37 UTC
# Descripción:
from random import random
from mis_recorridos import pre_orden


class NodoArbBin:

    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None

    def tiene_hijos(self):
        return (self.izq and self.der is None)


class ArbolBinario:

    def __init__(self):
        self.raiz = None

    def es_vacio(self):
        return(self.raiz is None)

    def insertar(self, nueva_clave):
        self.raiz = self.__insertar(self.raiz, nueva_clave)

    def __insertar(self, sub_raiz, nueva_clave):
        if sub_raiz is None:
            sub_raiz = NodoArbBin(nueva_clave)
        # por izquierda
        elif random() <= 0.5:
            sub_raiz.izq = self.__insertar(sub_raiz.izq, nueva_clave)
        else:
            # por derecha
            sub_raiz.der = self.__insertar(sub_raiz.der, nueva_clave)
        return sub_raiz
    # retorna el número de nodos del árbol

    def __len__(self):
        return self.__numero_nodos(self.raiz)

    def __numero_nodos(self, sub_raiz):
        if sub_raiz is None:
            return 0
        else:
            return(1 + self. __numero_nodos(sub_raiz.izq) +
                   self. __numero_nodos(sub_raiz.der))

if __name__ == '__main__':
    arbol = ArbolBinario()
    arbol.insertar(7)
    arbol.insertar(9)
    arbol.insertar(5)
    arbol.insertar(10)
    arbol.insertar(20)
    arbol.insertar(30)
    pre_orden(arbol)
    arbol.len()
