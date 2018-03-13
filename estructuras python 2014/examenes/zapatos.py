#!/usr/bin/env python3
"""
    PROJECT: zapatos

    MODULE: zapatos.py

    DESCRIPTION:
    Construir un programa, que utilizando una Lista Simplemente Enlazada,
    permita llevar el inventario/venta de una empresa de zapatos.

    DATE: 16.03.2016 13:00:07 COT

    AUTHORS: Miguel Rodriguez
"""
from listase import ListaSimplementeEnlazada

class Zapato:
    """
    Un Zapato se caracteriza porque debe tener en cuenta:
    - la marca
    - la referencia
    - origen
    - costo (de compra al proveedor.  Validar que sea un valor superior a cero
             siempre, incluso cuando se quiera modificar este valor cuando el
             objeto zapato esté creado)
    - existencia (unidades de zapatos, como mínimo deben ser 5 unidades las
                  que se compran para poder crear el zapato. De lo contrario
                  generara una excepción por valor incorrecto. Este valor podrá
                  ser modificado una vez el objeto zapato este creado, incluso
                  con un valor inferior a 5 unidades)
    """

    # Escriba y documente el constructor de la clase AQUI, con el mismo orden
    # para los parámetros del constructor de las caracteristicas de la clase
    def __init__(self, marca, referencia, origen, costo = 0, existencias = 5):
        self.marca = marca
        self.referencia = referencia
        self.origen = origen
        self.costo = costo
        if existencias < 5 or existencias is None :
            raise ValueError("Valor Incorrecto. la existencia debe ser >=5")
            #print(self)
            #self = None

        else:
            self.existencias = existencias

    # Método Z # 1
    def __eq__(self, otro):
        """
        Método de comparción de un zapato, teniendo en cuenta la marca, la
        referencia y el origen.

        :param otro: El otro zapato con el cual se van a ser las comparaciones
        :type otro: Zapato
        :returns: True si los zapatos son iguales. False en caso contrario
        :rtype: bool
        """
        return (isinstance(otro, Zapato) and (self.marca is otro.marca) and
                (self.referencia is otro.referencia) and
                (self.origen is otro.origen))

    # Método Z # 2
    def __str__(self):
        """
        Método de presentación de un zapato.

        :returns: Una cadena con el formato:
            <marca:referencia -- $costo -- existencia>
        :rtype: str
        """
        return ("<"+self.marca+":"+self.referencia+" -- $"+str(self.costo)+" -- "+
                str(self.existencias))

    @property
    def costo(self):
        return self.__costo

    @costo.setter
    def costo(self, nuevo_costo):
        if nuevo_costo < 0 or nuevo_costo is None:
            raise ValueError("Valor Incorrecto")
        else:
            self.__costo = nuevo_costo




