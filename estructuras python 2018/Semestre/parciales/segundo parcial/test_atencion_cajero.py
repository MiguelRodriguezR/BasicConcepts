#!/usr/bin/env python3
from test_builder import TestBuilder
from atencion_cajero import Cajero, Cliente
import unittest
import traceback
VIEW_LIST = False


def gen_lst_cli(t_n=0):
    """
    Función especial que permite la creación de los clientes utilizados en las
    diferentes pruebas, devolviendo una lista de tuplas con el cliente y un
    valor booleano que representa si el cliente será o no aceptado en la cola
    de Atención del Cajero.
    """
    cli1 = Cliente(1, 'C', 20000)
    cli2 = Cliente(2, 'R', 15000)
    if t_n == 1:
        cli3 = Cliente(3, 'C', -6000)
    else:
        cli3 = Cliente(3, 'C', 6000)
    cli4 = Cliente(4, 'R', 17500)
    # True: Es un robo
    if t_n == 2:
        cli5 = Cliente(5)
    else:
        cli5 = Cliente(5, 'R', 10000)
    cli6 = Cliente(6, 'R', 5000)
    if t_n == 1:
        cli7 = Cliente(7, 'C', -8000)
    else:
        cli7 = Cliente(7, 'C', 8000)
    # True: Es un robo
    if t_n == 2:
        cli8 = Cliente(8, 'J', 40000)
    else:
        cli8 = Cliente(8, 'R', 9000)
    cli9 = Cliente(9, 'C', 12977)
    cli10 = Cliente(10, 'C', 10300)

    lst_cli = [(cli1, True), (cli2, True), (cli3, False), (cli4, True),
               (cli5, True), (cli6, True), (cli7, False), (cli8, True),
               (cli9, True), (cli10, True)]
    return lst_cli


class Usuario:
    def __init__(self, num_oper, operación, monto):
        self.num_oper = num_oper
        self.operación = operación
        self.monto = monto


