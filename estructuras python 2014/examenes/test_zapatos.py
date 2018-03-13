7#!/usr/bin/env python3
from test_builder import TestBuilder, RED, printout
from zapatos import AlmacénZapatos, Zapato
import unittest
import traceback
VIEW_LIST = False


def gen_lst_zapatos(origen):
    """
    Función especial que permite la creación de los zapatos utilizados en
    las diferentes pruebas, devolviendo una lista de tuplas con el zapato y
    un valor booleano que representa si el zapato será o no adicionado al
    inventario del almacén para zapatos nacionales. Si son importados en vez
    del valor booleano se devuelve una tupla con los valores del costo y las
    existencias del zapato que se adiciona. En cualquier otro caso se devuelve
    una lista con los zapatos nacionales e importados que se deberían adicionar
    al inventario sin ningún tipo de problema.
    """
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

    if origen == "colombia":
        lst_zaps = [(zap1, True), (zap2, False), (zap3, False), (zap4, False),
                    (zap5, True), (zap6, False), (zap7, True), (zap8, False),
                    (zap9, False), (zap10, False), (zap11, False),
                    (zap12, True)]
    elif origen == "cualquier país que no sea colombia":
        lst_zaps = [(zap1, (0, 0)), (zap2, (20000, 5)), (zap3, (0, 0)),
                    (zap4, (4000, 10)), (zap5, (0, 0)), (zap6, (60000, 7)),
                    (zap7, (0, 0)), (zap8, (8000, 5)), (zap9, (9000, 7)),
                    (zap10, (0, 0)), (zap11, (110000, 8)), (zap12, (0, 0))]
    else:
        lst_zaps = [zap1, zap5, zap7, zap12, zap2, zap4, zap6, zap8, zap9,
                    zap11]
    return lst_zaps


class Zapatin:

    def __init__(self, marca, referencia, origen, c, e):
        self.marca = marca
        self.referencia = referencia
        self.origen = origen
        self.c = c
        self.e = e


