#!/usr/bin/env python3
from test_builder import TestBuilder
from agenda import Agenda
from agenda import __author_1__
from agenda import __author_2__
import unittest
import traceback


def gen_lst_contactos(bIngresar=False):
    """
    Función especial que permite la creación de los datos de los contactos
    utilizados en las diferentes pruebas, devolviendo una lista de tuplas con
    la lista del dato del contacto y un valor booleano que representa si los
    datos serán o no aceptados en la Agenda.
    """
    # ['Nombre', 'Teléfono', 'Operador', minutos]
    dat_cont00 = ['Pablo', '397', 'Claro', 18]
    dat_cont01 = ['Mario', '333', 'Movistar', 20]
    dat_cont02 = ['Benito', '350', 'Virgin', 14]
    dat_cont03 = ['David', '379', 'Tigo', -6]
    dat_cont04 = ['Patricia', '328', 'Movistar', 15]
    dat_cont05e = ['Benito', '350', 'Movistar', 3]
    dat_cont05 = ['Benito', '386', 'Claro', 29]
    dat_cont06 = ['Tulio', '364', 'Claro', 13]
    dat_cont07 = ['Zoila', '302', 'Movistar', 0]
    dat_cont07e = ['Pablo', '397', 'Tigo', 4]
    dat_cont08 = ['Rosa', '341', 'Tigo', 37]
    dat_cont09 = ['Carolina', '315', 'Claro', -51]

    if bIngresar:
        # Lista utilizada únicamente en test_1_agregar()
        lst_dat_conts = [(dat_cont00, True), (dat_cont01, True),
                         (dat_cont02, True), (dat_cont03, True),
                         (dat_cont04, True), (dat_cont05e, False),
                         (dat_cont05, True), (dat_cont06, True),
                         (dat_cont07, True), (dat_cont07e, False),
                         (dat_cont08, True), (dat_cont09, True)]
    else:
        lst_dat_conts = [dat_cont00, dat_cont01, dat_cont02, dat_cont03,
                         dat_cont04, dat_cont05, dat_cont06, dat_cont07,
                         dat_cont08, dat_cont09]
    return lst_dat_conts


