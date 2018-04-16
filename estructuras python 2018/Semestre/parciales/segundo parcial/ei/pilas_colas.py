from ei.nodos import NodoLSE
from ei.validación import Validacion

class NodoPila(NodoLSE):
    pass


class Pila:

    def __init__(self, sep=" "):
        self.__cima = None
        self.longitud = 0
        self.separador = sep

    def es_vacia(self):
        return(self.__cima is None)

    def apilar(self, nuevo_dato):
        nuevo_nodo = NodoLSE(nuevo_dato)
        bApilo = True
        if self.es_vacia():
            self.__cima = nuevo_nodo
        else:
            val = Validacion()
            if val.homogeneidad(self.__cima.dato, nuevo_dato):
                nuevo_nodo.sig = self.__cima
                self.__cima = nuevo_nodo

            else:
                bApilo = False
        if bApilo:
            self.longitud += 1
        return bApilo

    def desapilar(self):
        if self.es_vacia():
            return None
        else:
            self.longitud-=1
            un_dato = self.__cima.dato
            self.__cima = self.__cima.sig
            return un_dato

    def cima(self):
        return(None if self.es_vacia() else self.__cima.dato)

    def __str__(self):
        string = ""
        for x in self:
            string += str(x)+self.separador
        return string

    def __len__(self):
        return self.longitud

    def __iter__(self):
        aux = Pila()
        while(self.es_vacia() is False):
            dato = self.desapilar()
            aux.apilar(dato)
            yield dato
        self.apilardesde(aux)

    def apilardesde(self, pila):
        while pila.es_vacia() is False:
            dato = pila.desapilar()
            self.apilar(dato)


class NodoCola(NodoLSE):
    pass


class Cola:
    def __init__(self):
        self.__frente = None
        self.__final = None
        self.__tamano = 0

    def es_vacia(self):
        return(self.__frente is None)

    def encolar(self, nuevo_dato):
        nuevo_nodo = NodoCola(nuevo_dato)
        if self.es_vacia():
            self.__frente = nuevo_nodo
            self.__tamano += 1
            return True
        else:
            val = Validacion()
            if val.homogeneidad(self.__frente.dato, nuevo_dato):
                nodo_actual = self.__frente
                while nodo_actual.sig is not None:
                    nodo_actual = nodo_actual.sig
                nodo_actual.sig = nuevo_nodo
                self.__final = nuevo_nodo
                self.__tamano += 1
                return True
        return False

    def desencolar(self):
        if self.es_vacia():
            return None
        else:
            self.__tamano-=1
            un_dato = self.__frente.dato
            self.__frente = self.__frente.sig
            return un_dato

    def frente(self):
        return(None if self.es_vacia() else self.__frente.dato)

    def __len__(self):
        return __tamano

    def __iter__(self):
        aux = Cola()
        while(self.es_vacia() is False):
            dato = self.desencolar()
            aux.encolar(dato)
            yield dato
        self.encolardesde(aux)

    def encolardesde(self, cola):
        while cola.es_vacia() is False:
            dato = cola.desencolar()
            self.encolar(dato)



if __name__ == '__main__':
    # creando objetos
    o11 = Objeto1(1)
    num = 2
    o12 = Objeto1(2)
    o13 = Objeto1(3)
    o21 = Objeto2(1)

    print("---------TEST PILA ----------")
    pila = Pila("|\n|")
    # probando objetos
    pila.apilar(o11)
    pila.apilar(num)
    pila.apilar(o21)
    pila.apilar(o12)
    pila.apilar(o13)

    print(str(pila))

    for x in pila:
        print("recorriendo"+str(x))

    print("sacando"+str(pila.desapilar()))
    print("sacando"+str(pila.desapilar()))
    # print(str(pila.desapilar()))

    for x in pila:
        print("recorriendo"+str(x))

    print("---------TEST COLA ----------")
    cola = Cola()
    # probando objetos
    cola.encolar(o11)
    cola.encolar(num)
    cola.encolar(o21)
    cola.encolar(o12)

    for x in cola:
        print("recorriendo"+str(x))

    print(str(cola.desencolar()))
    print(str(cola.desencolar()))
    print(str(cola.desencolar()))
