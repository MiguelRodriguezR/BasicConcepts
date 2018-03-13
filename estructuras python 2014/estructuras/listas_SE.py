class NodoLSE:
    def __init__(self,dato=None,sig=None):
        self.dato=dato
        self.sig=sig
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
    
    def buscar(self,aux):
        pass
    
    def adicionar(self,nuevo_dato):
        nuevo_nodo=NodoLSE(nuevo_dato)
        if(self.es_vacia()):
            self.cab=nuevo_nodo
            self.tam=1
        else:
            if(type(self.cab.dato) is type(nuevo_dato)):
                actual=self.cab
                while(actual.sig is not None):
                    actual=actual.sig
                actual.sig=nuevo_nodo
                self.tam=self.tam+1
            else:
                #pass
                print("el dato '"+ str(nuevo_dato) +"' tiene un tipo invalido")
                        
                        
    def recorrer(self):
        lista=[]
        actual=self.cab
        while(actual is not None):
            lista.append(actual.dato)
            actual=actual.sig
        print(lista)
    
            
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
                anterior.sig=actual.sig
                self.tam=self.tam-1
                return True
            else:
                return False
        else:
            return False
        
        
        
        

#-----------------------------------------------------------------------------------------------------------------------------------------------------             

# Como eliminar espacios en blanco :3????????
# Como pasar varios argumentos a una funcion o metodo???????

# hacer una lista LISTA SIMPLEMENTE ORDENADA: que no acepte valores repetidos y que este ordenada de manor a mayor
            
#------------------------------------------------------------------------------------------------------------------------------------------------------
            
suma=0

if __name__=='__main__':
    lista_num=ListaSE()
    lista_num.adicionar(5)
    lista_num.adicionar(6)
    lista_num.adicionar(7)
    lista_num.recorrer()
    print(len(lista_num))
    
    for num in lista_num:
        suma+=num
    
    print(suma)