class TestAlmacénZapatos(TestBuilder):
    # Es posible desactivar cualquiera de las pruebas colocando el valor de
    # cero a cualquiera de ellas en el siguiente diccionario:
    dict_pruebas = {"nacionales": 1, "importados": 1, "posicionar": 1,
                    "desposicionar": 1, "vender": 1, "buscar": 1}

    def setUp(self):
        # Creación del Almacén de Zapatos con un nombre inicial
        self.almc_zap = AlmacénZapatos("Zapatos ACME")

    def test_0(self):
        self.presentación("Test Almacén de Zapatos")

    def test_1_nacionales(self):
        iTest = 1
        sTitle = "Entrada de zapatos nacionales al inventario"
        fMax_nota = 0.8
        n_t1 = fMax_nota * 0.25 / 4
        n_t2 = fMax_nota * 0.25 / 9
        if self.dict_pruebas.get("nacionales"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Comprobación de la entrada de Zapatos nacionales al inventario
            lst_zaps = gen_lst_zapatos("colombia")
            n_t3 = fMax_nota * 0.5 / len(lst_zaps)
            cr_i = 0
            le = (traceback.extract_stack()[-1])[1] + 2
            for zap in lst_zaps:
                self.comprobarAserción(zap[1],
                                       self.almc_zap.nacionales(zap[0]),
                                       n_t3, le, cr_i)
                cr_i += 1

            # Comprobación del tamaño del inventario
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(4, len(self.almc_zap), n_t2, le)

            # Comprobación de la validación de números positivos para el costo
            # del zapato
            try:
                zap13 = Zapato("mar_13", "ref_1", "colombia", -5671, 10)
                self.almc_zap.nacionales(zap13)
            except ValueError as e:
                print(e)
                self.comprobarAserción(True, True, n_t1, 0)
            try:
                zap14 = Zapato("mar_14", "ref_1", "colombia", 0, 10)
                self.almc_zap.nacionales(zap14)
            except ValueError as e:
                print(e)
                self.comprobarAserción(True, True, n_t1, 0)
            try:
                zap15 = Zapato("mar_15", "ref_1", "colombia", 5000, 10)
                le = (traceback.extract_stack()[-1])[1] + 2
                # Comprobamos si la clase Zapato tiene el atributo de costo
                if hasattr(zap15, "costo"):
                    zap15.costo = 0
                else:
                    printout("ATENCION: Modificar las líneas " + str(le) +
                             " y " + str(le + 1) + " con el nombre del" +
                             " atributo de la clase Zapato que guarda" +
                             " el 'costo', para obtener una mejor" +
                             " calificación.\n\n", RED)
                self.almc_zap.nacionales(zap15)
            except ValueError as e:
                print(e)
                self.comprobarAserción(True, True, n_t1, 0)
            try:
                zap16 = Zapato("mar_16", "ref_1", "colombia", 5000, 10)
                le = (traceback.extract_stack()[-1])[1] + 2
                # Comprobamos si la clase Zapato tiene el atributo de costo
                if hasattr(zap16, "costo"):
                    zap16.costo = -1
                else:
                    printout("ATENCION: Modificar las líneas " + str(le) +
                             " y " + str(le + 1) + " con el nombre del" +
                             " atributo de la clase Zapato que guarda" +
                             " el 'costo', para obtener una mejor" +
                             " calificación.\n\n", RED)
                self.almc_zap.nacionales(zap16)
            except ValueError as e:
                print(e)
                self.comprobarAserción(True, True, n_t1, 0)

            # Comprobación de la validación de zapatos con variaciones en la
            # referencia que SI serán adicionados al inventario
            le = (traceback.extract_stack()[-1])[1] + 2
            zap1a = Zapato("mar_1", "ref_2", "colombia", 10000, 8)
            self.comprobarAserción(True, self.almc_zap.nacionales(zap1a),
                                   n_t2, le)
            le = (traceback.extract_stack()[-1])[1] + 2
            zap5a = Zapato("mar_5", "ref_3", "colombia", 5000, 13)
            self.comprobarAserción(True, self.almc_zap.nacionales(zap5a),
                                   n_t2, le)
            le = (traceback.extract_stack()[-1])[1] + 2
            zap7a = Zapato("mar_7", "ref_2", "colombia", 70000, 6)
            self.comprobarAserción(True, self.almc_zap.nacionales(zap7a),
                                   n_t2, le)

            # Comprobación del tamaño del inventario
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(7, len(self.almc_zap), n_t2, le)

            # Comprobación de la validación de zapatos ya existentes en el
            # inventario que NO serán adicionados
            le = (traceback.extract_stack()[-1])[1] + 2
            zap1c = Zapato("mar_1", "ref_1", "colombia", 10000, 8)
            self.comprobarAserción(False, self.almc_zap.nacionales(zap1c),
                                   n_t2, le)

            le = (traceback.extract_stack()[-1])[1] + 2
            zap5c = Zapato("mar_5", "ref_1", "colombia", 5000, 13)
            self.comprobarAserción(False, self.almc_zap.nacionales(zap5c),
                                   n_t2, le)

            # Validación de la Homogeneidad del inventario de Zapatos
            le = (traceback.extract_stack()[-1])[1] + 2
            zap1x = Zapatin("mar_1x", "ref_1x", "colombia", 700, 7)
            self.comprobarAserción(False, self.almc_zap.nacionales(zap1x),
                                   n_t2, le)

            # Comprobación del tamaño del inventario
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(7, len(self.almc_zap), n_t2, le)

            # VISUALIZACIÓN del Inventario actual del Almacén de Zapatos
            if VIEW_LIST:
                self.almc_zap.ver_inventario()
                input("[Enter] para continuar ...")

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_2_importados(self):
        iTest = 2
        sTitle = "Entrada de zapatos importados al inventario"
        fMax_nota = 1.0
        n_t1 = fMax_nota * 0.5 / 8
        if self.dict_pruebas.get("importados"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Comprobación de la entrada de Zapatos importados al inventario
            lst_zaps = gen_lst_zapatos("cualquier país que no sea colombia")
            n_t2 = fMax_nota * 0.5 / len(lst_zaps)
            cr_i = 0
            le = (traceback.extract_stack()[-1])[1] + 2
            for zap in lst_zaps:
                self.comprobarAserción(zap[1],
                                       self.almc_zap.importados(zap[0]),
                                       n_t2, le, cr_i)
                cr_i += 1

            # Comprobación de la no creación de zapatos cuando el valor de las
            # existencias es menor que 5 pares
            try:
                zap13 = Zapato("mar_13", "ref_1", "chile", 7000, 4)
                self.almc_zap.importados(zap13)
            except ValueError as e:
                print(e)
                self.comprobarAserción(True, True, n_t1, 0)
            try:
                zap14 = Zapato("mar_14", "ref_1", "perú", 7000, -7)
                self.almc_zap.importados(zap14)
            except ValueError as e:
                print(e)
                self.comprobarAserción(True, True, n_t1, 0)

            # Comprobación del tamaño del inventario
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(6, len(self.almc_zap), n_t1, le)

            # Importación de zapatos ya existentes en el inventario que
            # modificarán los valores del costo y de las existencias
            le = (traceback.extract_stack()[-1])[1] + 2
            zap2a = Zapato("mar_2", "ref_1", "usa", 30000, 10)
            self.comprobarAserción((25000, 15),
                                   self.almc_zap.importados(zap2a), n_t1, le)

            le = (traceback.extract_stack()[-1])[1] + 2
            zap11a = Zapato("mar_11", "ref_1", "usa", 340000, 15)
            self.comprobarAserción((225000, 23),
                                   self.almc_zap.importados(zap11a), n_t1, le)

            le = (traceback.extract_stack()[-1])[1] + 2
            zap8a = Zapato("mar_8", "ref_1", "méxico", 12000, 20)
            self.comprobarAserción((10000, 25),
                                   self.almc_zap.importados(zap8a), n_t1, le)

            # Validación de la Homogeneidad del inventario de Zapatos
            le = (traceback.extract_stack()[-1])[1] + 2
            zap1x = Zapatin("mar_1x", "ref_1x", "usa", 700, 7)
            self.comprobarAserción((0, 0), self.almc_zap.importados(zap1x),
                                   n_t1, le)

            # Comprobación del tamaño del inventario
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(6, len(self.almc_zap), n_t1, le)

            # VISUALIZACIÓN del Inventario actual del Almacén de Zapatos
            if VIEW_LIST:
                self.almc_zap.ver_inventario()
                input("[Enter] para continuar ...")
            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_3_posicionar(self):
        iTest = 3
        sTitle = "Posicionar zapatos en el inventario del almacén"
        fMax_nota = 1.0
        n_t = fMax_nota * 0.6 / 8
        if self.dict_pruebas.get("posicionar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Adición de zapatos cuando el inventario está vació
            zap0c = Zapato("mar_0", "ref_1", "colombia", 8000, 5)
            zap0u = Zapato("mar_0", "ref_1", "usa", 18000, 7)
            zap0m = Zapato("mar_0", "ref_1", "méxico", 12000, 6)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(False,
                                   self.almc_zap.posicionar_zapato(zap0c, -1),
                                   n_t, le)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(True,
                                   self.almc_zap.posicionar_zapato(zap0c, 0),
                                   n_t, le)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(False,
                                   self.almc_zap.posicionar_zapato(zap0u, 2),
                                   n_t, le)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(True,
                                   self.almc_zap.posicionar_zapato(zap0u, 1),
                                   n_t, le)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(True,
                                   self.almc_zap.posicionar_zapato(zap0m, 0),
                                   n_t, le)

            # Comprobación del tamaño del inventario
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(3, len(self.almc_zap), n_t, le)

            # Inserción de más Zapatos nacionales e importados al inventario
            lst_zaps = gen_lst_zapatos("")
            n_t2 = fMax_nota * 0.4 / len(lst_zaps)
            cr_i = 0
            posiciones = [(True, 3), (False, 5), (True, 0), (True, 5),
                          (False, -1), (True, 2), (True, 2), (False, 9),
                          (True, 0), (False, -2)]
            le = (traceback.extract_stack()[-1])[1] + 3
            for zap in lst_zaps:
                self.comprobarAserción(posiciones[cr_i][0],
                                       self.almc_zap.posicionar_zapato(
                                       zap, posiciones[cr_i][1]),
                                       n_t2, le, cr_i)
                cr_i += 1

            # Comprobación del tamaño del inventario
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(9, len(self.almc_zap), n_t, le)

            # Validación de la Homogeneidad del inventario de Zapatos
            le = (traceback.extract_stack()[-1])[1] + 2
            zap1x = Zapatin("mar_1x", "ref_1x", "usa", 700, 7)
            self.comprobarAserción(False,
                                   self.almc_zap.posicionar_zapato(zap1x, 0),
                                   n_t, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_4_desposicionar(self):
        iTest = 4
        sTitle = "Desposicionamiento de una referencia de zapato"
        fMax_nota = 0.6
        n_t = fMax_nota * 0.3 / 3
        if self.dict_pruebas.get("desposicionar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Desposicionar cuando no hay nada en el inventario
            le = (traceback.extract_stack()[-1])[1] + 2
            self.comprobarAserción(False,
                                   self.almc_zap.desposicionar_zapato(0),
                                   n_t, le)

            # Adición de Zapatos nacionales e importados al inventario
            lst_zaps = gen_lst_zapatos("")
            cr_i = 0
            for zap in lst_zaps:
                if cr_i < 4:
                    self.almc_zap.nacionales(zap)
                else:
                    self.almc_zap.importados(zap)
                cr_i += 1

            # Comprobación del tamaño del inventario
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(10, len(self.almc_zap), n_t, le)

            # Desposicionar cuando hay zapatos en el inventario
            cr_i = 0
            posiciones = [(True, 3), (False, 9), (True, 0), (True, 7),
                          (False, -1), (True, 6), (True, 2), (False, 7),
                          (True, 1), (False, -2)]
            n_t2 = fMax_nota * 0.7 / len(posiciones)
            le = (traceback.extract_stack()[-1])[1] + 3
            for pos_x in posiciones:
                self.comprobarAserción(pos_x[0],
                                       self.almc_zap.desposicionar_zapato(
                                       pos_x[1]), n_t2, le, cr_i)
                cr_i += 1

            # Comprobación del tamaño del inventario
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(4, len(self.almc_zap), n_t, le)
            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_5_vender_zapato(self):
        iTest = 5
        sTitle = "Venta de zapatos del inventario del almacén"
        fMax_nota = 1.0
        n_t = fMax_nota / 10
        if self.dict_pruebas.get("vender"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Adición de Zapatos nacionales e importados al inventario
            lst_zaps = gen_lst_zapatos("")
            cr_i = 0
            for zap in lst_zaps:
                if cr_i < 4:
                    self.almc_zap.nacionales(zap)
                else:
                    self.almc_zap.importados(zap)
                cr_i += 1

            # Comprobación del tamaño del inventario
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(10, len(self.almc_zap), n_t, le)

            # Vender zapatos del inventario actual del almacén
            z1 = Zapato("mar_1", "ref_1", "colombia")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(65000.0, self.almc_zap.vender_zapato(
                                   z1, 5), n_t, le)
            # quedan 3 pares zap1

            z11 = Zapato("mar_11", "ref_1", "usa")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(1001000.0, self.almc_zap.vender_zapato(
                                   z11, 7), n_t, le)
            # quedan 1 par zap11

            z7 = Zapato("mar_7", "ref_1", "colombia")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(-1.0, self.almc_zap.vender_zapato(
                                   z1, 7), n_t, le)
            # quedan 6 pares zap7, ninguno es vendido

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(546000.0, self.almc_zap.vender_zapato(
                                   z7, 6), n_t, le)
            # quedan 0 pares zap7 y por lo tanto se elimina [X]

            # Comprobación del tamaño del inventario
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(9, len(self.almc_zap), n_t, le)

            z6x = Zapato("mar_6", "ref_1", "china")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(-1.0, self.almc_zap.vender_zapato(
                                   z6x, 1), n_t, le)
            # zapato no existe en inventario

            z9x = Zapato("mar_9", "ref_1", "panamá")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(-1.0, self.almc_zap.vender_zapato(
                                   z9x, -1), n_t, le)
            # cantidad negativa

            z11 = Zapato("mar_11", "ref_1", "usa")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(143000.0, self.almc_zap.vender_zapato(
                                   z11, 1), n_t, le)
            # quedan 0 pares zap1 y por lo tanto se elimina [X]

            # Comprobación del tamaño del inventario
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(8, len(self.almc_zap), n_t, le)

            # VISUALIZACIÓN del Inventario actual del Almacén de Zapatos
            if VIEW_LIST:
                self.almc_zap.ver_inventario()
                input("[Enter] para continuar ...")

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_6_buscar_en_inventario(self):
        iTest = 6
        sTitle = "Comprobación de la búsqueda de un zapato en el inventario"
        fMax_nota = 0.6
        n_t = fMax_nota / 10
        if self.dict_pruebas.get("buscar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Adición de Zapatos nacionales e importados al inventario
            lst_zaps = gen_lst_zapatos("")
            cr_i = 0
            for zap in lst_zaps:
                if cr_i < 4:
                    self.almc_zap.nacionales(zap)
                else:
                    self.almc_zap.importados(zap)
                cr_i += 1

            # Comprobación del tamaño del inventario
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(10, len(self.almc_zap), n_t, le)

            # Buscar zapatos del inventario actual del almacén
            z2 = Zapato("mar_2", "ref_1", "usa")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("[Zapatos ACME] / mar_2:ref_1 -- " +
                                   "$20000 -- 5 pares",
                                   self.almc_zap.buscar_en_inventario(z2),
                                   n_t, le)

            z12 = Zapato("mar_12", "ref_1", "colombia")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("[Zapatos ACME] / mar_12:ref_1 -- " +
                                   "$120000 -- 7 pares",
                                   self.almc_zap.buscar_en_inventario(z12),
                                   n_t, le)

            z3x = Zapato("mar_3", "ref_1", "bolivia")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("", self.almc_zap.buscar_en_inventario(z3x),
                                   n_t, le)

            z5x = Zapato("mar_5x", "ref_1", "colombia")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("", self.almc_zap.buscar_en_inventario(z5x),
                                   n_t, le)

            z9x = Zapato("mar_9", "ref_1x", "panamá")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("", self.almc_zap.buscar_en_inventario(z9x),
                                   n_t, le)

            z8 = Zapato("mar_8", "ref_1", "méxico")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("[Zapatos ACME] / mar_8:ref_1 -- " +
                                   "$8000 -- 5 pares",
                                   self.almc_zap.buscar_en_inventario(z8),
                                   n_t, le)

            z4x = Zapato("mar_4", "ref_1", "chile")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("",
                                   self.almc_zap.buscar_en_inventario(z4x),
                                   n_t, le)

            z1 = Zapato("mar_1", "ref_1", "colombia")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("[Zapatos ACME] / mar_1:ref_1 -- " +
                                   "$10000 -- 8 pares",
                                   self.almc_zap.buscar_en_inventario(z1),
                                   n_t, le)

            # Comprobación del tamaño del inventario
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(10, len(self.almc_zap), n_t, le)
            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_nota(self):
        """
        INFORME DE LA NOTA FINAL
        """
        self.nota_final()

if __name__ == "__main__":
    unittest.main(verbosity=0)
