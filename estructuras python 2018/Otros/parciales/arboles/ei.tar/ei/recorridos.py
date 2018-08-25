#!/usr/bin/env python3
#
# Project:
# File: recorridos.py
# Authors: (student 1 and student 2)
# Date: 28.04.2016 14:49:09 COT
# Description:


def __visitar_nodo(sub_arbol, con_hijos=True):
    print("["+str(sub_arbol)+"]")
    if con_hijos:
        print(("O" if sub_arbol.izq is not None else "X") +
              ":"+("O" if sub_arbol.der is not None else "X"))


def pre_orden(arbol):
    __pre_orden(arbol.raiz)


def __pre_orden(sub_arbol):
    if sub_arbol is not None:
        __visitar_nodo(sub_arbol)
        __pre_orden(sub_arbol.izq)
        __pre_orden(sub_arbol.der)


def in_orden(arbol):
    __in_orden(arbol.raiz)


def __in_orden(sub_arbol):
    if sub_arbol is not None:
        __in_orden(sub_arbol.izq)
        __visitar_nodo(sub_arbol)
        __in_orden(sub_arbol.der)


def post_orden(arbol):
    __post_orden(arbol.raiz)


def __post_orden(sub_arbol):
    if sub_arbol is not None:
        __post_orden(sub_arbol.izq)
        __post_orden(sub_arbol.der)
        __visitar_nodo(sub_arbol)


def pre_orden_str(arbol):
    pass
    "Devuelve una cadena de todos los valores que tenga ese arbol solo
    los valores"
