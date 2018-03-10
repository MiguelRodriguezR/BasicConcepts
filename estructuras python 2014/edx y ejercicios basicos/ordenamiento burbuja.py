lista=[]
print("0 para terminar el proceso")
elemento=1
while elemento!=0:
    elemento=int(input("Ingrese un elemento: "))
    lista.append(elemento)


def burbuja():

    for recorrido in range(1,len(lista)):
        for posicion in range(len(lista)-recorrido):
            if lista[posicion]>lista[posicion+1]:
                aux=lista[posicion]
                lista[posicion]=lista[posicion+1]
                lista[posicion+1]=aux

    return lista


print (burbuja())
