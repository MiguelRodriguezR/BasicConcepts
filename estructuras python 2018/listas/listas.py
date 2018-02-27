from nodos.nodos import NodoLSE


class LSE:

    def __init__(self):
        self.cab = None

    def homogeneidad(self, dat):
        if(self.cab is None):
            return True
        elif(self.cab is not None and isinstance(dat,type(self.cab.dato))):
            return True
        return False



    def es_vacia(self):
        if self.cab is None:
            return True
        else:
            return False

    def agregar(self, nuevo_dato):
        """
        El metodo agregar tiene que devolver un valor boleano(true si se puede,
        false
        sino)
        """
        if(self.homogeneidad(nuevo_dato)):
            nuevo_nodo = NodoLSE(nuevo_dato)  # Crear nuevo nodo con la importacio
            if self.es_vacia():
                self.cab = nuevo_nodo
            else:
                nodo_actual = self.cab
                while nodo_actual.sig is not None:
                    nodo_actual = nodo_actual.sig  # pregunta si tiene o no otro no
                nodo_actual.sig = nuevo_nodo
            return True
        else:
            return False

    def recorrer(self):
        nodo_actual = self.cab
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.sig

    def remover(self, item, por_pos=True):
        """
        def remover (self, item, por_pos = True):remover tiene que devolver un
        valor boleano
        lista (4,False)elimina todos los datos que cumplan que  sean 4
        en listas vamos a incorporar otros metodo
        """
        if(por_pos is True):
            nodo_anterior = None
            nodo_actual = self.cab
            pos = item
            cr_pos = 0
            while nodo_actual is not None and cr_pos != pos:  # seubicaenlap a elim
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.sig
                cr_pos += 1
            if pos == 0:
                self.cab = nodo_actual.sig
            else:
                nodo_anterior.sig = nodo_actual.sig
        else:
            nodo_anterior = None
            nodo_actual = self.cab
            while nodo_actual is not None:
                #print (nodo_actual.dato == item)
                while nodo_actual is not None and nodo_actual.dato != item:
                    nodo_anterior = nodo_actual
                    nodo_actual = nodo_actual.sig
                if nodo_actual is not None and nodo_actual.dato == item:

                    if (nodo_actual == self.cab):
                        self.cab = nodo_actual.sig
                        nodo_actual = self.cab

                    else:
                        nodo_anterior.sig = nodo_actual.sig
                        nodo_actual = nodo_actual.sig
                    #print(nodo_actual)
                    #print(nodo_actual == None)






    def posicionar(self, pos, nuevo_dato):
        """
        Inserta un nuevo dato en la posicion designada siempre y cuando esta
        sea valida :
        parametros:
        *pos: valor entero comenzando desde 0 que indica la posicion de la list
        a sobre la cual se va a insertar el nuevo nodos
        *nuevo_dato: el dato a ser insertado en una determinada posicion de la
        lista
        *retorna:
        true si el nuevo dato es insertado de forma satisfactoria en la listas
        false en caso contrario
        """
        pass

    def encontrar(self, dato_a_buscar):
        """ def __eq__(self,otro_objeto)
        if self.cod == otro_objeto.cod
            return True
        return false
        EJM
        Class estudiante
        e1=est("210"."juanpablo")
        e1=est("210"."pablo")
        if e1 == e2:

        """
    pass

    def __len__(self):
        """
        return int
        """
    pass

    def __str__(self):
        """
        tiene un
        return str metodo de presentacion
        print (lista_nuevos)
        """
    pass

    """
    def __init__(self,separator = "\n")
    pass
    como crear paquetes de tal forma que :
    listado_empleados.py
    quiero invocar de esta forma                       listas.py
    from ei.listas import LSE                    from ei.nodos import NodoLSE
                                                 from ei.validacion import ?
    lista.emp1 = LSE

    """
    """
     type me verifica si es o no si es del mismo dato en validación.py
    el metodo def posicionar (self,pos,nuevo_dato)
    debe devolver un valor boleano,
    """
