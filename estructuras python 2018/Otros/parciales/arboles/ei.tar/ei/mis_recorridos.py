def pre_orden(arbol_binario):

    __pre_orden(arbol_binario.raiz)


def __pre_orden(sub_raiz):

    if (sub_raiz is not None):
        __ver_nodo(sub_raiz)
        __pre_orden(sub_raiz.izq)
        __pre_orden(sub_raiz.der)


def in_orden(arbol_binario):
    __in_orden(arbol_binario.raiz)


def __in_orden(sub_raiz):

    if sub_raiz is not None:

        __in_orden(sub_raiz.izq)
        __ver_nodo(sub_raiz)
        __in_orden(sub_raiz.der)


def pos_orden(arbol_binario):
    __pos_orden(arbol_binario.raiz)


def __pos_orden(sub_raiz):

    if sub_raiz is not None:

        __in_orden(sub_raiz.izq)
        __in_orden(sub_raiz.der)
        __ver_nodo(sub_raiz)


def __ver_nodo(sub_raiz):

    print("[" + str(sub_raiz.clave) + "]")
    print(("O" if sub_raiz.izq is not None else "X")+" : " +
          ("O" if sub_raiz.der is not None else "X"))
