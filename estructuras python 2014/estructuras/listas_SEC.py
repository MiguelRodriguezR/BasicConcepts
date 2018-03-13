"""
Operaciones:- es_vacia
            - adicionar--->se le pasara un dato X
            - eliminar---->se la pasara un dato(Eliminara todas las apariciones 
            del dato) X
            - recorrer X
            - buscar------>dato a buscar
            - __len__ X
            - __iter__ X
            - ruletaRusa-->se le pasara una posicion (comenzando desde 0) 
            devolvera el dato ubicado en esa posicion X

           



"""




"""

██╗     ██╗███████╗████████╗ █████╗     ███████╗███████╗ ██████╗
██║     ██║██╔════╝╚══██╔══╝██╔══██╗    ██╔════╝██╔════╝██╔════╝
██║     ██║███████╗   ██║   ███████║    ███████╗█████╗  ██║     
██║     ██║╚════██║   ██║   ██╔══██║    ╚════██║██╔══╝  ██║     
███████╗██║███████║   ██║   ██║  ██║    ███████║███████╗╚██████╗
╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝╚══════╝ ╚═════╝

"""




"""
se importa la clase nodo para utilizarla con nuestra clase lista_SEC
"""
from listas_SE import NodoLSE


class ListaSEC:

    def __init__(self):
        """
        en el constructor definimos un atributo que apunte al primer nodo(self.cab),uno que 
        apunte al ultimo nodo(self.ult) y el tamaño de la lista
        """
        self.cab = None
        self.ult = None
        self.tam = 0

    def __iter__(self):
        """
        el metodo de iteracion que nos permitira llamar la lista como objeto iterable
        """
        if(self.es_vacia()):
            return None
        else:
            """
            con la funcion yield se retorna el primer nodo ya que haremos el conteo desde
            el segundo nodo(en caso de que exista un segundo nodo )
            """
            actual = self.cab.sig
            yield(self.cab.dato)
            while(actual is not self.cab):
                """
                seguira iterando hasta que actual no sea la cavecera
                """
                yield(actual.dato)
                actual = actual.sig

    def __len__(self):
        return self.tam

    def es_vacia(self):
        return(self.cab is None)
    
    def actualizar(self):
        """
        se usa para que el ultimo nodo apunte a el primero
        """
        if(self.ult is not None):
            self.ult.sig=self.cab
        if(self.cab is None):
            self.ult=None
            self.tam=0
        if(self.tam == 0):
            self.ult=None
            self.cab=None

    def buscar(self, dato):
        self.actualizar()
        """
        si el enlace del nodo de la cavecera no es la misma cavecera
        (lo que querria decir que solo tenemos un nodo)
        
        """
        if(self.cab.sig is not self.cab):
            actual = self.cab.sig
            """
            ^
            el nodo actual sera el segundo
            """
        posicion = 1
        """
        ^
        creamos una variable posicion que nos retornara la posicion del nodo
        que buscamos
        """
        if(self.cab.dato is dato and self.es_vacia() is not True):
            return 0
            """
            si el dato que ingresamos esta en el primer nodo entonces que regrese la 
            posicion 0
            """
        elif(self.es_vacia()):
            """
            si la lista esta vacia va a retornar un None como posicion 
            osea nunguna posicion
            """
            return None
        else:
            """
            se recorrera la lista siempre y cuando no se encuentre el dato o se 
            termine la lista
            """
            while(actual is not self.cab and actual.dato is not dato):
                actual = actual.sig
                posicion += 1
                """
                ^
                la posicion va incrementando a medida que se recorre la lista
                """
            if(actual is self.cab):
                return None
            else:
                return posicion
            
    

    def adicionar(self, dato):
        
        nuevonodo=NodoLSE(dato)
        """
        se crea un nuevo nodo para agregarlo luego
        """
        if(self.es_vacia()):
            """
            en el caso de que la lista sea vacia se le agrega un nodo el cual sera cavecera
            y cola a la vez
            """
            self.cab = nuevonodo
            self.cab.sig = self.cab
            self.tam += 1 
            self.ult = self.cab
        elif(type(dato) is type(self.cab.dato)):
            """
            de lo contrario se revisa si el siguiente no es la cavecera(osea un nodo unico)
            y se procede a añadir el nodo siempre aumentando el tamaño en 1
            """
            if(self.cab.sig is not self.cab):
                actual = self.cab.sig
                while(actual.sig is not self.cab):
                    actual = actual.sig
                actual.sig = nuevonodo
                actual.sig.sig = self.cab
                self.ult = actual.sig
                self.tam += 1
            else:
                self.cab.sig = nuevonodo
                self.cab.sig.sig = self.cab
                self.ult = self.cab.sig
                self.tam += 1

    def eliminar(self, dato):
        self.actualizar()
        """
        se procede a actualizar para no tener errores
        """
        
        if(self.es_vacia()):
            
            """
            en el caso que sea vacia se dice que no se encontro el dato y
            se retorna false
            """
            
            return False
        
        else:
            anterior = self.ult
            actual = self.cab
            tamanio = 0
            cont = 0
            """
            de lo contrario se itera una sola vez la lista y se busca
            todos los datos que sean iguales al dato ingresado
            """

            while(tamanio <= self.tam):
                if(actual.dato is dato):
                    if(self.cab.sig is self.cab):
                        """
                        si el dato esta en el unico nodo se vuelve la lista vacia
                        """
                        self.cab=None
                        self.tam-=1
                        return True
                    if(actual is self.ult):
                        """
                        si el dato a eliminar esta en el ultimo nodo
                        ahora la cola sera el anterior a ese
                        """
                        self.ult = anterior
                    if(actual is self.cab):
                        """
                        si el dato a eliminar esta en el primer nodo
                        ahora la cabecera sera el siguiente a ese
                        """
                        self.cab = actual.sig
                    """
                    el contador se suma en uno para al final restarselo al tamaño
                    """    
                    cont += 1
                    anterior.sig = actual.sig
                    actual = actual.sig

                else:
                    anterior = actual
                    actual = actual.sig
                tamanio += 1

            self.tam -= cont
            self.actualizar()
            """
            al finalizar se retorna si la operacion tubo exito
            """
            return True
        self.actualizar()
        
    def recorrer(self):
        
        """
        se actualiza y se crea una variable texto para guardar la lista 
        """
        self.actualizar()
        texto="{}"
        if(self.es_vacia() is not True):
            texto = "{"
            actual = self.cab
            for i in range(0, self.tam):
                """
                a medida que crece se le añade una coma 
                """
                texto = texto + str(actual.dato)
                texto = texto + ","
                actual = actual.sig
            texto = texto + "}"
            """
            al final se imprime el texto
            """
        print(texto)

    def ruletaRusa(self, pos):
        """
        si la lista es vacia se retorna que no se encontro la posicion
        """
        if(self.es_vacia()):
            return None
        self.actualizar()
        """
        de lo contrario se itera una vez la lista hasta encontrar el dato
        """
        actual = self.cab
        posicion = 0

        while(posicion != pos):
            posicion += 1
            actual = actual.sig
            """
            al final se retorna la posicion
            """
        return actual
       
    
    

