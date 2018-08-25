#!/usr/bin/env python3
from ei.arboles import ABinBus
from ei.recorridos import str_pre_orden
from ei.recorridos import str_post_orden
from ei.recorridos import str_in_orden
from ei.recorridos import pre_orden
from ei.recorridos import post_orden
from ei.recorridos import in_orden
from test_builder import TestBuilder
import unittest
import traceback
TIENE_STR_RECORRIDOS = True


def gen_lst_datos(bIngresar=False):
    """
    Función especial que permite la creación de los datos de tipo cadena
    utilizados en las diferentes pruebas.
    """
    lst_dat_ents = ['050', '025', '060', '090', '015', '055', '005', '070',
                    '080', '045', '035', '075', '030', '020', '085', '010',
                    '040', '100', '001', '065']
    return lst_dat_ents


class Testabb(TestBuilder):
    # Es posible desactivar cualquiera de las pruebas colocando el valor de
    # cero a cualquiera de ellas en el siguiente diccionario:
    dict_pruebas = {"recorrido_homogen": 1, "encontrar": 1,
                    "altura_nodos": 1, "remover_all": 1}

    def setUp(self):
        # Creación del abb con un variado grupo de cadenas
        self.abb = ABinBus()

    def test_0(self):
        self.presentación("Test ABinBus")

    def test_1_recorrido_homogen(self):
        iTest = 1
        sTitle = "Comprobación de recorrido y Homogeneidad"
        fMax_nota = 0.3
        Nt1_1 = fMax_nota * 0.4 / 3
        Nt1_2 = fMax_nota * 0.1
        Nt1_3 = fMax_nota * 0.5 / 2
        if self.dict_pruebas.get("recorrido_homogen"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Ingreso de 20 cadenas al abb
            lst_dat_ents = gen_lst_datos(True)
            for dat_ent in lst_dat_ents:
                self.abb.agregar(dat_ent)

            # Pruebas de Homogeneidad
            # Comprobación de la validación de objetos que no son cadenas
            # y son rechazados.
            lst_obj_malos = [100, 77.7, False]
            for obj in lst_obj_malos:
                try:
                    idx = lst_obj_malos.index(obj)
                    self.abb.agregar(obj)
                    print("NO DEBERIA MOSTRARSE ESTE MENSAJE", idx, "x objeto",
                          str(type(obj).__name__))
                except TypeError as e:
                    print(e)
                    le = (traceback.extract_stack()[-1])[1] + 1
                    self.comprobarAserción(True, True, Nt1_1, le, idx)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(20, len, [self.abb], Nt1_2, le)

            # Comprobación del recorrido.str_in_orden
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("[001][005][010][015][020][025][030][035]"
                                    "[040][045][050][055][060][065][070][075]"
                                    "[080][085][090][100]", str_in_orden,
                                    [self.abb], Nt1_3, le)

            # Comprobación del recorrido.str_post_orden
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("[001][010][005][020][015][030][040][035]"
                                    "[045][025][055][065][075][085][080][070]"
                                    "[100][090][060][050]", str_post_orden,
                                    [self.abb], Nt1_3, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_2_encontrar(self):
        iTest = 2
        sTitle = "Comprobación de Encontrar"
        fMax_nota = 0.3
        Nt2_1 = fMax_nota * 0.9 / 5
        Nt2_2 = fMax_nota * 0.1 / 24

        if self.dict_pruebas.get("encontrar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Comprobación de encontrar cuando el abb esta vacío
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(
                None, self.abb.encontrar, ["050"], Nt2_1, le)
            self.comprobarAserción2(
                None, self.abb.encontrar_min, [], Nt2_1, le + 2)
            self.comprobarAserción2(
                None, self.abb.encontrar_max, [], Nt2_1, le + 4)

            # Ingreso de 20 cadenas al abb
            lst_dat_ents = gen_lst_datos(True)
            for dat_ent in lst_dat_ents:
                self.abb.agregar(dat_ent)

            # Comprobación del método encontrar()
            le = (traceback.extract_stack()[-1])[1] + 3
            cr_i = 0
            for dat_ent in lst_dat_ents:
                self.comprobarAserción2(dat_ent, self.abb.encontrar, [dat_ent],
                                        Nt2_2, le, cr_i)
                cr_i += 1
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(
                None, self.abb.encontrar, ["007"], Nt2_2, le)
            self.comprobarAserción2(
                None, self.abb.encontrar, ["056"], Nt2_2, le + 2)
            self.comprobarAserción2(
                None, self.abb.encontrar, ["077"], Nt2_2, le + 4)
            self.comprobarAserción2(
                None, self.abb.encontrar, ["101"], Nt2_2, le + 6)

            # Comprobación del método encontrar_min()
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(
                "001", self.abb.encontrar_min, [], Nt2_1, le)

            # Comprobación del método encontrar_max()
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(
                "100", self.abb.encontrar_max, [], Nt2_1, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_3_altura_nodos(self):
        iTest = 3
        sTitle = "Comprobación de Altura y cantidad según el tipo de Nodo"
        fMax_nota = 0.4
        Nt3_1 = fMax_nota / 6
        if self.dict_pruebas.get("altura_nodos"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Comprobación de cantidades de nodos cuando el abb está vacío
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(0, self.abb.num_hojas, [], Nt3_1, le)
            self.comprobarAserción2(0, self.abb.num_nodos_internos, [], Nt3_1,
                                    le + 1)
            self.comprobarAserción2(0, self.abb.altura, [], Nt3_1, le + 3)

            # Ingreso de 20 cadenas al abb
            lst_dat_ents = gen_lst_datos(True)
            for dat_ent in lst_dat_ents:
                self.abb.agregar(dat_ent)

            # Comprobación de cantidades de nodos cuando el abb NO está vacío
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(10, self.abb.num_hojas, [], Nt3_1, le)
            self.comprobarAserción2(10, self.abb.num_nodos_internos, [], Nt3_1,
                                    le + 1)
            self.comprobarAserción2(6, self.abb.altura, [], Nt3_1, le + 3)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_4_remover_all(self):
        iTest = 4
        sTitle = "Comprobación de remover y algo más"
        fMax_nota = 1.0
        Nt4_1 = fMax_nota * 0.7 / 35
        Nt4_2 = fMax_nota * 0.2 / 21  # para str_recorridos
        Nt4_3 = fMax_nota * 0.1 / 7  # para len
        if self.dict_pruebas.get("remover_all"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Comprobación de remover de nodos cuando el abb está vacío
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(None, self.abb.remover, ["001"], 0.0, le)
            self.comprobarAserción2(None, self.abb.remover, [100], 0.0,
                                    le + 1)
            self.comprobarAserción2(None, self.abb.remover, [50.5], 0.0,
                                    le + 2)

            # Ingreso de 20 cadenas al abb
            lst_dat_ents = gen_lst_datos(True)
            for dat_ent in lst_dat_ents:
                self.abb.agregar(dat_ent)

            # Comprobación de remover cuando el abb NO está vacío
            # Nodos Hoja
            self.abb.remover("001")
            self.abb.remover("085")

            # Comprobación de los recorridos
            cad_pre = ("[050][025][015][005][010][020][045][035][030][040]"
                       "[060][055][090][070][065][080][075][100]")
            cad_pos = ("[010][005][020][015][030][040][035][045][025][055]"
                       "[065][075][080][070][100][090][060][050]")
            cad_in = ("[005][010][015][020][025][030][035][040][045][050]"
                      "[055][060][065][070][075][080][090][100]")
            if TIENE_STR_RECORRIDOS:
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_pre, str_pre_orden, [self.abb],
                                        Nt4_2, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_pos, str_post_orden, [self.abb],
                                        Nt4_2, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_in, str_in_orden, [self.abb],
                                        Nt4_2, le)
            else:
                print("ATENCIÓN: Recorridos no Implementados!")
                pre_orden(self.abb)
                print(cad_pre)
                rta = input("Presentación pre_orden Correcta # 1 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")
                post_orden(self.abb)
                print(cad_pos)
                rta = input("Presentación post_orden Correcta # 1 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")
                in_orden(self.abb)
                print(cad_in)
                rta = input("Presentación in_orden Correcta # 1 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")

            # Comprobación del tamaño del abb
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(18, len, [self.abb], Nt4_3, le)

            # Comprobación de cantidades de nodos y encontrar en abb NO vacío
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(8, self.abb.num_hojas, [], Nt4_1, le)
            self.comprobarAserción2(10, self.abb.num_nodos_internos, [],
                                    Nt4_1, le + 1)
            self.comprobarAserción2(6, self.abb.altura, [], Nt4_1, le + 3)
            self.comprobarAserción2("005", self.abb.encontrar_min, [], Nt4_1,
                                    le + 4)
            self.comprobarAserción2("100", self.abb.encontrar_max, [], Nt4_1,
                                    le + 6)

            # Comprobación de remover cuando el abb NO está vacío
            # Nodos Internos
            self.abb.remover("025", False)
            self.abb.remover("060")

            # Comprobación de los recorridos
            cad_pre = ("[050][020][015][005][010][045][035][030][040][065]"
                       "[055][090][070][080][075][100]")
            cad_pos = ("[010][005][015][030][040][035][045][020][055][075]"
                       "[080][070][100][090][065][050]")
            cad_in = ("[005][010][015][020][030][035][040][045][050][055]"
                      "[065][070][075][080][090][100]")
            if TIENE_STR_RECORRIDOS:
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_pre, str_pre_orden, [self.abb],
                                        Nt4_2, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_pos, str_post_orden, [self.abb],
                                        Nt4_2, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_in, str_in_orden, [self.abb],
                                        Nt4_2, le)
            else:
                print("ATENCIÓN: Recorridos no Implementados!")
                pre_orden(self.abb)
                print(cad_pre)
                rta = input("Presentación pre_orden Correcta # 2 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")
                post_orden(self.abb)
                print(cad_pos)
                rta = input("Presentación post_orden Correcta # 2 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")
                in_orden(self.abb)
                print(cad_in)
                rta = input("Presentación in_orden Correcta # 2 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")

            # Comprobación del tamaño del abb
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(16, len, [self.abb], Nt4_3, le)

            # Comprobación de cantidades de nodos y encontrar en abb NO vacío
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(6, self.abb.num_hojas, [], Nt4_1, le)
            self.comprobarAserción2(10, self.abb.num_nodos_internos, [],
                                    Nt4_1, le + 1)
            self.comprobarAserción2(6, self.abb.altura, [], Nt4_1, le + 3)
            self.comprobarAserción2("005", self.abb.encontrar_min, [],
                                    Nt4_1, le + 4)
            self.comprobarAserción2("100", self.abb.encontrar_max, [],
                                    Nt4_1, le + 6)

            # Comprobación de remover cuando el abb NO está vacío
            # Nodos Internos
            self.abb.remover("090")
            self.abb.remover("015", False)

            # Comprobación de los recorridos
            cad_pre = ("[050][020][005][010][045][035][030][040][065][055]"
                       "[100][070][080][075]")
            cad_pos = ("[010][005][030][040][035][045][020][055][075][080]"
                       "[070][100][065][050]")
            cad_in = ("[005][010][020][030][035][040][045][050][055][065][070]"
                      "[075][080][100]")
            if TIENE_STR_RECORRIDOS:
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_pre, str_pre_orden, [self.abb],
                                        Nt4_2, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_pos, str_post_orden, [self.abb],
                                        Nt4_2, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_in, str_in_orden, [self.abb],
                                        Nt4_2, le)
            else:
                print("ATENCIÓN: Recorridos no Implementados!")
                pre_orden(self.abb)
                print(cad_pre)
                rta = input("Presentación pre_orden Correcta # 3 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")
                post_orden(self.abb)
                print(cad_pos)
                rta = input("Presentación post_orden Correcta # 3 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")
                in_orden(self.abb)
                print(cad_in)
                rta = input("Presentación in_orden Correcta # 3 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")

            # Comprobación del tamaño del abb
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(14, len, [self.abb], Nt4_3, le)

            # Comprobación de cantidades de nodos y encontrar en abb NO vacío
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(5, self.abb.num_hojas, [], Nt4_1, le)
            self.comprobarAserción2(9, self.abb.num_nodos_internos, [], Nt4_1,
                                    le + 1)
            self.comprobarAserción2(6, self.abb.altura, [], Nt4_1, le + 3)
            self.comprobarAserción2("005", self.abb.encontrar_min, [], Nt4_1,
                                    le + 4)
            self.comprobarAserción2("100", self.abb.encontrar_max, [], Nt4_1,
                                    le + 6)

            # Comprobación de remover de min/max y root del abb
            self.abb.remover("005", False)
            self.abb.remover("100", False)
            self.abb.remover("050", False)

            # Comprobación de los recorridos
            cad_pre = "[045][020][010][035][030][040][065][055][070][080][075]"
            cad_pos = "[010][030][040][035][020][055][075][080][070][065][045]"
            cad_in = "[010][020][030][035][040][045][055][065][070][075][080]"
            if TIENE_STR_RECORRIDOS:
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_pre, str_pre_orden, [self.abb],
                                        Nt4_2, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_pos, str_post_orden, [self.abb],
                                        Nt4_2, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_in, str_in_orden, [self.abb],
                                        Nt4_2, le)
            else:
                print("ATENCIÓN: Recorridos no Implementados!")
                pre_orden(self.abb)
                print(cad_pre)
                rta = input("Presentación pre_orden Correcta # 4 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")
                post_orden(self.abb)
                print(cad_pos)
                rta = input("Presentación post_orden Correcta # 4 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")
                in_orden(self.abb)
                print(cad_in)
                rta = input("Presentación in_orden Correcta # 4 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")

            # Comprobación del tamaño del abb
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(11, len, [self.abb], Nt4_3, le)

            # Comprobación de cantidades de nodos y encontrar en abb NO vacío
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(5, self.abb.num_hojas, [], Nt4_1, le)
            self.comprobarAserción2(6, self.abb.num_nodos_internos, [], Nt4_1,
                                    le + 1)
            self.comprobarAserción2(5, self.abb.altura, [], Nt4_1, le + 3)
            self.comprobarAserción2("010", self.abb.encontrar_min, [], Nt4_1,
                                    le + 4)
            self.comprobarAserción2("080", self.abb.encontrar_max, [], Nt4_1,
                                    le + 6)

            # Comprobación de remover de hojas del abb
            self.abb.remover("075")
            self.abb.remover("040", False)
            self.abb.remover("030")
            self.abb.remover("010", False)

            # Comprobación de los recorridos
            cad_pre = "[045][020][035][065][055][070][080]"
            cad_pos = "[035][020][055][080][070][065][045]"
            cad_in = "[020][035][045][055][065][070][080]"
            if TIENE_STR_RECORRIDOS:
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_pre, str_pre_orden, [self.abb],
                                        Nt4_2, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_pos, str_post_orden, [self.abb],
                                        Nt4_2, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_in, str_in_orden, [self.abb],
                                        Nt4_2, le)
            else:
                print("ATENCIÓN: Recorridos no Implementados!")
                pre_orden(self.abb)
                print(cad_pre)
                rta = input("Presentación pre_orden Correcta # 5 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")
                post_orden(self.abb)
                print(cad_pos)
                rta = input("Presentación post_orden Correcta # 5 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")
                in_orden(self.abb)
                print(cad_in)
                rta = input("Presentación in_orden Correcta # 5 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")

            # Comprobación del tamaño del abb
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(7, len, [self.abb], Nt4_3, le)

            # Comprobación de cantidades de nodos y encontrar en abb NO vacío
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(3, self.abb.num_hojas, [], Nt4_1, le)
            self.comprobarAserción2(4, self.abb.num_nodos_internos, [], Nt4_1,
                                    le + 1)
            self.comprobarAserción2(4, self.abb.altura, [], Nt4_1, le + 3)
            self.comprobarAserción2("020", self.abb.encontrar_min, [], Nt4_1,
                                    le + 4)
            self.comprobarAserción2("080", self.abb.encontrar_max, [], Nt4_1,
                                    le + 6)

            # Comprobación de remover hasta llegar al root del abb
            self.abb.remover("020", False)
            self.abb.remover("080", False)
            self.abb.remover("065")
            self.abb.remover("055", False)
            self.abb.remover("070", False)
            self.abb.remover("035", False)

            # Comprobación de los recorridos
            cad_pre = "[045]"
            cad_pos = "[045]"
            cad_in = "[045]"
            if TIENE_STR_RECORRIDOS:
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_pre, str_pre_orden, [self.abb],
                                        Nt4_2, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_pos, str_post_orden, [self.abb],
                                        Nt4_2, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_in, str_in_orden, [self.abb],
                                        Nt4_2, le)
            else:
                print("ATENCIÓN: Recorridos no Implementados!")
                pre_orden(self.abb)
                print(cad_pre)
                rta = input("Presentación pre_orden Correcta # 6 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")
                post_orden(self.abb)
                print(cad_pos)
                rta = input("Presentación post_orden Correcta # 6 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")
                in_orden(self.abb)
                print(cad_in)
                rta = input("Presentación in_orden Correcta # 6 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")

            # Comprobación del tamaño del abb
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(1, len, [self.abb], Nt4_3, le)

            # Comprobación de cantidades de nodos y encontrar en abb NO vacío
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(1, self.abb.num_hojas, [], Nt4_1, le)
            self.comprobarAserción2(0, self.abb.num_nodos_internos, [], Nt4_1,
                                    le + 1)
            self.comprobarAserción2(1, self.abb.altura, [], Nt4_1, le + 3)
            self.comprobarAserción2("045", self.abb.encontrar_min, [], Nt4_1,
                                    le + 4)
            self.comprobarAserción2("045", self.abb.encontrar_max, [], Nt4_1,
                                    le + 6)

            # Comprobación de remover de root y abb vacío
            self.abb.remover("045")

            # Comprobación de los recorridos
            cad_pre = ""
            cad_pos = ""
            cad_in = ""
            if TIENE_STR_RECORRIDOS:
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_pre, str_pre_orden, [self.abb],
                                        Nt4_2, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_pos, str_post_orden, [self.abb],
                                        Nt4_2, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(cad_in, str_in_orden, [self.abb],
                                        Nt4_2, le)
            else:
                print("ATENCIÓN: Recorridos no Implementados!")
                pre_orden(self.abb)
                print(cad_pre)
                rta = input("Presentación pre_orden Correcta # 7 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")
                post_orden(self.abb)
                print(cad_pos)
                rta = input("Presentación post_orden Correcta # 7 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")
                in_orden(self.abb)
                print(cad_in)
                rta = input("Presentación in_orden Correcta # 7 ([S]/n)?")
                if rta in ["S", "s", ""]:
                    self.comprobarAserción(True, True, Nt4_2 / 5, 0)
                    print("OK")

            # Comprobación del tamaño del abb
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(0, len, [self.abb], Nt4_3, le)

            # Comprobación de cantidades de nodos y encontrar en abb NO vacío
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(0, self.abb.num_hojas, [], Nt4_1, le)
            self.comprobarAserción2(0, self.abb.num_nodos_internos, [], Nt4_1,
                                    le + 1)
            self.comprobarAserción2(0, self.abb.altura, [], Nt4_1, le + 3)
            self.comprobarAserción2(None, self.abb.encontrar_min, [], Nt4_1,
                                    le + 4)
            self.comprobarAserción2(None, self.abb.encontrar_max, [], Nt4_1,
                                    le + 6)
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
