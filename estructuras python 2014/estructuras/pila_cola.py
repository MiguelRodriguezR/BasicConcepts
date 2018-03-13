from nodolse import NodoLSE


def validar_homogeneidad(nodo,dato):
	if nodo is not None:
		if isinstance(dato,type(nodo.dato)):
			return True
	return False

class Objeto1():
	"""docstring for objeto1"""
	def __init__(self,num):
		self.num=num

	def __str__(self):
		return("Clase Objeto1..."+str(self.num))

class Objeto2():
	"""docstring for objeto2"""
	def __init__(self,num):
		self.num=num

	def __str__(self):
		return("Clase Objeto2..."+str(self.num))
		


class NodoPila(NodoLSE):
	pass
		
class Pila:
	
	def __init__(self):
		self.__cima = None
		
	def es_vacia(self):
		return(self.__cima is None)
	
	def apilar(self, nuevo_dato):
		nuevo_nodo = NodoPila(nuevo_dato)
		bApilo = True
		if self.es_vacia():
			self.__cima = nuevo_nodo
		else:
			if validar_homogeneidad(self.__cima,nuevo_dato):
				nuevo_nodo.sig = self.__cima
				self.__cima = nuevo_nodo
			
			else:
				bApilo = False
		return bApilo
				
	
	def desapilar(self):
		if self.es_vacia():
			return None
		else:
			un_dato = self.__cima.dato
			self.__cima = self.__cima.sig
			return un_dato
			
	def cima(self):
		return(None if self.es_vacia() else self.__cima.dato)
	
	def __len__(self):
		pass
		
class NodoCola(NodoLSE):
	pass
			
class Cola:
	def __init__(self):
		self.__frente = None
		self.__final = None
		self.__tamano = 0
		
	def es_vacia(self):
		return(self.__frente is None)
	
	def encolar(self, nuevo_dato):
		nuevo_nodo = NodoCola(nuevo_dato)
		if self.es_vacia():
			self.__frente = nuevo_nodo
			self.__tamano += 1
			return True
		else:
			if validar_homogeneidad(self.__frente,nuevo_dato):
				nodo_actual = self.__frente
				while nodo_actual.sig is not None:
					nodo_actual = nodo_actual.sig
				nodo_actual.sig = nuevo_nodo
				self.__final = nuevo_nodo
				self.__tamano += 1
				return True
		return False
			

	def desencolar(self):
		if self.es_vacia():
			return None
		else:
			un_dato = self.__frente.dato
			self.__frente = self.__frente.sig
			return un_dato


	def frente(self):
		return(None if self.es_vacia() else self.__frente.dato)
	
	def __len__(self):
		return __tamano
			
if __name__ == '__main__':
	#creando objetos
	o11=Objeto1(1)
	num=2
	o12=Objeto1(2)
	o21=Objeto2(1)

	print("---------TEST PILA ----------") 
	pila = Pila()
	#probando objetos
	pila.apilar(o11)
	pila.apilar(num)
	pila.apilar(o21)
	pila.apilar(o12)
	print(str(pila.desapilar()))
	print(str(pila.desapilar()))
	print(str(pila.desapilar()))

	print("---------TEST COLA ----------") 
	cola = Cola()
	#probando objetos
	cola.encolar(o11)
	cola.encolar(num)
	cola.encolar(o21)
	cola.encolar(o12)
	print(str(cola.desencolar()))
	print(str(cola.desencolar()))
	print(str(cola.desencolar()))
    

