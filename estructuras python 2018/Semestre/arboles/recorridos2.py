def __ver_nodo(sub_arbol):
    print(f"[{sub_arbol.clave}]")
    print('O' if sub_arbol.izq is not None else 'X', end=':')
    print('O' if sub_arbol.der is not None else 'X')

def pre_orden(arbol_bin, con_hijos=True):
    __pre_orden(arbol_bin.raiz, con_hijos)


def __pre_orden(sub_raiz, con_hijos):
    if sub_raiz is not None:
        __ver_nodo(sub_raiz)
        __pre_orden(sub_raiz.izq, con_hijos)
        __pre_orden(sub_raiz.der, con_hijos)


# Tarea
def in_orden(arbol_bin, con_hijos=True):
    __in_orden(arbol_bin.raiz, con_hijos)


def __in_orden(sub_raiz, con_hijos):
    if sub_raiz is not None:
        __in_orden(sub_raiz.izq, con_hijos)
        __ver_nodo(sub_raiz)
        __in_orden(sub_raiz.der, con_hijos)


def post_orden(arbol_bin, con_hijos=True):
    __post_orden(arbol_bin.raiz, con_hijos)


def __post_orden(sub_raiz, con_hijos):
    if sub_raiz is not None:
        __post_orden(sub_raiz.izq, con_hijos)
        __post_orden(sub_raiz.der, con_hijos)
        __ver_nodo(sub_raiz)
