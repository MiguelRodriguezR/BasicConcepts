#!/usr/bin/env python3
"""
    PROJECT:

    MODULE: cola_prioridad_n.py

    DESCRIPTION:


    DATE: 07.04.2016 08:22:03 COT

    AUTHORS: Student 1 and Student 2
"""
from pila_cola import Cola
from pila_cola import Objeto1
from pila_cola import Objeto2


def validar_homogeneidad(nodo,dato):
    if nodo is not None:
        if isinstance(dato,type(nodo.dato)):
            return True
    return False

class NodoPrioridad:
    '''
    Clase que implementa el funcionamiento de un Nodo que maneja una prioridad.
    '''
    def __init__(self, dato, prioridad):
        '''
        Método constructor que inicializa el Nodo con un dato y su prioridad.

        :param dato: El elemento o dato que es almacenado dentro del Nodo.
        :type dato: object
        :param prioridad: Un valor numérico entero que representa la prioridad
                          del Nodo y que estará en el rango:
                                    (1 > 2 > 3 > ... > n)
        :type prioridad: int
        '''
        self.dato = dato
        self.sig = None
        self.prioridad = prioridad


class ColaDePrioridad(Cola):
    '''
    Clase que implementa el funcionamiento del ADT Cola de Prioridad,
    utilizando Nodos del tipo NodoPrioridad. Serán atentidos primeramente, o
    tienen MAYOR prioridad, los Nodos que por el contrario poseen un valor de
    prioridad menor.

    ATENCIÓN: Esta clase debe soportar el manejo de los mismos métodos que
    implementa una clase Cola, con la excepción del método encolar que posee
    una implementación diferente.
    '''
    def __init__(self):
        super(ColaDePrioridad, self).__init__()

    def encolar(self, nuevo_dato, prioridad):
        """
        Método que adiciona un nuevo NodoPrioridad con su dato a la Cola de
        Prioridad, según la prioridad que éste tendrá. A mayor valor de la
        prioridad el nuevo NodoPrioridad se ubicará hacia el final de la
        Cola de Prioridad.
        - Si el nuevo NodoPrioridad tiene la misma prioridad que uno o varios
        nodos de la Cola de Prioridad, el nuevo NodoPrioridad se ubicará
        después del último NodoPrioridad con la misma prioridad.

        :param nuevo_dato: El elemento o dato que es almacenado dentro del
                           NodoPrioridad.
        :type nuevo_dato: object
        :param prioridad: Un valor numérico entero que representa la prioridad
                          del NodoPrioridad y por lo tanto determina la
                          posición de éste dentro de la Cola de Prioridad.
        :type prioridad: int
        :returns: True en el caso de que nuevo_dato se haya adicionado a la
                  Cola de Prioridad de forma satisfactoria. False en caso
                  contrario.
        :rtype: bool
        """
        nuevo_nodo = NodoPrioridad(nuevo_dato,prioridad)
        if self.es_vacia():
            self._Cola__frente = nuevo_nodo
            self._Cola__tamano += 1
            return True
        else:
            if validar_homogeneidad(self._Cola__frente,nuevo_dato):
                if int(self._Cola__frente.prioridad) >  int(nuevo_nodo.prioridad):
                    nuevo_nodo.sig=self._Cola__frente
                    self._Cola__frente=nuevo_nodo
                    self._Cola__tamano += 1
                    return True
                nodo_actual = self._Cola__frente
                while nodo_actual.sig is not None:
                    if int(nodo_actual.sig.prioridad) >  int(nuevo_nodo.prioridad):
                        nuevo_nodo.sig=nodo_actual.sig
                        nodo_actual.sig=nuevo_nodo
                        return True
                    nodo_actual = nodo_actual.sig

                nodo_actual.sig = nuevo_nodo
                self._Cola__final = nuevo_nodo
                self._Cola__tamano += 1
                return True
        return False

if __name__ == '__main__':

    #creando objetos
    o11=Objeto1("1-prioridad 1")
    num=2
    o12=Objeto1("2-prioridad 1")
    o21=Objeto2("1-prioridad 3")
    o13=Objeto1("1-prioridad 2")
    o14=Objeto1("2-prioridad 2")
    o15=Objeto1("1-prioridad 3")
    o16=Objeto1("1-prioridad 500")

    print("---------TEST COLA PIORIDAD ----------") 
    cola = ColaDePrioridad()
    #probando objetos
    cola.encolar(o13,2)
    cola.encolar(o16,500)
    cola.encolar(o15,3)
    cola.encolar(o11,1)
    cola.encolar(num,2)
    cola.encolar(o21,3)
    cola.encolar(o12,1)
    cola.encolar(o14,2)
    print(str(cola.desencolar()))
    print(str(cola.desencolar()))
    print(str(cola.desencolar()))
    print(str(cola.desencolar()))
    print(str(cola.desencolar()))
    print(str(cola.desencolar()))
