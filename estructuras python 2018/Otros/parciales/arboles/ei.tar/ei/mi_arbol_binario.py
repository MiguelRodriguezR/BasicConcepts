from mi_arbol import NodoArbBin, ArbolBinario
from mis_recorridos import pre_orden, in_orden, pos_orden


class ArbolBinarioBus(ArbolBinario):

    def insertar(self, nueva_clave):
        self.raiz = self.__insertar(self.raiz, nueva_clave)

    def __insertar(self, sub_raiz, nueva_clave):

        if (sub_raiz is None):

            sub_raiz = NodoArbBin(nueva_clave)

        elif(sub_raiz.clave == nueva_clave):
            print("No puedes Insertar la clave")

        elif(nueva_clave < sub_raiz.clave):

            sub_raiz.izq = self.__insertar(sub_raiz.izq, nueva_clave)

        if(nueva_clave > sub_raiz.clave):
            sub_raiz.der = self.__insertar(sub_raiz.der, nueva_clave)

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

    def eliminar(self, clave_eliminar):
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


arbol = ArbolBinarioBus()
arbol.insertar(16)
arbol.insertar(8)
"""arbol.insertar(59)
arbol.insertar(7)
arbol.insertar(22)
arbol.insertar(70)
arbol.insertar(66)
arbol.insertar(74)
arbol.insertar(75)
arbol.insertar(9)
arbol.insertar(8)
arbol.insertar(12)
arbol.insertar(16)
arbol.insertar(-9)"""
# print(arbol.encontrar(13))
pre_orden(arbol)
print(arbol.contar_hojas())
arbol.eliminar(7)
print("############")
pre_orden(arbol)
print(arbol.contar_hojas())