class AlmacénZapatos:
    """
    Una almacén de zapatos se caracteriza por tener:
    - nombre del almacén
    y debe manejar una lista de todos los zapatos existentes en el inventario
    """

    # Escriba y documente el constructor de la clase AQUI, con el mismo orden
    # para los parámetros del constructor de las caracteristicas de la clase
    def __init__(self, nombre):
        self.nombre = nombre
        self.tamaño = 0
        self.lst_almacen = ListaSimplementeEnlazada("inventario"+nombre)
    # Método AZ # 1
    def nacionales(self, un_zapato):
        """
        Método que adiciona una referencia de zapato a el inventario del
        almacén.  Se deberá validar que únicamente ingresen zapatos de origen
        "colombia".
        Puede ser que el tipo de zapato ya exista en el inventario, en
        ese caso, NO se deberá adicionar el zapato.

        :param un_zapato: El zapato a ser adicionado al inventario del almacén
        :type un_zapato: Zapato
        :returns: True si el zapato fue agregado al inventario de forma
        satisfactoria. False en caso contrario
        :rtype: bool
        """
        zapato = self.lst_almacen.encontrar(un_zapato)
        if zapato == un_zapato:
            return False
        else:
            if un_zapato.origen == "colombia":
                retorno = self.lst_almacen.adicionar(un_zapato)
                if retorno is True:
                    self.tamaño +=1
                return retorno

            return False


    # Método AZ # 2
    def importados(self, un_zapato):
        """
        Método que adiciona una referencia de zapato a el inventario del
        almacén.  Se deberá validar que únicamente ingresen zapatos de origen
        extranjero.
        Puede ser que el tipo de zapato ya exista en el inventario, en
        ese caso, únicamente se deberá modificar la existencia del zapato en
        inventario, agregando el valor de la existencia del zapato que iba a
        ser adicionado y además, el costo del zapato se modificará al promedio
        del costo del zapato en inventario y del zapato que iba a ser
        adicionado. Por ejemplo, si el zapato a adicionar XYZ tiene 15 pares y
        su costo es de $30000, y éste ya se encuentra en el inventario con 20
        pares y un costo de $20000, entonces se deberá modificar el par de
        zapatos en el inventario ahora con una cantidad igual a 35 pares y un
        costo de $25000.

        :param un_zapato: El zapato a ser adicionado al inventario del almacén
        :type un_zapato: Zapato
        :returns: El costo y las existencias del zapato, como una tupla, si el
        zapato fue agregado/modificado al inventario de forma satisfactoria:
                (costo, existencias)
        En caso contrario retornar una tupla con valores de cero para el costo
        y las existenciass:
                (0, 0)
        :rtype: tuple
        """
        if not self.lst_almacen.existe(un_zapato):
            if un_zapato.origen != "colombia":
                self.lst_almacen.adicionar(un_zapato)
                tupla = (un_zapato.costo, un_zapato.existencias)
                self.tamaño +=1
                return (tupla)
        else:
            zapato = self.lst_almacen.encontrar(un_zapato)
            if zapato is not None:
                tipo=type(zapato)
                if isinstance(un_zapato,tipo):
                   zapato.existencias = zapato.existencias + un_zapato.existencias

                   zapato.costo = ((zapato.costo + un_zapato.costo)/2)
                   tupla = (zapato.costo, zapato.existencias)
                   return(tupla)
        tupla =0, 0
        return (tupla)

    # Método AZ # 3
    def posicionar_zapato(self, un_zapato, pos):
        """
        Método que ingresa un nuevo zapato al inventario, en una posición
        determinada. Se deberá validar que el zapato que ingresa sea único en
        el inventario.

        :param un_zapato: El zapato a ser insertado en una posición del
        inventario del almacén
        :type un_zapato: Zapato
        :param pos: Un valor con la posición del inventario a ser insertado el
        zapato.
        :type pos: int
        :returns: True si se pudo insertar el zapato al inventario. False en
        caso contrario.
        :rtype: bool
        """

        if pos >=0 and pos is not None:
            if not self.lst_almacen.existe(un_zapato):
                if self.tamaño >= pos:
                    self.lst_almacen.insertar(un_zapato, pos)
                    self.tamaño +=1
                    return True

        return False

    # Método AZ # 4
    def desposicionar_zapato(self, pos):
        """
        Método que quita un zapato del inventario en una posición determinada.

        :param pos: Un valor con la posición del inventario a ser removido el
        zapato.
        :type pos: int
        :returns: True si se pudo remover el zapato del inventario. False en
        caso contrario.
        :rtype: bool
        """
        if pos>= 0:
            if self.lst_almacen.eliminar_pos(pos):
                self.tamaño -=1
                return True
        return False

    # Método AZ # 5
    def vender_zapato(self, un_zapato, cantidad):
        """
        Método que realiza la venta de zapatos del inventario del almacén, de
        a cuerdo a una cantidad dada. Se debe validar que al menos exista la
        cantidad de zapatos a vender y que la cantidad a vender sea mayor que
        cero. Es necesario calcular el precio de venta total de los pares de
        zapatos, el cual correponderá a un 30% del costo de compra del zapato.
        Si se venden todas las existencias del zapato, éste deberá salir del
        inventario.

        :param un_zapato: El zapato a ser vendido del inventario del almacén.
        :type un_zapato: Zapato
        :param cantidad: La cantidad de pares de zapatos a ser vendida.
        :type cantidad: int
        :returns: El costo total de venta de los pares de zapatos vendidos, si
        el zapato es vendido de forma satisfactoria. De lo contrario la venta,
        se devolverá el valor -1.0.
        :rtype: float
        """
        if not self.lst_almacen.existe(un_zapato):
            return (-1.0)

        zapato = self.lst_almacen.encontrar(un_zapato)
        if zapato.existencias >= cantidad and cantidad > 0:
            zapato.existencias = zapato.existencias - cantidad
            venta = cantidad * zapato.costo
            ventap = venta*0.3
            if zapato.existencias == 0:
                self.lst_almacen.eliminar_dato(zapato)
                self.tamaño -=1
            return (ventap)
        return (-1.0)

    # Método AZ # 6
    def buscar_en_inventario(self, un_zapato):
        """
        Método que busca en el inventario de un almacén un determinado calzado
        según su marca, referencia y origen.

        :param un_zapato: El zapato a ser buscado en el inventario.
        :type un_zapato: Zapato
        :returns: Si el zapato existe, una cadena con la información del nombre
        del almacén y toda la información del zapato en el formato:
            [nombre del almacén] / <marca:referencia -- $costo -- existencia>
        Si no existe, una cadena vacía "".
        :rtype: str
        """
        if un_zapato.costo is None and un_zapato.existencias is None:
            return ""

        #if self.lst_almacen.existe(un_zapato):
        if un_zapato is None:
            return ""

        zapato = self.lst_almacen.encontrar(un_zapato)

        if zapato is None:
            return ""

        msj = ("[" + self.nombre + "] / " + un_zapato.marca + ":"
                + un_zapato.referencia+" -- $" + str(zapato.costo)
                + " -- " + str(zapato.existencias) + " pares")
        return msj
        return ("")

    # Método AZ # 7
    def ver_inventario(self):
        """
        Método que permite visualizar el inventario actual del almacén de
        zapatos.
        """
        self.lst_almacen.recorrer()

    # Método AZ # 8
    def __len__(self):
        """
        Método que ...

        :returns: ... retorna el número de pares de zapatos que se encuentran
        actualmente en el inventario del almacén.
        :rtype: int
        """
        return self.tamaño


if __name__ == "__main__":
    zap1 = Zapato("mar_1", "ref_1", "colombia", 10000, 8)
    zap2 = Zapato("mar_2", "ref_1", "usa", 20000, 5)
    zap3 = Zapato("mar_1", "ref_1", "colombia", 30000, 5)
    zap4 = Zapato("mar_4", "ref_1", "china", 4000, 10)
    zap5 = Zapato("mar_5", "ref_1", "colombia", 5000, 8)
    zap6 = Zapato("mar_6", "ref_1", "canada", 60000, 7)
    zap7 = Zapato("mar_7", "ref_1", "colombia", 70000, 6)
    zap8 = Zapato("mar_8", "ref_1", "méxico", 8000, 5)
    zap9 = Zapato("mar_9", "ref_1", "panamá", 9000, 7)
    zap10 = Zapato("mar_7", "ref_1", "colombia", 100000, 10)
    zap11 = Zapato("mar_11", "ref_1", "usa", 110000, 8)
    zap12 = Zapato("mar_12", "ref_1", "colombia", 120000, 7)

    print(zap7 == zap10)