class TestAgendaTelefónica(TestBuilder):
    # Es posible desactivar cualquiera de las pruebas colocando el valor de
    # cero a cualquiera de ellas en el siguiente diccionario:
    dict_pruebas = {"agregar": 1, "borrar": 1, "llamar": 1, "consumo": 1}

    def setUp(self):
        # Creación de la Agenda con un variado grupo de contactos
        self.registro = Agenda()

    def test_0(self):
        self.presentación("Test Agenda")

    def test_1_agregar(self):
        iTest = 1
        sTitle = "Comprobación de Agregación de nuevos Contactos a la Agenda"
        fMax_nota = 0.5
        Nt1_1 = fMax_nota * 0.6 / 12    # Agregar
        Nt1_2 = fMax_nota * 0.2         # Tamaño
        Nt1_3 = fMax_nota * 0.2 / 2        # Informe de la Agenda
        if self.dict_pruebas.get("agregar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Comprobación del ingreso de 10 contactos a la Agenda
            lst_dat_conts = gen_lst_contactos(True)
            cr_i = 0
            le = (traceback.extract_stack()[-1])[1] + 2
            for dat_cont in lst_dat_conts:
                # Se agregan los contactos generados con el siguiente
                # formato:
                # "Nombre", "Teléfono", "Operador", minutos
                self.comprobarAserción(dat_cont[1], (
                    self.registro.agregarContacto(dat_cont[0][0],
                                                  dat_cont[0][1],
                                                  dat_cont[0][2],
                                                  dat_cont[0][3])),
                                       Nt1_1, le, cr_i)
                cr_i += 1

            # Comprobación del tamaño de la Agenda
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(10, len(self.registro), Nt1_2, le)

            # Cadena de registros de la Agenda
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("[<Pablo> #397(Claro):18]"
                                   "[<Mario> #333(Movistar):20]"
                                   "[<Benito> #350(Virgin):14]"
                                   "[<David> #379(Tigo):0]"
                                   "[<Benito> #386(Claro):29]"
                                   "[<Carolina> #315(Claro):0]"
                                   "[<Patricia> #328(Movistar):15]"
                                   "[<Tulio> #364(Claro):13]"
                                   "[<Rosa> #341(Tigo):37]"
                                   "[<Zoila> #302(Movistar):0]",
                                   self.registro.infoHistorico(), Nt1_3, le)

            # Cadena de registros de la Agenda con presentación Incorrecta
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("", self.registro.infoHistorico(4),
                                   Nt1_3, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_2_borrar(self):
        iTest = 2
        sTitle = "Comprobación del Borrado de un Contacto en la Agenda"
        fMax_nota = 1.0
        Nt2_1 = fMax_nota * 0.6 / 8    # Borrar Contacto
        Nt2_2 = fMax_nota * 0.2 / 4    # Tamaño
        Nt2_3 = fMax_nota * 0.2 / 4      # Informe de la Agenda
        if self.dict_pruebas.get("borrar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Comprobación del borrado de contactos en Agenda vacía
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(False, self.registro.borrarContacto("Ana",
                                                                       "378"),
                                   Nt2_1, le)

            # Ingreso de 10 contactos a la Agenda
            lst_dat_conts = gen_lst_contactos()
            for dat_cont in lst_dat_conts:
                # Se agregan los contactos generados con el siguiente
                # formato:
                # "Teléfono", "Teléfono", "Operador"
                self.registro.agregarContacto(dat_cont[0], dat_cont[1],
                                              dat_cont[2])

            # Comprobación del borrado sobre Agenda con contactos
            # Contacto: "Carolina", "315"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(True,
                                   self.registro.borrarContacto("Carolina",
                                                                "315"),
                                   Nt2_1, le)

            # Comprobación del borrado sobre Agenda con contactos
            # Contacto: "Patricia", "328"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(True,
                                   self.registro.borrarContacto("Patricia",
                                                                "328",
                                                                False),
                                   Nt2_1, le)

            # Comprobación del borrado sobre Agenda con contactos
            # Contacto: "Pablo", "123" NO EXISTE
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(False,
                                   self.registro.borrarContacto("Pablo",
                                                                "123"),
                                   Nt2_1, le)

            # Comprobación del tamaño de la Agenda
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(8, len(self.registro), Nt2_2, le)

            # Cadena de registros de la Agenda
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("[<Benito> #386(Claro):0]"
                                   "[<David> #379(Tigo):0]"
                                   "[<Benito> #350(Virgin):0]"
                                   "[<Mario> #333(Movistar):0]"
                                   "[<Rosa> #341(Tigo):0]"
                                   "[<Zoila> #302(Movistar):0]"
                                   "[<Tulio> #364(Claro):0]"
                                   "[<Pablo> #397(Claro):0]",
                                   self.registro.infoHistorico(2), Nt2_3, le)

            # Se agregan los contactos generados con el siguiente
            # formato:
            # "Nombre", "Teléfono", "Operador"
            self.registro.agregarContacto("Nelly", "311", "Tigo")
            self.registro.agregarContacto("Marco", "322", "Movistar")
            self.registro.agregarContacto("Melina", "333", "Claro")

            # Comprobación del borrado sobre Agenda con contactos
            # Contacto: "Pablo", "397"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(True,
                                   self.registro.borrarContacto("Pablo",
                                                                "397"),
                                   Nt2_1, le)

            # Comprobación del tamaño de la Agenda
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(10, len(self.registro), Nt2_2, le)

            # Cadena de registros de la Agenda
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("[<Nelly> #311(Tigo):0]"
                                   "[<Mario> #333(Movistar):0]"
                                   "[<Benito> #350(Virgin):0]"
                                   "[<David> #379(Tigo):0]"
                                   "[<Benito> #386(Claro):0]"
                                   "[<Marco> #322(Movistar):0]"
                                   "[<Melina> #333(Claro):0]"
                                   "[<Tulio> #364(Claro):0]"
                                   "[<Rosa> #341(Tigo):0]"
                                   "[<Zoila> #302(Movistar):0]",
                                   self.registro.infoHistorico(), Nt2_3, le)

            # Se agregan los contactos generados con el siguiente
            # formato:
            # "Nombre", "Teléfono", "Operador"
            self.registro.agregarContacto("Orlando", "301", "Movistar")
            self.registro.agregarContacto("Pedro", "320", "Tigo")
            self.registro.agregarContacto("Quino", "303", "Claro")
            self.registro.agregarContacto("Paola", "340", "Claro")

            # Comprobación del borrado sobre Agenda con contactos
            # Contacto: "Nelly", "311"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(True,
                                   self.registro.borrarContacto("Nelly",
                                                                "311",
                                                                False),
                                   Nt2_1, le)

            # Comprobación del tamaño de la Agenda
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(13, len(self.registro), Nt2_2, le)

            # Cadena de registros de la Agenda
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("[<Benito> #350(Virgin):0]"
                                   "[<Benito> #386(Claro):0]"
                                   "[<David> #379(Tigo):0]"
                                   "[<Marco> #322(Movistar):0]"
                                   "[<Mario> #333(Movistar):0]"
                                   "[<Melina> #333(Claro):0]"
                                   "[<Orlando> #301(Movistar):0]"
                                   "[<Paola> #340(Claro):0]"
                                   "[<Pedro> #320(Tigo):0]"
                                   "[<Quino> #303(Claro):0]"
                                   "[<Rosa> #341(Tigo):0]"
                                   "[<Tulio> #364(Claro):0]"
                                   "[<Zoila> #302(Movistar):0]",
                                   self.registro.infoHistorico(3), Nt2_3, le)

            # Comprobación del borrado sobre Agenda con contactos
            # Contacto: "Mario", "333"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(True, self.registro.borrarContacto("Mario",
                                                                      "333"),
                                   Nt2_1, le)

            # Comprobación del borrado sobre Agenda con contactos
            # Contacto: "Falcao", "309" NO EXISTE
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(False,
                                   self.registro.borrarContacto("Falcao",
                                                                "309"),
                                   Nt2_1, le)

            # Comprobación del tamaño de la Agenda
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(12, len(self.registro), Nt2_2, le)

            # Cadena de registros de la Agenda
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("[<Orlando> #301(Movistar):0]"
                                   "[<Marco> #322(Movistar):0]"
                                   "[<Benito> #350(Virgin):0]"
                                   "[<David> #379(Tigo):0]"
                                   "[<Benito> #386(Claro):0]"
                                   "[<Melina> #333(Claro):0]"
                                   "[<Tulio> #364(Claro):0]"
                                   "[<Rosa> #341(Tigo):0]"
                                   "[<Pedro> #320(Tigo):0]"
                                   "[<Paola> #340(Claro):0]"
                                   "[<Quino> #303(Claro):0]"
                                   "[<Zoila> #302(Movistar):0]",
                                   self.registro.infoHistorico(1), Nt2_3, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_3_llamar(self):
        iTest = 3
        sTitle = "Comprobación de Llamadas realizadas a diferentes Contactos"
        fMax_nota = 0.5
        Nt3_1 = fMax_nota * 0.8 / 10    # Llamar Contacto
        Nt3_2 = fMax_nota * 0.1         # Tamaño
        Nt3_3 = fMax_nota * 0.1         # Informe de la Agenda

        if self.dict_pruebas.get("llamar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Comprobación de Llamadas cuando la Agenda esta vacía
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(-1,
                                   self.registro.llamarContacto("Juanito",
                                                                "159", 100),
                                   Nt3_1, le)

            # Ingreso de 10 contactos a la Agenda
            lst_dat_conts = gen_lst_contactos()
            for dat_cont in lst_dat_conts:
                # Se agregan los contactos generados con el siguiente
                # formato:
                # "Nombre", "Teléfono", "Operador", minutos
                self.registro.agregarContacto(dat_cont[0], dat_cont[1],
                                              dat_cont[2], dat_cont[3])

            # Comprobación de Llamadas en Agenda que tiene Contactos
            # + 10 minutos / Contacto: "Rosa", "341"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(47, self.registro.llamarContacto("Rosa",
                                                                    "341", 10),
                                   Nt3_1, le)

            # Comprobación de Llamadas en Agenda que tiene Contactos
            # + 18 minutos, + 25 minutos / Contacto: "David", "379"
            self.registro.llamarContacto("David", "379", 18)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(43, self.registro.llamarContacto("David",
                                                                    "379",
                                                                    25),
                                   Nt3_1, le)

            # Comprobación de Llamadas en Agenda que tiene Contactos
            # + 36 minutos, -70 minutos, + 24 minutos /
            # Contacto: "Benito", "386"
            self.registro.llamarContacto("Benito", "386", 36)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(-1,
                                   self.registro.llamarContacto("Benito",
                                                                "386", -70),
                                   Nt3_1, le)
            self.comprobarAserción(89, self.registro.llamarContacto("Benito",
                                                                    "386", 24),
                                   Nt3_1, le + 4)

            # Comprobación de Llamadas en Agenda que tiene Contactos
            # - 8 minutos, + 17 minutos, +0 minutos, + 6 minutos /
            # Contacto: "Pablo", "397"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(-1, self.registro.llamarContacto("Pablo",
                                                                    "397", -8),
                                   Nt3_1, le)
            self.registro.llamarContacto("Pablo", "397", 17)
            self.comprobarAserción(35, self.registro.llamarContacto("Pablo",
                                                                    "397", 0),
                                   Nt3_1, le + 4)
            self.comprobarAserción(41, self.registro.llamarContacto("Pablo",
                                                                    "397", 6),
                                   Nt3_1, le + 7)

            # Comprobación de Llamadas en Agenda que tiene Contactos
            # + 77 minutos / Contacto: "Zoila", "302"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(77, self.registro.llamarContacto("Zoila",
                                                                    "302", 77),
                                   Nt3_1, le)

            # Comprobación de Llamadas en Agenda que tiene Contactos
            # + 100 minutos / Contacto: "Jame", "310"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(-1, self.registro.llamarContacto("James",
                                                                    "310",
                                                                    100),
                                   Nt3_1, le)

            # Comprobación del tamaño de la Agenda
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(10, len(self.registro), Nt3_2, le)

            # Cadena de registros de la Agenda
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("[<Carolina> #315(Claro):0]"
                                   "[<Benito> #386(Claro):89]"
                                   "[<David> #379(Tigo):43]"
                                   "[<Benito> #350(Virgin):14]"
                                   "[<Mario> #333(Movistar):20]"
                                   "[<Rosa> #341(Tigo):47]"
                                   "[<Zoila> #302(Movistar):77]"
                                   "[<Tulio> #364(Claro):13]"
                                   "[<Patricia> #328(Movistar):15]"
                                   "[<Pablo> #397(Claro):41]",
                                   self.registro.infoHistorico(2), Nt3_3, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_4_consumo(self):
        iTest = 4
        sTitle = "Comprobación de los minutos de consumo por cada Operador"
        fMax_nota = 1.0
        Nt4_1 = fMax_nota / 9   # Consumo
        if self.dict_pruebas.get("consumo"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Comprobación del consumo de minutos de un Operador cuando la
            # Agenda está vacía
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(0, self.registro.consumoOperador("Tigo"),
                                   Nt4_1, le)
            self.comprobarAserción(0, self.registro.consumoOperador("Claro"),
                                   Nt4_1, le + 2)
            self.comprobarAserción(0,
                                   self.registro.consumoOperador("Movistar"),
                                   Nt4_1, le + 4)
            self.comprobarAserción(0, self.registro.consumoOperador("Virgin"),
                                   Nt4_1, le + 7)

            # Ingreso de 10 contactos a la Agenda
            lst_dat_conts = gen_lst_contactos()
            for dat_cont in lst_dat_conts:
                # "Nombre", "Teléfono", "Operador", minutos
                self.registro.agregarContacto(dat_cont[0], dat_cont[1],
                                              dat_cont[2], dat_cont[3])

            # Comprobación del consumo de minutos por Operador
            # Operador: Claro
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(60, self.registro.consumoOperador("Claro"),
                                   Nt4_1, le)

            # Comprobación del consumo de minutos por Operador
            # Operador: Virgin
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(14, self.registro.consumoOperador("Virgin"),
                                   Nt4_1, le)

            # Comprobación del consumo de minutos por Operador
            # Operador: Migo NO EXISTE!
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(0, self.registro.consumoOperador("Migo"),
                                   Nt4_1, le)

            # Comprobación del consumo de minutos por Operador
            # Operador: Tigo
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(37, self.registro.consumoOperador("Tigo"),
                                   Nt4_1, le)

            # Comprobación del consumo de minutos por Operador
            # Operador: Movistar
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(35,
                                   self.registro.consumoOperador("Movistar"),
                                   Nt4_1, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_nota(self):
        """
        INFORME DE LA NOTA FINAL
        """
        self.nota_final(__author_1__, __author_2__)


if __name__ == "__main__":
    unittest.main(verbosity=0)
