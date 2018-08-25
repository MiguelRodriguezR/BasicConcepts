
# !/usr/bin/env python3
#
# Project:arbol binario
# File: arboles.py
# Authors: (Camila Quintero-Geraldin Fajardo)
# Date: 27.04.2016 15:42:25 COT
# Description:


from random import random
# from recorridos import pre_orden, in_orden, post_orden


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


class ABinBus:

    def __init__(self):
        self.raiz = None
        self.can = 0

    def num_nodos_internos(self):
        return self.can

    def altura(self):
        return self.can

    def agregar(self, nueva_clave):
        self.raiz = self.__agregar(self.raiz, nueva_clave)

    def __agregar(self, sub_raiz, nueva_clave):

        if (sub_raiz is None):

            sub_raiz = NodoABin(nueva_clave)

        elif(sub_raiz.clave == nueva_clave):
            print("No puedes Insertar la clave")

        elif(nueva_clave < sub_raiz.clave):

            sub_raiz.izq = self.__agregar(sub_raiz.izq, nueva_clave)

        if(nueva_clave > sub_raiz.clave):
            sub_raiz.der = self.__agregar(sub_raiz.der, nueva_clave)

        return sub_raiz

    def buscar(self, clave_buscar):
        return (self.__buscar(self.raiz, clave_buscar))

    def __buscar(self, sub_raiz, clave_buscar):

        if (sub_raiz is None):
            return False

        elif(sub_raiz.clave == clave_buscar):
            return True

        elif(clave_buscar < sub_raiz.clave):

            return self.__buscar(sub_raiz.izq, clave_buscar)

        elif(clave_buscar > sub_raiz.clave):

            return self.__buscar(sub_raiz.der, clave_buscar)

    def encontrar(self, clave_encontrar):
        return (self.__encontrar(self.raiz, clave_encontrar))

    def __encontrar(self, sub_raiz, clave_encontrar):

        if (sub_raiz is None):
            return sub_raiz

        elif(sub_raiz.clave == clave_encontrar):
            return sub_raiz.clave

        elif(clave_encontrar < sub_raiz.clave):

            return self.__encontrar(sub_raiz.izq, clave_encontrar)

        elif(clave_encontrar > sub_raiz.clave):
            return self.__encontrar(sub_raiz.der, clave_encontrar)

    def __len__(self):
        return self.contar_hojas()

    def encontrar_min(self):
        pass

    def encontrar_max(self):
        pass

    def num_hojas(self):
        return self.contar_hojas()


    def contar_hojas(self):
        self.can = 0
        self.can = self.__contar_hojas(self.raiz)
        return self.can

    def __contar_hojas(self, sub_raiz):

        if sub_raiz is not None:
            if sub_raiz.izq is None and sub_raiz.der is None:
                self.can += 1

            self.__contar_hojas(sub_raiz.izq)
            self.__contar_hojas(sub_raiz.der)
        return self.can

    def remover(self, clave_eliminar , cc = True):
        ban = self.__eliminar(self.raiz, clave_eliminar)
        return ban

    def __eliminar(self, sub_raiz, clave_eliminar):
        if (sub_raiz is not None):
            # if  sub_raiz.der None:   # print("###")
            if sub_raiz.der.clave == clave_eliminar:
                if sub_raiz.der.izq is None and sub_raiz.der.der is None:
                    self.can -= 1
                    sub_raiz.der = None
                    return True
            # if  sub_raiz.izq is not None:
            # print("***")
            if sub_raiz.izq.clave == clave_eliminar:
                print("----")
                if sub_raiz.izq.izq is None and sub_raiz.izq.der is None:

                    sub_raiz.izq = None
                    self.can -= 1
                    return True
            elif(clave_eliminar < sub_raiz.clave):
                return self.__eliminar(sub_raiz.izq, clave_eliminar)

            elif(clave_eliminar > sub_raiz.clave):
                return self.__eliminar(sub_raiz.der, clave_eliminar)
        else:
            return False



if __name__ == '__main__':

    ar1 = ABinBus()
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