class TestAtenciónCajero(TestBuilder):
    # Es posible desactivar cualquiera de las pruebas colocando el valor de
    # cero a cualquiera de ellas en el siguiente diccionario:
    dict_pruebas = {"a_la_cola": 1, "atención": 1, "seguridad": 1}

    def setUp(self):
        # Creación del Cajero con un recaudo inicial de $0 y su cola de
        # atención vacía.
        self.cajero = Cajero()

    def test_0(self):
        self.presentación("Test Atención de Cajero")

    def test_1_a_la_cola(self):
        iTest = 1
        sTitle = "Comprobación de Recepción de Clientes en la cola del Cajero"
        fMax_nota = 0.6
        Nt1_2 = fMax_nota * 0.15 / 3  # Homogeneidad
        Nt1_3 = fMax_nota * 0.05      # Tamaño de la CC
        Nt1_4 = fMax_nota * 0.10      # Escaneo por operación de la CC
        Nt1_5 = fMax_nota * 0.10      # Informe de la CC
        if self.dict_pruebas.get("a_la_cola"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICCO DE PRUEBAS ###########################
            """
            # Comprobación de recepción de Clientes en la cola del Cajero
            lst_cli = gen_lst_cli(1)
            Nt1_1 = fMax_nota * 0.60 / (len(lst_cli) + 2)  # A la cola
            # Ciente que va a Robar
            cli0 = Cliente(0)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.cajero.a_la_cola, [cli0],
                                    Nt1_1, le)
            cr_i = 0
            le = (traceback.extract_stack()[-1])[1] + 2
            for cli in lst_cli:
                self.comprobarAserción2(cli[1], self.cajero.a_la_cola,
                                        [cli[0]], Nt1_1, le, cr_i)
                cr_i += 1

            # Validación de la Homogeneidad del Cajero
            le = (traceback.extract_stack()[-1])[1] + 2
            usu1x = Usuario(1, 'C', 20000)
            self.comprobarAserción2(False, self.cajero.a_la_cola, [usu1x],
                                    Nt1_2, le)
            le = (traceback.extract_stack()[-1])[1] + 2
            usu2x = Usuario(8, 'R', 9000)
            self.comprobarAserción2(False, self.cajero.a_la_cola, [usu2x],
                                    Nt1_2, le)

            le = (traceback.extract_stack()[-1])[1] + 2
            usu3x = Usuario(5, 'X', 0)
            self.comprobarAserción2(False, self.cajero.a_la_cola, [usu3x],
                                    Nt1_2, le)
            # Ciente que va a Robar
            cli11 = Cliente(11, 'H', 1)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.cajero.a_la_cola, [cli11],
                                    Nt1_1, le)

            # Comprobación del tamaño de la CC
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(10, len(self.cajero), Nt1_3, le)

            # Escaneo del tamaño de la cola discriminado por tipo de Operación
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción((3, 5, 2), self.cajero.escaneo(), Nt1_4, le)

            # Informe de los clientes actuales en la Cola del Cajero, separados
            # por tipo de Operación y mostrados en orden inverso a como serán
            # atendidos
            strInfoCC = """N-O <10>
Consignación $10300
+++++++++++++++++++++++++++++
N-O <9>
Consignación $12977
+++++++++++++++++++++++++++++
N-O <1>
Consignación $20000
.............................
N-O <8>
Retiro $9000
-----------------------------
N-O <6>
Retiro $5000
-----------------------------
N-O <5>
Retiro $10000
-----------------------------
N-O <4>
Retiro $17500
-----------------------------
N-O <2>
Retiro $15000
.............................
N-O <11>
Robo $0
xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
N-O <0>
Robo $0"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(strInfoCC, self.cajero.info(), Nt1_5, le)
            """
            ################ PRESENTACCÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_2_atención(self):
        iTest = 2
        sTitle = "Comprobación de la Atención de la Cola del Cajero"
        fMax_nota = 1.2
        Nt2_1 = fMax_nota * 0.70 / 14    # Atención
        Nt2_2 = fMax_nota * 0.10 / 4     # Tamaño de la CC
        Nt2_3 = fMax_nota * 0.10 / 4     # Escaneo por operación de la CC
        Nt2_4 = fMax_nota * 0.10 / 4     # Informe de la CC
        if self.dict_pruebas.get("atención"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICCO DE PRUEBAS ###########################
            """
            # Comprobación de la atención cuando la CC está Vacía
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("COLA DE CLIENTES VACIA\n"
                                   "RECAUDO CAJERO $0",
                                   self.cajero.atención(), Nt2_1, le)

            # Comprobación del tamaño de la CC
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(0, len(self.cajero), Nt2_2, le)

            # Escaneo del tamaño de la cola discriminado por tipo de Operación
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción((0, 0, 0), self.cajero.escaneo(), Nt2_3, le)

            # Informe de los clientes actuales en la Cola del Cajero, separados
            # por tipo de Operación y mostrados en orden inverso a como serán
            # atendidos
            strInfoCC = ""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(strInfoCC, self.cajero.info(), Nt2_4, le)

            # Adición de clientes a la CC
            lst_cli = gen_lst_cli()
            for cli in lst_cli:
                self.cajero.a_la_cola(cli[0])

            # Comprobación de la atención cuando la CC contiene clientes
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <1>\n"
                                   "Consignación $20000\n"
                                   "RECAUDO CAJERO $20000",
                                   self.cajero.atención(), Nt2_1, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <2>\n"
                                   "Retiro $15000\n"
                                   "RECAUDO CAJERO $5000",
                                   self.cajero.atención(), Nt2_1, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <3>\n"
                                   "Consignación $6000\n"
                                   "RECAUDO CAJERO $11000",
                                   self.cajero.atención(), Nt2_1, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <4>\n"
                                   "Retiro $17500\n"
                                   "RECAUDO CAJERO $11000",
                                   self.cajero.atención(), Nt2_1, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <5>\n"
                                   "Retiro $10000\n"
                                   "RECAUDO CAJERO $1000",
                                   self.cajero.atención(), Nt2_1, le)

            # Comprobación del tamaño de la CC
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(6, len(self.cajero), Nt2_2, le)

            # Escaneo del tamaño de la cola discriminado por tipo de Operación
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción((3, 3, 0), self.cajero.escaneo(), Nt2_3, le)

            # Informe de los clientes actuales en la Cola del Cajero, separados
            # por tipo de Operación y mostrados en orden inverso a como serán
            # atendidos
            strInfoCC = """N-O <10>
Consignación $10300
+++++++++++++++++++++++++++++
N-O <9>
Consignación $12977
+++++++++++++++++++++++++++++
N-O <7>
Consignación $8000
.............................
N-O <4>
Retiro $17500
-----------------------------
N-O <8>
Retiro $9000
-----------------------------
N-O <6>
Retiro $5000"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(strInfoCC, self.cajero.info(), Nt2_4, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <6>\n"
                                   "Retiro $5000\n"
                                   "RECAUDO CAJERO $1000",
                                   self.cajero.atención(), Nt2_1, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <7>\n"
                                   "Consignación $8000\n"
                                   "RECAUDO CAJERO $9000",
                                   self.cajero.atención(), Nt2_1, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <8>\n"
                                   "Retiro $9000\n"
                                   "RECAUDO CAJERO $0",
                                   self.cajero.atención(), Nt2_1, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <9>\n"
                                   "Consignación $12977\n"
                                   "RECAUDO CAJERO $12977",
                                   self.cajero.atención(), Nt2_1, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <10>\n"
                                   "Consignación $10300\n"
                                   "RECAUDO CAJERO $23277",
                                   self.cajero.atención(), Nt2_1, le)

            # Comprobación del tamaño de la CC
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(2, len(self.cajero), Nt2_2, le)

            # Escaneo del tamaño de la cola discriminado por tipo de Operación
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción((0, 2, 0), self.cajero.escaneo(), Nt2_3, le)

            # Informe de los clientes actuales en la Cola del Cajero, separados
            # por tipo de Operación y mostrados en orden inverso a como serán
            # atendidos
            strInfoCC = """N-O <6>
