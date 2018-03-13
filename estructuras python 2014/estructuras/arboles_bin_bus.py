from arboles import NodoABin
from recorridos import pre_orden



class ArbolBinBus:
    def __init__(self):
        self.raiz=None


    def insertar(self, nueva_clave):
        self.raiz = self.__insertar(self.raiz, nueva_clave)
        
    def __insertar (self, sub_raiz, nueva_clave):
        if sub_raiz is None:
            sub_raiz = NodoABin(nueva_clave)
        elif sub_raiz.clave == nueva_clave:
            print("no se puede insertar.... pobresito :'(")
        elif sub_raiz.clave > nueva_clave:
            por_izq = self.__insertar(sub_raiz.izq, nueva_clave)
            sub_raiz.izq = por_izq
        else:
            por_der = self.__insertar(sub_raiz.der, nueva_clave)
            sub_raiz.der = por_der
        return sub_raiz
    
    def padre(self,sub_raiz,clave_enc):
        if sub_raiz is None:
            return None
        elif ((sub_raiz.izq is not None and sub_raiz.izq.clave == clave_enc) or (sub_raiz.der is not None and sub_raiz.der.clave == clave_enc)):
            return sub_raiz
        elif clave_enc < sub_raiz.clave:
            return self.padre(sub_raiz.izq, clave_enc)
        else:
            return self.padre(sub_raiz.der, clave_enc)
        
    def buscar(self, clave_buscar):
        return self.__buscar(self.raiz, clave_buscar)
    
    def __buscar(self,sub_raiz,clave_buscar):
        if sub_raiz is not None:
            print(str(sub_raiz.clave)+'<-->'+str(clave_buscar))
            if sub_raiz.clave == clave_buscar:
                return True
            else:
                if sub_raiz.clave > clave_buscar:
                    return self.__buscar(sub_raiz.izq, clave_buscar)
                else:
                    return self.__buscar(sub_raiz.der, clave_buscar)
                return False
        return False
    
    def eliminar(self,elemento):
        sub_raiz=self.raiz
        encontrado=False
        while(encontrado==False and sub_raiz is not None):
            if(elemento == sub_raiz.clave):
                encontrado=True
            elif(elemento<sub_raiz.clave):
                sub_raiz=sub_raiz.izq
            elif(elemento>sub_raiz.clave):
                sub_raiz=sub_raiz.der
        if(sub_raiz is None):
            return False
        if sub_raiz.izq is None and sub_raiz.der is None:
            if sub_raiz is self.raiz:
                self.raiz=None
                return True
            else:
                p=self.padre(self.raiz,sub_raiz.clave)
                while p.izq is not sub_raiz and p.der is not sub_raiz:
                    if(sub_raiz.clave<p.clave):
                        p=p.izq
                    elif(sub_raiz.clave>p.clave):
                        p=p.der
                if(sub_raiz is p.izq):
                    p.izq=None
                elif(sub_raiz is p.der):
                    p.der=None
                return True
            return True
        elif sub_raiz.izq is not None:
            c=sub_raiz.izq
            while(c.der is not None):
                c=c.der
            p=self.padre(self.raiz,c.clave)
            sub_raiz.clave=c.clave
            if p.izq is c:
                if c.izq is not None:
                    p.izq=c.izq
                else:
                    p.izq=None
            if p.der is c:
                if c.izq is not None:
                    p.der=c.izq
                else:
                    p.der=None
            return True
        elif sub_raiz.der is not None:
            if sub_raiz is self.raiz:
                self.raiz=self.raiz.der
                return True
            else:
                p=self.padre(self.raiz,sub_raiz.clave)
                if(sub_raiz is p.izq):
                    p.izq=sub_raiz.der
                elif(sub_raiz is p.der):
                    p.der=sub_raiz.der
                return True
            
    def num_hojas(self):
        if self.raiz is None:
            return 0
        return self.__num_hojas(self.raiz)
    
    def __num_hojas(self,subraiz):
        aux=0
        if subraiz.der is None and subraiz.izq is None:         
            return 1
        if subraiz.der is not None:
            aux+=self.__num_hojas(subraiz.der) 
        if subraiz.izq is not None:
            aux+=self.__num_hojas(subraiz.izq)
        
        return aux
            
        
            
       
    
    

if __name__=='__main__':
    print("Prueva 1")
    arbol = ArbolBinBus()
    arbol.insertar(10)
    arbol.insertar(8)
    arbol.insertar(9)
    arbol.insertar(3)
    arbol.insertar(11)
    print(arbol.num_hojas())
    print(arbol.eliminar(8))
    pre_orden(arbol)
    print("//////////////////////////////////////////\n")
    print("Prueva 2")
    arbol2 = ArbolBinBus()
    arbol2.insertar(10)
    arbol2.insertar(12)
    arbol2.insertar(11)
    arbol2.insertar(13)
    arbol2.insertar(15)
    print(arbol2.num_hojas())
    print(arbol2.eliminar(10))
    pre_orden(arbol2)
    print("//////////////////////////////////////////\n")
    print("Prueva 3")
    arbol3 = ArbolBinBus()
    arbol3.insertar(10)
    arbol3.insertar(8)
    arbol3.insertar(6)
    arbol3.insertar(9)
    arbol3.insertar(7)
    arbol3.insertar(5)
    arbol3.insertar(2)
    arbol3.insertar(1)
    arbol3.insertar(4)
    arbol3.insertar(3)
    arbol3.insertar(11)
    arbol3.insertar(14)
    arbol3.insertar(12)
    arbol3.insertar(13)
    print(arbol3.num_hojas())
    print(arbol3.eliminar(10))
    print(arbol3.eliminar(14))
    print(arbol3.eliminar(11))
    print(arbol3.eliminar(2))
    pre_orden(arbol3)
    
    print("//////////////////////////////////////////\n")
    print("Prueva 4")
    arbol4 = ArbolBinBus()
    arbol4.insertar(10)
    arbol4.insertar(5)
    arbol4.insertar(2)
    arbol4.insertar(7)
    arbol4.insertar(1)
    arbol4.insertar(3)
    arbol4.insertar(6)
    arbol4.insertar(8)
    arbol4.insertar(15)
    arbol4.insertar(12)
    arbol4.insertar(11)
    arbol4.insertar(13)
    arbol4.insertar(17)
    arbol4.insertar(16)
    arbol4.insertar(18)
    print(arbol4.num_hojas())
    pre_orden(arbol4)
    
   