#    ***********************************************************
#    *                                                         *
#    *                METODOS ADICIONALES                      *
#    *                                                         *
#    ***********************************************************            

    
    def eliminarTodo(self):
        self.cab=None
        self.ult=None
        tam=0
        
    def dar_datos(self):
        self.actualizar()
        texto="tamaño:"+str(self.tam)+",Cavecera:"+str(self.cab)+",Cola:"+str(self.ult)
        print(texto)
        
    def eliminarPos(self,pos):
        if(pos<0):
            while(pos<0):
                pos=self.tam+pos
        
        self.actualizar()
        if(self.es_vacia()):
            return True
        if(self.cab is self.cab.sig):
            self.eliminarTodo()
            self.tam=0
            return True
        else:
            
            posicion=0
            anterior=self.ult
            actual=self.cab
            while(posicion < pos):
                anterior=actual
                actual=actual.sig
                posicion+=1
                 
            anterior.sig=actual.sig
            self.tam-=1
            if(self.cab is actual):
                self.cab=self.cab.sig
            if(self.ult is actual):
                self.ult=anterior
            self.actualizar()
            
            return True
            
       
        
        


if __name__ == '__main__':

    lista = ListaSEC()
    for i in range(0,12):
        lista.adicionar("a")
        lista.adicionar("e")
         
        
  
    lista.eliminar("a")
    lista.eliminar("e")
    lista.recorrer()
    lista.dar_datos()
        
        