Retiro $5000
-----------------------------
N-O <4>
Retiro $17500"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(strInfoCC, self.cajero.info(), Nt2_4, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <4>\n"
                                   "Retiro $17500\n"
                                   "RECAUDO CAJERO $5777",
                                   self.cajero.atención(), Nt2_1, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <6>\n"
                                   "Retiro $5000\n"
                                   "RECAUDO CAJERO $777",
                                   self.cajero.atención(), Nt2_1, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("COLA DE CLIENTES VACIA\n"
                                   "RECAUDO CAJERO $777",
                                   self.cajero.atención(), Nt2_1, le)

            # Comprobación del tamaño de la CC
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(0, len(self.cajero), Nt2_2, le)

            # Escaneo del tamaño de la cola discriminado por tipo de Operación
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción((0, 0, 0), self.cajero.escaneo(), Nt2_3, le)

            # Informe de los clientes actuales en la Cola del Cajero, separados
            # por tipo de Operación y mostrados en orden inverso a como serán
            # atendidos
            strInfoCC = ""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(strInfoCC, self.cajero.info(), Nt2_4, le)
            """
            ################ PRESENTACCÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_3_seguridad(self):
        iTest = 3
        sTitle = "Comprobación de la efectividad de la Seguridad del Cajero"
        fMax_nota = 1.2
        Nt3_1 = fMax_nota * 0.60 / 4     # Seguridad
        Nt3_2 = fMax_nota * 0.15 / 6     # Atención
        Nt3_3 = fMax_nota * 0.05 / 4     # Tamaño de la CC
        Nt3_4 = fMax_nota * 0.10 / 2     # Escaneo por operación de la CC
        Nt3_5 = fMax_nota * 0.10 / 2     # Informe de la CC

        if self.dict_pruebas.get("seguridad"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICCO DE PRUEBAS ###########################
            """
            # Comprobación de la atención cuando la CC está Vacía
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(False, self.cajero.seguridad(), Nt3_1, le)

            # Adición de clientes a la CC
            lst_cli = gen_lst_cli(2)
            for cli in lst_cli:
                self.cajero.a_la_cola(cli[0])

            # Atención de 5 clientes [1:Sí, 2:Sí, 3:Sí, 4:No, 5:Robo] de la CC
            self.cajero.atención()  # 1
            self.cajero.atención()  # 2
            self.cajero.atención()  # 3
            self.cajero.atención()  # 4
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <5>\n"
                                   "Robo $11000\n"
                                   "RECAUDO CAJERO $0",
                                   self.cajero.atención(), Nt3_2, le)

            # Comprobación del tamaño de la CC
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(6, len(self.cajero), Nt3_3, le)

            # Escaneo del tamaño de la cola discriminado por tipo de Operación
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción((3, 2, 1), self.cajero.escaneo(), Nt3_4, le)

            # Informe de los clientes actuales en la Cola del Cajero, separados
            # por tipo de Operación y mostrados en orden inverso a como serán
            # atendidos
            strInfoCC = """N-O <10>
Consignación $10300
+++++++++++++++++++++++++++++
N-O <9>
Consignación $12977
+++++++++++++++++++++++++++++
N-O <7>
Consignación $8000
.............................
N-O <4>
Retiro $17500
-----------------------------
N-O <6>
Retiro $5000
.............................
N-O <8>
Robo $0"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(strInfoCC, self.cajero.info(), Nt3_5, le)

            # Atención de 4 clientes [6:No, 7:Sí, 8:Robo, 9:Sí] de la CC
            self.cajero.atención()  # 6
            self.cajero.atención()  # 7
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <8>\n"
                                   "Robo $8000\n"
                                   "RECAUDO CAJERO $0",
                                   self.cajero.atención(), Nt3_2, le)
            self.cajero.atención()  # 9

            # Comprobación del tamaño de la CC
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(3, len(self.cajero), Nt3_3, le)

            # Escaneo del tamaño de la cola discriminado por tipo de Operación
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción((1, 2, 0), self.cajero.escaneo(), Nt3_4, le)

            # Informe de los clientes actuales en la Cola del Cajero, separados
            # por tipo de Operación y mostrados en orden inverso a como serán
            # atendidos
            strInfoCC = """N-O <10>
