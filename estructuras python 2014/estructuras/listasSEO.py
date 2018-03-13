class NodoLSE:
    def __init__(self,dato=None):
        self.dato=dato
        self.sig=None
    def __str__(self):
        return(str(self.dato))


class ListaSE:
    def __init__(self):
        self.cab=None
        self.tam=0
        
    def __iter__(self):
        actual=self.cab
        while(actual is not None):
            yield(actual.dato)
            actual=actual.sig
            
    def es_vacia(self):
        return(self.cab is None)
    
    def __len__(self):
        return self.tam

    
    def buscar(self,posicion):
        actual = self.cab
        contador=0
        if(self.es_vacia()):
            return None
        
        while(actual is not None and posicion!=contador):
            actual=actual.sig
            contador+=1
        if (actual is not None):
            return actual.dato
    
    def adicionar(self,nuevo_dato):
        
        nuevo_nodo=NodoLSE(nuevo_dato)
        if(self.es_vacia()):
            self.cab=nuevo_nodo
            self.tam=1
        else:
            if(type(self.cab.dato) is type(nuevo_dato)):
                actual=self.cab
                while(actual.sig is not None and actual.dato!=nuevo_dato):
                    actual=actual.sig
                if actual.dato is not nuevo_dato:    
                    actual.sig=nuevo_nodo
                    self.tam=self.tam+1
            else:
                #pass
                print("el dato '"+ str(nuevo_dato) +"' tiene un tipo invalido")
                
        
                        
                        
    def recorrer(self):
        self.oredenar()
        actual=self.cab
        while(actual is not None):
            print(actual)
            actual=actual.sig
            
    
            
    def borrar_dato(self,dato):
        if(not self.es_vacia()):
            actual=self.cab
            anterior=None
            while(actual is not None and actual.dato != dato):
                anterior=actual
                actual=actual.sig
            if(actual is not None):
                if(anterior is None):
                    self.cab=self.cab.sig
                    self.tam=self.tam-1
                    return True
                else:
                    anterior.sig=actual.sig
                    self.tam=self.tam-1
                    return True
            else:
                return False
        else:
            return False
        
    def oredenar(self):
        actual=self.cab
        if(actual.sig is not None):
            siguiente=actual.sig
        else:
            return False
        for x in range(0,self.tam):
            for y in range(x,self.tam):
                actualdato=actual.dato
                siguientedato=siguiente.dato
                if(actualdato > siguientedato):
                    aux=siguiente.dato
                    siguiente.dato=actual.dato
                    actual.dato=aux
                if(siguiente.sig is not None):
                    siguiente=siguiente.sig
            if(actual.sig is not None):        
                actual=actual.sig
            if(actual.sig is not None):
                siguiente=actual.sig
            
            
        
        
        
        
        
        
        
        
        
lista=ListaSE()
lista.adicionar(3)
lista.adicionar(5)
lista.adicionar(8)
lista.adicionar(9)
lista.adicionar(12)
lista.adicionar(25)
lista.adicionar(109)
lista.adicionar(32)
lista.adicionar(25)
lista.adicionar(5)
lista.adicionar(15)
lista.adicionar(45)
lista.adicionar(9)
lista.adicionar(67)
lista.adicionar(80)
lista.adicionar(1)
lista.recorrer()

        
        