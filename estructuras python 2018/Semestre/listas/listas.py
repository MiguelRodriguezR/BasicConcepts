from nodos import NodoLSE
from nodos import NodoLDE


class LDE:

    def __init__(self):
        self.cab = None
        self.pie = None
        self.actual = None

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

    def adelante(self):
        if(self.actual is None):
            self.actual = self.cab
            return self.actual.dato
        if(self.actual.sig is None):
            return self.actual.dato
        self.actual = self.actual.sig
        return self.actual.dato

    def atras(self):
        if(self.actual is None):
            self.actual = self.cab
            return self.actual
        if(self.actual.ant is None):
            return self.actual.dato
        self.actual = self.actual.ant
        return self.actual.dato


    def agregar(self, nuevo_dato):
        """
        El metodo agregar tiene que devolver un valor boleano(true si se puede,
        false
        sino)
        """
        if(self.homogeneidad(nuevo_dato)):
            nuevo_nodo = NodoLDE(nuevo_dato)  
            if self.es_vacia():
                self.cab = nuevo_nodo
                self.pie = self.cab
            else:
                nodo_actual = self.cab
                while nodo_actual.sig is not None:
                    nodo_actual = nodo_actual.sig  # pregunta si tiene o no otro no
                nodo_actual.sig = nuevo_nodo
                self.pie = nodo_actual.sig
                nuevo_nodo.ant = nodo_actual
            return True
        return False

    def recorrer(self,atras=False):
        if atras is False:
            nodo_actual = self.cab
            while nodo_actual is not None:
                print(nodo_actual.dato)
                nodo_actual = nodo_actual.sig
        else:
            nodo_actual = self.pie
            while nodo_actual is not None:
                print(nodo_actual.dato)
                nodo_actual = nodo_actual.ant

    def __len__(self):
        """
        return int
        """
        nodo_actual = self.cab
        contador  = 0
        while nodo_actual is not None:
            contador+=1
            nodo_actual = nodo_actual.sig
        return contador

    def remover(self, item, por_pos=True,  all=False):
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
                self.pie = nodo_actual.sig
                if self.actual == nodo_actual:
                    self.actual = nodo_actual.ant
                if nodo_actual.sig is not None:
                    self.cab.ant=None
                return True
            else:
                nodo_anterior.sig = nodo_actual.sig
                if self.actual == nodo_actual:
                    self.actual = nodo_actual.ant
                if nodo_actual.sig is not None:
                    nodo_actual.sig.ant = nodo_anterior
                else:
                    self.pie = nodo_anterior
                return True
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
                        self.cab.ant = None
                        nodo_actual = self.cab
                        #por si es la cabecera
                        if self.actual == nodo_actual:
                            self.actual = nodo_actual.ant

                    else:
                        nodo_anterior.sig = nodo_actual.sig
                        #por si es un dato despues de la cabecera
                        if self.actual == nodo_actual:
                            self.actual = nodo_actual.ant
                        if nodo_actual.sig is not None:
                            nodo_actual.sig.ant = nodo_anterior
                        else:
                            self.pie = nodo_anterior
                        nodo_actual = nodo_actual.sig
                if(all == False):
                    nodo_actual = None
                    return True
                    #print(nodo_actual)
                    #print(nodo_actual == None)
        return False





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
        if(pos>=0 and pos<=len(self)-1 and self.homogeneidad(nuevo_dato)):
            nuevo_nodo = NodoLDE(nuevo_dato)
            nodo_anterior = None
            nodo_actual = self.cab
            cr_pos = 0
            while nodo_actual is not None and cr_pos != pos:  # seubicaenlap a elim
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.sig
                cr_pos += 1
            if pos == 0:
                nuevo_nodo.sig = nodo_actual
                self.cab = nuevo_nodo
                nodo_actual.ant=nuevo_nodo

            else:
                nuevo_nodo.sig = nodo_actual
                nodo_actual.ant= nuevo_nodo
                nuevo_nodo.ant = nodo_anterior
                nodo_anterior.sig = nuevo_nodo
            return True
        else:
            return False

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
        nodo_actual = self.cab
        nodo_buscar = NodoLDE(dato_a_buscar)
        while nodo_actual is not None and nodo_actual != nodo_buscar:
            nodo_actual = nodo_actual.sig
        if(nodo_actual == nodo_buscar):
            return True
        else:
            return False


    def __len__(self):
        """
        return int
        """
        nodo_actual = self.cab
        contador  = 0
        while nodo_actual is not None:
            contador+=1
            nodo_actual = nodo_actual.sig
        return contador

    def __str__(self):
        """
        tiene un
        return str metodo de presentacion
        print (lista_nuevos)
        """
        nodo_actual = self.cab
        res = "None"
        while nodo_actual is not None:
            res+="<-["+str(nodo_actual.dato)+"]->"
            nodo_actual = nodo_actual.sig
        res+="None"
        return res

    def __iter__(self):
        nodo_actual = self.cab
        while nodo_actual is not None:
            yield(nodo_actual.dato)
            nodo_actual = nodo_actual.sig


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
        if(pos>=0 and pos<=len(self)-1 and self.homogeneidad(nuevo_dato)):
            nuevo_nodo = NodoLSE(nuevo_dato)
            nodo_anterior = None
            nodo_actual = self.cab
            cr_pos = 0
            while nodo_actual is not None and cr_pos != pos:  # seubicaenlap a elim
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.sig
                cr_pos += 1
            if pos == 0:
                nuevo_nodo.sig = nodo_actual
                self.cab = nuevo_nodo

            else:
                nuevo_nodo.sig = nodo_actual
                nodo_anterior.sig = nuevo_nodo
            return True
        else:
            return False

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
        nodo_anterior = None
        nodo_actual = self.cab
        cr_pos = 0
        while nodo_actual is not None and nodo_actual.dato == dato_a_buscar:  # seubicaenlap a elim
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.sig
            cr_pos += 1
        if nodo_actual is not None:
            return True
        return False

    def __len__(self):
        """
        return int
        """
        nodo_actual = self.cab
        contador  = 0
        while nodo_actual is not None:
            contador+=1
            nodo_actual = nodo_actual.sig
        return contador

    def __str__(self):
        """
        tiene un
        return str metodo de presentacion
        print (lista_nuevos)
        """
        nodo_actual = self.cab
        res = ""
        while nodo_actual is not None:
            res+="["+str(nodo_actual.dato)+"]->"
            nodo_actual = nodo_actual.sig
        res+="None"
        return res


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
