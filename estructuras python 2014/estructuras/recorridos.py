def pre_orden(arbol_bin, con_hijos=True):
    __pre_orden(arbol_bin.raiz, con_hijos)


def __pre_orden(sub_raiz, con_hijos):
    if sub_raiz is not None:
        __visitar_nodo(sub_raiz, con_hijos)
        __pre_orden(sub_raiz.izq, con_hijos)
        __pre_orden(sub_raiz.der, con_hijos)


def __visitar_nodo(sub_raiz, con_hijos=True):
    print('[' + str(sub_raiz.clave) + ']')
    if con_hijos:
        print(('O' if sub_raiz.izq is not None else 'X') + ':' +
              ('O' if sub_raiz.der is not None else 'X'))


def in_orden(arbol_bin, con_hijos=True):
    __in_orden(arbol_bin.raiz, con_hijos)


def __in_orden(sub_raiz, con_hijos):
    if sub_raiz is not None:
        __in_orden(sub_raiz.izq, con_hijos)
        __visitar_nodo(sub_raiz, con_hijos)
        __in_orden(sub_raiz.der, con_hijos)


def post_orden(arbol_bin, con_hijos=True):
    __post_orden(arbol_bin.raiz, con_hijos)


def __post_orden(sub_raiz, con_hijos):
    if sub_raiz is not None:
        __post_orden(sub_raiz.izq, con_hijos)
        __post_orden(sub_raiz.der, con_hijos)
        __visitar_nodo(sub_raiz, con_hijos)

