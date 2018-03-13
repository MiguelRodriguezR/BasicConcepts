# 29/abril/2014
# desarrollado por Miguel Rodriguez y jhonatan 
   

from listas_SE import NodoLSE, ListaSE
from listas_DEA import ListaDEA


class NodoLDE(NodoLSE):  # herencia de la clase nodo de listas_SE

    def __init__(self, dato=None):
        super().__init__(dato,None)  
        self.ant = None


class ListaDE(ListaDEA, ListaSE):

    def __init__(self):
        super().__init__()  # hernencia de la clase ListaSE
        self.anclaje=None

    def adicionar(self, nuevo_dato):
        nuevo_Nodo = NodoLDE(nuevo_dato)
        if self.es_vacia():
            self.cab = nuevo_Nodo
        else:
            tipo_dato = type(self.cab.dato)
            if not isinstance(nuevo_dato, tipo_dato):
                lst_msj = ['valor >>>\n', str(nuevo_dato),
                           "\n <<< no permitido!",
                           "\nse requiere datos de tipo:",
                           tipo_dato.__name__,
                           "\n los datos de la lista tienen que ser",
                           "HoMoGeNeos!"]
                msj_error = "".join(lst_msj)
                raise TypeError(msj_error)  # raise lansan un mensaje de error
            nodo_actual = self.cab
            while nodo_actual.sig is not None:
                nodo_actual = nodo_actual.sig
            nodo_actual.sig = nuevo_Nodo
            nuevo_Nodo.ant = nodo_actual
        self.tam += 1

    def borrar(self, dato_elm):
        if not (self.es_vacia()):
            nodo_actual = self.cab
            while nodo_actual is not None and dato_elm != nodo_actual.dato:
                nodo_actual = nodo_actual.sig
            if nodo_actual is not None:
                self.tam -= 1
                if nodo_actual is self.anclaje:
                    self.anclaje=nodo_actual.ant
                if nodo_actual.ant is None:
                    self.cab = self.cab.sig
                    self.cab.ant=None
                else:
                    nodo_actual.ant.sig = nodo_actual.sig
                    if nodo_actual.sig is not None:
                        nodo_actual.sig.ant = nodo_actual.ant

    def recorrer_atras(self):
        lista=[]
        nodo_actual = self.cab
        while nodo_actual.sig is not None:
            nodo_actual=nodo_actual.sig
        while nodo_actual is not None:
            lista.append(nodo_actual.dato)
            nodo_actual=nodo_actual.ant
        print(lista)

    def adelante(self):
        if not self.es_vacia():
            if self.anclaje is None:
                self.anclaje=self.cab
            elif self.anclaje.sig is not None:
                self.anclaje=self.anclaje.sig
            return self.anclaje.dato 
        return None    

    def atras(self):
        if not self.es_vacia():
            if self.anclaje is None:
                self.anclaje=self.cab
            elif self.anclaje.ant is not None:
                self.anclaje=self.anclaje.ant
            return self.anclaje.dato
        return None
        
if __name__ == '__main__':
    lde = ListaDE()
        
    lde.adicionar(5)
    lde.adicionar(10)
    lde.adicionar(15)
    lde.adicionar(20)
    lde.recorrer()
    lde.recorrer_atras()
    print(lde.adelante())
    print(lde.adelante())
    print(lde.adelante())
    print(lde.adelante())
    print(lde.adelante())
    print(lde.atras())
    print(lde.atras())
    print(lde.adelante())

    print("tamaño", len(lde))
   
