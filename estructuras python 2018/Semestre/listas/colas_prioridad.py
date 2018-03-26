from nodos import NodoLSE
from validación import Validacion
from objetos_Prueba import *
from pilas_colas import *

class NodoColaPrioridad(NodoLSE):

    def __init__(self,dato,prioridad):
        super().__init__(dato)
        self.prioridad = prioridad

    def __str__(self):
        return str(self.dato)


class PriorityQueue():

    def __init__(self):
        self.__frente = None
        self.__final = None
        self.__tamano = 0

    def es_vacia(self):
        return self.__frente is None

    def encolar(self,nuevo_dato,prioridad):

        if (not isinstance(prioridad,int)):
            return False
        v = Validacion()
        if (not self.es_vacia() and not v.homogeneidad(self.__frente.dato,nuevo_dato)):
            return False
        nuevo_nodo = NodoColaPrioridad(nuevo_dato,prioridad)
        if self.es_vacia():
            self.__frente = nuevo_nodo
            self.__final = nuevo_nodo
            self.__tamano += 1
            return True
        nodo_actual = self.__frente
        nodo_anterior = None
        while nodo_actual is not None and nodo_actual.prioridad <= prioridad:
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.sig
        if(nodo_anterior is None):
            self.__frente = nuevo_nodo
            nuevo_nodo.sig = nodo_actual
            self.__tamano += 1
            return True
        nodo_anterior.sig = nuevo_nodo
        nuevo_nodo.sig = nodo_actual
        self.__tamano += 1
        if nodo_actual is None:
            self.__final = nuevo_nodo
        return True



    def desencolar(self):
        if self.es_vacia():
            return None
        else:
            un_dato = self.__frente.dato
            self.__frente = self.__frente.sig
            self.__tamano -= 1
            return un_dato


    def frente(self):
        if self.__frente is None:
            return None
        return self.__frente.dato

    def final(self):
        if self.__final is None:
            return None
        return self.__final.dato

    def __len__(self):
        return self.__tamano

    def __iter__(self):
        nodo_actual = self.__frente
        while(nodo_actual is not None):
            yield nodo_actual.dato
            nodo_actual = nodo_actual.sig

if __name__ == '__main__':
    o11 = ObjetoPrioridad(1,3)
    num = 2
    o12 = ObjetoPrioridad(2,3)
    o13 = ObjetoPrioridad(3,1)
    o14 = ObjetoPrioridad(4,2)
    o15 = ObjetoPrioridad(5,1)
    o16 = ObjetoPrioridad(6,2)
    o21 = Objeto2(1)

    cola = PriorityQueue()
    # probando objetos
    cola.encolar(o11,o11.prioridad)
    cola.encolar(num,0)
    cola.encolar(o21,0)
    cola.encolar(o12,o12.prioridad)
    cola.encolar(o13,o13.prioridad)
    cola.encolar(o14,o14.prioridad)
    cola.encolar(o15,o15.prioridad)
    cola.encolar(o16,o16.prioridad)

    for x in cola:
        print(x)

    print ("==========")
    print(cola.frente())
    print(cola.final())
    print(len(cola))
