#!/usr/bin/env python3
#
# Proyecto:
# Archivo: mi_arbol_binario.py
# Autores: (nombres y apellidos)
# Fecha: 30.05.2014 08:06:56 UTC
# Descripción:
from mi_arbol import NodoArbBin, ArbolBinario
from mis_recorridos import pre_orden


class ArbolBinarioBus(ArbolBinario):

    def insertar(self, nueva_clave):
        self.raiz = self.__insertar(self.raiz, nueva_clave)

    def __insertar(self, sub_raiz, nueva_clave):
        if sub_raiz is None:
            sub_raiz = NodoArbBin(nueva_clave)
        elif sub_raiz.clave == nueva_clave:
            print("No podéis insertar la clave" + str(nueva_clave))
        elif nueva_clave < sub_raiz.clave:
            sub_raiz.izq = self.__insertar(sub_raiz.izq, nueva_clave)
        else:
            sub_raiz.der = self.__insertar(sub_raiz.der, nueva_clave)
        return sub_raiz

    def buscar(self, clave_buscar):
        return self.__buscar(self.raiz, clave_buscar)

    def __buscar(self, sub_raiz, clave_buscar):
        if sub_raiz is None:
            return False
        elif sub_raiz.clave == clave_buscar:
            return True
        elif clave_buscar < sub_raiz.clave:
            return self.__buscar(sub_raiz.izq, clave_buscar)
        else:
            return self.__buscar(sub_raiz.der, clave_buscar)

    def eliminar(self, clave_elm):
        """
        Metodo que permite eliminar un nodo por su clave.
        retorna True, si es eliminado y False en caso contrario
        tiene que reacomodar los hijos volverse padre
        """
        #encontrando el nodo a eliminar
        sub_raiz=self.raiz
        encontrado=False
        while(encontrado==False and sub_raiz is not None):
            if(clave_elm == sub_raiz.clave):
                encontrado=True
            elif(clave_elm<sub_raiz.clave):
                sub_raiz=sub_raiz.izq
            elif(clave_elm>sub_raiz.clave):
                sub_raiz=sub_raiz.der
                
        #comprovando posivilidades de eliminacion en nulo
        if(sub_raiz is None):
            return False
        
        #comprovando posivilidades de eliminacion en verdadero
        #hijosporizquierda
        if sub_raiz.izq is not None:
            
            #encontrando el mayor hijo por el lado izquierdo
            cambio=sub_raiz.izq
            while(cambio.der is not None):
                cambio=cambio.der
            
            #encontrando al padre del cambio
            padre=sub_raiz
            while padre.izq is not cambio and padre.der is not cambio:
                if(cambio.clave<padre.clave):
                    padre=padre.izq
                elif(cambio.clave>padre.clave):
                    padre=padre.der
            
            #remplazar el valor de sub_raiz por cambio
            sub_raiz.clave=cambio.clave
            
            #eliminar el cambio
            if padre.izq is cambio:
                if cambio.izq is not None:
                    padre.izq=cambio.izq
                else:
                    padre.izq=None
                
            if padre.der is cambio:
                if cambio.izq is not None:
                    padre.der=cambio.izq
                else:
                    padre.der=None
                    
            #retornar verdadero
            return True
                
        #hijos por derecha
        elif sub_raiz.der is not None:
            
            #comprovar si la raiz a eliminar es la raiz principal 
            if sub_raiz is self.raiz:
                #procedemos a remplazarla
                self.raiz=self.raiz.der
                return True
            
            else:
                #encontrar al padre del nodo a eliminar
                padre=self.raiz
                while padre.izq is not sub_raiz and padre.der is not sub_raiz:
                    if(sub_raiz.clave<padre.clave):
                        padre=padre.izq
                    elif(sub_raiz.clave>padre.clave):
                        padre=padre.der
                
                #comprovar la posicion del nodo a eliminar
                if(sub_raiz is padre.izq):
                    padre.izq=sub_raiz.der
                elif(sub_raiz is padre.der):
                    padre.der=sub_raiz.der
                return True
            
        #sin hijos
        elif sub_raiz.izq is None and sub_raiz.der is None:
            
            #comprovar si la raiz a eliminar es la raiz principal
            if sub_raiz is self.raiz:
                #procedemos a eliminarla
                self.raiz=None
                return True
            
            else:
                #encontrar al padre del nodo a eliminar
                padre=self.raiz
                while padre.izq is not sub_raiz and padre.der is not sub_raiz:
                    if(sub_raiz.clave<padre.clave):
                        padre=padre.izq
                    elif(sub_raiz.clave>padre.clave):
                        padre=padre.der
                        
                #comprovar la posicion del nodo a eliminar
                if(sub_raiz is padre.izq):
                    padre.izq=None
                elif(sub_raiz is padre.der):
                    padre.der=None
                return True
        return True
                        
        
                

    def encontrar(self, clave_enc):
        """
        Metodo que encuentra y devuelve la clave a ser encontrada en
        el arbol. Si no existe la clave se retorna None
        """
        return self.__encontrar(self.raiz, clave_enc)
    
    def __encontrar(self,sub_raiz,clave_enc):
        if sub_raiz is None:
            return None
        elif sub_raiz.clave == clave_enc:
            return sub_raiz.clave
        elif clave_enc < sub_raiz.clave:
            return self.__encontrar(sub_raiz.izq, clave_enc)
        else:
            return self.__encontrar(sub_raiz.der, clave_enc)
        
        
    def numero_de_hojas(self):
        if self.raiz is None:
            return 0
        #en el caso de que solo exista la raiz
        if self.raiz.izq is None and self.raiz.der is None:
            return 1
        
        #buscar ojas por metodo recursivo
        return self.__numero_de_hojas(self.raiz)
    
    def __numero_de_hojas(self,subraiz):
        
        numero=0
        #verificacion de hoja
        if subraiz.der is None and subraiz.izq is None:         
            return 1
        
        #verificar por derecha
        if subraiz.der is not None:
            numero+=self.__numero_de_hojas(subraiz.der)
            
        #verificar por izquierda    
        if subraiz.izq is not None:
            numero+=self.__numero_de_hojas(subraiz.izq)
        
        return numero
        
        
        
          
        

if __name__=='__main__':
    
    print("Prueva 1")
    arbol = ArbolBinarioBus()
    arbol.insertar(10)
    arbol.insertar(8)
    arbol.insertar(9)
    arbol.insertar(3)
    arbol.insertar(11)
    print(arbol.numero_de_hojas())
    print(arbol.eliminar(8))
    pre_orden(arbol)
    print("//////////////////////////////////////////\n")
    print("Prueva 2")
    arbol2 = ArbolBinarioBus()
    arbol2.insertar(10)
    arbol2.insertar(12)
    arbol2.insertar(11)
    arbol2.insertar(13)
    arbol2.insertar(15)
    print(arbol2.numero_de_hojas())
    print(arbol2.eliminar(10))
    pre_orden(arbol2)
    print("//////////////////////////////////////////\n")
    print("Prueva 3")
    arbol3 = ArbolBinarioBus()
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
    print(arbol3.numero_de_hojas())
    print(arbol3.eliminar(10))
    print(arbol3.eliminar(14))
    print(arbol3.eliminar(11))
    print(arbol3.eliminar(2))
    pre_orden(arbol3)
    
    print("//////////////////////////////////////////\n")
    print("Prueva 4")
    arbol4 = ArbolBinarioBus()
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
    print(arbol4.numero_de_hojas())
    pre_orden(arbol4)
    
