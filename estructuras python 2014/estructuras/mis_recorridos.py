#!/usr/bin/env python3
#
# Proyecto:
# Archivo: mis_recorridos.py
# Autores: (Miguel Rodriguez)
# Fecha: 23.05.2014 09:27:44 UTC
# Descripción:


def pre_orden(arbol_binario):
    __pre_orden(arbol_binario.raiz)


def __pre_orden(sub_raiz):
    if sub_raiz is not None:
        __ver__nodo(sub_raiz)
        __pre_orden(sub_raiz.izq)
        __pre_orden(sub_raiz.der)


def in_orden(arbol_binario):
    __pre_orden(arbol_binario.raiz)


def __in_orden(sub_raiz):
    if sub_raiz is not None:
        __pre_orden(sub_raiz.izq)
        __ver__nodo(sub_raiz)
        __pre_orden(sub_raiz.der)


def post_orden(arbol_binario):
    __pre_orden(arbol_binario.raiz)


def __post_orden(sub_raiz):
    if sub_raiz is not None:
        __pre_orden(sub_raiz.izq)
        __pre_orden(sub_raiz.der)
        __ver__nodo(sub_raiz)


def __ver__nodo(sub_raiz):
    print("[" + str(sub_raiz.clave) + "]")
    print(("O" if sub_raiz.izq is not None else "X") + ":" +
          ("O" if sub_raiz.der is not None else "X"))