Consignación $10300
.............................
N-O <6>
Retiro $5000
-----------------------------
N-O <4>
Retiro $17500"""
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(strInfoCC, self.cajero.info(), Nt3_5, le)

            # Llamado a la seguridad: Ladrón NO encontrado.
            # CC Invertida [6, 4, 10]
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(False, self.cajero.seguridad(), Nt3_1, le)

            # Adición de nuevos clientes y ladrones la CC
            cli11 = Cliente(11, 'R', 16700)
            cli12 = Cliente(12, 'C', 30033)
            cli13 = Cliente(13, 'X')
            cli14 = Cliente(14, 'R', 8777)
            cli15 = Cliente(15, 'R', 9500)
            lst_cli = [cli11, cli12, cli13, cli14, cli15]
            for cli in lst_cli:
                self.cajero.a_la_cola(cli)

            # Comprobación del tamaño de la CC
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(8, len(self.cajero), Nt3_3, le)

            # Llamado a la seguridad. Ladrón SI encontrado.
            # CC Invertida [15, 14, 12, 11, 10, 4, 6]
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(True, self.cajero.seguridad(), Nt3_1, le)

            # Atención de 4 clientes [15:Sí, 14:No, 12:Sí, 11:Sí, 10:Sí, 4:Sí,
            #                         6:Sí, 14:No] de la CC
            self.cajero.atención()  # 15
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <14>\n"
                                   "Retiro $8777\n"
                                   "RECAUDO CAJERO $3477",
                                   self.cajero.atención(), Nt3_2, le)
            self.cajero.atención()  # 12
            self.cajero.atención()  # 11
            self.cajero.atención()  # 10
            self.cajero.atención()  # 4
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <6>\n"
                                   "Retiro $5000\n"
                                   "RECAUDO CAJERO $4610",
                                   self.cajero.atención(), Nt3_2, le)

            # Adición de nuevos clientes y ladrones la CC
            cli16 = Cliente(16, 'C', 35000)
            cli17 = Cliente(17, 'Z', 1000)
            cli18 = Cliente(18, 'C', 18690)
            cli19 = Cliente(19)
            cli20 = Cliente(20, 'R', 25000)
            lst_cli = [cli16, cli17, cli18, cli19, cli20]
            for cli in lst_cli:
                self.cajero.a_la_cola(cli)

            # Atención de 2 clientes de la CC
            self.cajero.atención()  # 14
            self.cajero.atención()  # 16

            # Llamado a la seguridad. Ladrón SI encontrado.
            # CC Invertida [14, 20, 19, 18]
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(True, self.cajero.seguridad(), Nt3_1, le)

            # Atención de 4 clientes de la CC
            self.cajero.atención()  # 14
            self.cajero.atención()  # 20

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <19>\n"
                                   "Robo $5833\n"
                                   "RECAUDO CAJERO $0",
                                   self.cajero.atención(), Nt3_2, le)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("N-O <18>\n"
                                   "Consignación $18690\n"
                                   "RECAUDO CAJERO $18690",
                                   self.cajero.atención(), Nt3_2, le)

            # Comprobación del tamaño de la CC
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(0, len(self.cajero), Nt3_3, le)
            """
            ################ PRESENTACCÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_nota(self):
        """
        INFORME DE LA NOTA FINAL
        """
        self.nota_final()


if __name__ == "__main__":
    unittest.main(verbosity=0)
