"""
1- Construir una clase Premio con:
a) un nombre y un valor en pesos.
b) un método que pueda verificar la igualdad con otro, teniendo en cuenta su
nombre y valor
c) la presentación del Premio con el formato: [nombre_premio : $valor]

2- Cronstruir una clase Sorteo, que permita lo siguiente:
a) tener una fecha de sorteo
b) tener una lista de premios
c) un método que permita agregar un nuevo premio
d) un método que permita quitar todos los premios coincidentes con otro premio
e) un método que permita encontrar un premio en la lista de premios
f) un método que permita cuantificar el valor total de los premios del sorteo
g) un método que permita sortear un premio por su posición relativa y devolver
el premio correspondiente o None si el valor de la posición es negativa
h) Escribir en pantalla los premios del sorteo con la notación:
    Sorteo fecha_sorteo {[prm-1 : $valor-prm-1] [prm-2 : $valor-prm-2],...etc}
"""
from listas_SEC import ListaSEC


class Premio:

    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

    def __eq__(self, otro_Premio):
        return (isinstance(otro_Premio, Premio) and self.nombre ==
                otro_Premio.nombre and self.valor == otro_Premio.valor)

    def __str__(self):
        return ("[" + str(self.nombre) + " : $" + str(self.valor) + "]")


class Sorteo:

    def __init__(self, fecha):
        self.fecha = fecha
        self.lista_premios = ListaSEC()

    def agregar(self, premio):
        self.lista_premios.adicionar(premio)

    def quitar(self, premio):
        for i in self.lista_premios:
            if(i == premio):
                self.lista_premios.eliminar(i)

    def encontrar(self, premio):
        for i in self.lista_premios:
            if(i == premio):
                return True
        return False

    def pozo(self):
        acumulado = 0
        for i in self.lista_premios:
            acumulado += i.valor
        return acumulado

    def sortear(self, posicion):
        if(posicion < 0):
            return None
        return self.lista_premios.ruletaRusa(posicion)

    def __str__(self):
        cont = 0
        texto = "Sorteo " + str(self.fecha) + " {"
        for i in self.lista_premios:
            cont += 1
            texto = texto + str(i)
            if(cont < self.lista_premios.tam):
                texto = texto + " "
        texto = texto + "}"
        return texto


if __name__ == '__main__':
    sorteo = Sorteo("20-3-11")
    prm6 = Premio('Auto Maxda 3.1', 36740000)
    sorteo.agregar(prm6)
    sorteo.agregar(prm6)
    print(sorteo)
    print(sorteo.encontrar(Premio('Auro Maxda 3.1', 36740000)))
