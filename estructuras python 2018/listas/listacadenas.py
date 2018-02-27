from listas import LSE


lista_cad = LSE()
lista_cad.agregar('j')
lista_cad.agregar('u')
lista_cad.agregar('a')
lista_cad.agregar('n')
lista_cad.remover(2)
lista_cad.recorrer()
print(lista_cad.homogeneidad("perrito"))

lista_cas = LSE()
lista_cas.agregar(1)
lista_cas.agregar(1)
lista_cas.agregar(2)
lista_cas.agregar(1)
lista_cas.agregar(3)
lista_cas.agregar(4)
lista_cas.agregar(5)
lista_cas.agregar(5)
lista_cas.remover(3,False)
lista_cas.recorrer()
#
