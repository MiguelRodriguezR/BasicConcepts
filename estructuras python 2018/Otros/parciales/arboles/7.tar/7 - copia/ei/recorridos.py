#!/usr/bin/env python3
#
# Project:
# File: recorridos.py
# Authors: (student 1 and student 2)
# Description:


def __visitar_nodo(sub_arbol, con_hijos=True):
    cadena = "["+str(sub_arbol)+"]"
    # print("["+str(sub_arbol)+"]")
    # if con_hijos:
    #     print(("O" if sub_arbol.izq is not None else "X") +
    #           ":"+("O" if sub_arbol.der is not None else "X"))
    return cadena


def __mostrar_nodo(sub_arbol, con_hijos=True):
    cadena = "["+str(sub_arbol)+"]"
    print("["+str(sub_arbol)+"]")
    return cadena


def pre_orden(arbol):
    return __pre_orden(arbol.raiz)

def str_pre_orden(arbol):
    return str__pre_orden(arbol.raiz)


def __pre_orden(sub_arbol):
    cadena = ""
    if sub_arbol is not None:
        cadena += __visitar_nodo(sub_arbol)
        cadena += __pre_orden(sub_arbol.izq)
        cadena += __pre_orden(sub_arbol.der)
    return cadena

def str__pre_orden(sub_arbol):
    cadena = ""
    if sub_arbol is not None:
        cadena += __mostrar_nodo(sub_arbol)
        cadena += __pre_orden(sub_arbol.izq)
        cadena += __pre_orden(sub_arbol.der)
    return cadena


def in_orden(arbol):
    return __in_orden(arbol.raiz)

def str_in_orden(arbol):
    return str__in_orden(arbol.raiz)


def __in_orden(sub_arbol):
    cadena = ""
    if sub_arbol is not None:
        cadena += str(__in_orden(sub_arbol.izq))
        cadena += str(__visitar_nodo(sub_arbol))
        cadena += str(__in_orden(sub_arbol.der))
    return cadena

def str__in_orden(sub_arbol):
    cadena = ""
    if sub_arbol is not None:
        cadena += __in_orden(sub_arbol.izq)
        cadena += __mostrar_nodo(sub_arbol)
        cadena += __in_orden(sub_arbol.der)
    return cadena


def post_orden(arbol):
    return __post_orden(arbol.raiz)

def str_post_orden(arbol):
    return str__post_orden(arbol.raiz)


def __post_orden(sub_arbol):
    cadena = ""
    if sub_arbol is not None:
        cadena += str(__post_orden(sub_arbol.izq))
        cadena += str(__post_orden(sub_arbol.der))
        cadena += str(__visitar_nodo(sub_arbol))
    return cadena

def str__post_orden(sub_arbol):
    cadena = ""
    if sub_arbol is not None:
        cadena += __post_orden(sub_arbol.izq)
        cadena += __post_orden(sub_arbol.der)
        cadena += __mostrar_nodo(sub_arbol)
    return cadena
