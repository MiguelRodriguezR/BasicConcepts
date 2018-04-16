#!/usr/bin/env python3
from test_builder import TestBuilder
from ei.q_s import Stack, Queue
import unittest
import traceback


class TestStackAndQueue(TestBuilder):
    # Es posible desactivar cualquiera de las pruebas colocando el valor de
    # cero a cualquiera de ellas en el siguiente diccionario:
    dict_pruebas = {"extract_stack": 1, "varios_stack": 1,
                    "extract_queue": 1, "varios_queue": 1}

    # Configuración de las Pruebas: Creación inicial de 10 números para
    # inicializar Stacks y Queues
    def setUp(self):
        self.pila = Stack(" .-. ")
        self.cola = Queue()
        # Stack and Queue [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for elm in range(1, 11):
            self.pila.apilar(elm)
            self.cola.encolar(elm)

    def test_0(self):
        self.presentación("Test Stack and Queue")

    # Verificación de los elementos de la Stack "apilar", extracción
    # "desapilar", valores próximos a salir "cima", tamaño y presentación
    # Calificación Máxima = 0.75
    def test_1_extract_stack(self):
        iTest = 1
        sTitle = ("Comprobación de apilar, desapilar, cima, tamaño y "
                  "presentación de un Stack")
        tam_pil = len(self.pila)
        fMax_nota = 0.75
        Nt1_1 = fMax_nota * 0.20 / 5                # str(Stack)
        Nt1_2 = fMax_nota * 0.10 / (tam_pil + 1)    # Tamaño
        Nt1_3 = fMax_nota * 0.20 / (tam_pil + 1)    # Cima
        Nt1_4 = fMax_nota * 0.50 / (tam_pil + 1)    # Desapilar
        if self.dict_pruebas.get("extract_stack"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Presentación del estado de la Stack
            strPil = "10 .-. 9 .-. 8 .-. 7 .-. 6 .-. 5 .-. 4 .-. 3 .-. 2 .-. 1"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(strPil, str(self.pila), Nt1_1, le)

            # Extraer de la Stack, tamaño, presentación y cima
            tam_pil2 = tam_pil
            cr_i = 0
            for i_a in range(tam_pil, 0, -1):
                if i_a == 8:
                    strPil = "8 .-. 7 .-. 6 .-. 5 .-. 4 .-. 3 .-. 2 .-. 1"
                    le = (traceback.extract_stack()[-1])[1] + 1
                    self.comprobarAserción(strPil, str(self.pila), Nt1_1, le)
                elif i_a == 5:
                    strPil = "5 .-. 4 .-. 3 .-. 2 .-. 1"
                    le = (traceback.extract_stack()[-1])[1] + 1
                    self.comprobarAserción(strPil, str(self.pila), Nt1_1, le)
                elif i_a == 1:
                    strPil = "1"
                    le = (traceback.extract_stack()[-1])[1] + 1
                    self.comprobarAserción(strPil, str(self.pila), Nt1_1, le)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción(tam_pil2, len(self.pila),
                                       Nt1_2, le, cr_i)
                self.comprobarAserción(i_a, self.pila.cima(),
                                       Nt1_3, le + 2, cr_i)
                self.comprobarAserción(i_a, self.pila.desapilar(),
                                       Nt1_4, le + 4, cr_i)
                tam_pil2 -= 1
                cr_i += 1

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción("", str(self.pila), Nt1_1, le)
            self.comprobarAserción(0, len(self.pila), Nt1_2, le + 1)
            self.comprobarAserción(None, self.pila.cima(), Nt1_3, le + 2)
            self.comprobarAserción(None, self.pila.desapilar(), Nt1_4, le + 3)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    # Pruebas varias del comportamiento de un Stack
    # Calificación Máxima = 0.75
    def test_2_varios_stack(self):
        iTest = 2
        sTitle = "Pruebas Varias Stack"
        fMax_nota = 0.75
        Nt2_1 = fMax_nota * 0.30 / 11   # Apilar
        Nt2_2 = fMax_nota * 0.10 / 7    # Tamaño
        Nt2_3 = fMax_nota * 0.30 / 19   # Desapilar
        Nt2_4 = fMax_nota * 0.20 / 7    # str(Stack)
        Nt2_5 = fMax_nota * 0.10 / 6    # Cima
        if self.dict_pruebas.get("varios_stack"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Prueba de Homogeneidad
            strPil = "10 .-. 9 .-. 8 .-. 7 .-. 6 .-. 5 .-. 4 .-. 3 .-. 2 .-. 1"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(False, self.pila.apilar('A'), Nt2_1, le)
            self.comprobarAserción(10, len(self.pila), Nt2_2, le + 1)
            self.comprobarAserción(strPil, str(self.pila), Nt2_4, le + 2)

            # Pruebas varias sobre Stacks
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(True, self.pila.apilar(11), Nt2_1, le)
            self.comprobarAserción(True, self.pila.apilar(12), Nt2_1, le + 1)

            strPil = ("12 .-. 11 .-. 10 .-. 9 .-. 8 .-. 7 .-. 6 .-. 5 .-. 4 "
                      ".-. 3 .-. 2 .-. 1")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(12, len(self.pila), Nt2_2, le)
            self.comprobarAserción(strPil, str(self.pila), Nt2_4, le + 1)
            self.comprobarAserción(12, self.pila.desapilar(), Nt2_3, le + 2)
            self.comprobarAserción(11, self.pila.desapilar(), Nt2_3, le + 3)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(10, self.pila.desapilar(), Nt2_3, le)
            self.comprobarAserción(True, self.pila.apilar(13), Nt2_1, le + 1)
            self.comprobarAserción(False, self.pila.apilar('7'), Nt2_1, le + 2)
            self.comprobarAserción(True, self.pila.apilar(14), Nt2_1, le + 3)
            self.comprobarAserción(14, self.pila.desapilar(), Nt2_3, le + 4)
            self.comprobarAserción(13, self.pila.desapilar(), Nt2_3, le + 5)
            self.comprobarAserción(9, self.pila.desapilar(), Nt2_3, le + 6)
            self.comprobarAserción(8, self.pila.desapilar(), Nt2_3, le + 7)

            strPil = "6 .-. 5 .-. 4 .-. 3 .-. 2 .-. 1"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(7, self.pila.desapilar(), Nt2_3, le)
            self.comprobarAserción(6, len(self.pila), Nt2_2, le + 1)
            self.comprobarAserción(strPil, str(self.pila), Nt2_4, le + 2)
            self.comprobarAserción(6, self.pila.cima(), Nt2_5, le + 3)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(True, self.pila.apilar(14), Nt2_1, le)
            self.comprobarAserción(14, self.pila.cima(), Nt2_5, le + 1)
            self.comprobarAserción(14, self.pila.desapilar(), Nt2_3, le + 2)
            self.comprobarAserción(6, self.pila.desapilar(), Nt2_3, le + 3)
            self.comprobarAserción(5, self.pila.desapilar(), Nt2_3, le + 4)
            self.comprobarAserción(4, self.pila.desapilar(), Nt2_3, le + 5)

            strPil = "2 .-. 1"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(3, self.pila.desapilar(), Nt2_3, le)
            self.comprobarAserción(2, len(self.pila), Nt2_2, le + 1)
            self.comprobarAserción(strPil, str(self.pila), Nt2_4, le + 2)
            self.comprobarAserción(2, self.pila.cima(), Nt2_5, le + 3)
            self.comprobarAserción(2, self.pila.desapilar(), Nt2_3, le + 4)
            self.comprobarAserción(1, self.pila.desapilar(), Nt2_3, le + 5)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(None, self.pila.desapilar(), Nt2_3, le)
            self.comprobarAserción(0, len(self.pila), Nt2_2, le + 1)
            self.comprobarAserción("", str(self.pila), Nt2_4, le + 2)
            self.comprobarAserción(True, self.pila.apilar(15), Nt2_1, le + 3)
            self.comprobarAserción(True, self.pila.apilar(16), Nt2_1, le + 4)
            self.comprobarAserción(False, self.pila.apilar('1'), Nt2_1, le + 5)
            self.comprobarAserción(True, self.pila.apilar(17), Nt2_1, le + 6)

            strPil = "16 .-. 15"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(17, self.pila.desapilar(), Nt2_3, le)
            self.comprobarAserción(2, len(self.pila), Nt2_2, le + 1)
            self.comprobarAserción(strPil, str(self.pila), Nt2_4, le + 2)
            self.comprobarAserción(16, self.pila.cima(), Nt2_5, le + 3)
            self.comprobarAserción(16, self.pila.desapilar(), Nt2_3, le + 4)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(15, self.pila.cima(), Nt2_5, le)
            self.comprobarAserción(15, self.pila.desapilar(), Nt2_3, le + 1)
            self.comprobarAserción(None, self.pila.cima(), Nt2_5, le + 2)
            self.comprobarAserción(0, len(self.pila), Nt2_2, le + 3)
            self.comprobarAserción("", str(self.pila), Nt2_4, le + 4)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    # Verificación de los elementos de Queue "encolar", extracción
    # "desencolar", valores próximos a salir "frente", tamaño e iteración
    # Calificación Máxima = 0.75
    def test_3_extract_queues(self):
        iTest = 3
        sTitle = ("Comprobación de encolar, desencolar, frente, tamaño e "
                  "iteración de una Queue")
        tam_col = len(self.cola)
        fMax_nota = 0.75
        Nt3_1 = fMax_nota * 0.20 / 5                # Iteración(Queue)
        Nt3_2 = fMax_nota * 0.10 / (tam_col + 1)    # Tamaño
        Nt3_3 = fMax_nota * 0.20 / (tam_col + 1)    # Frente
        Nt3_4 = fMax_nota * 0.50 / (tam_col + 1)    # Desencolar
        if self.dict_pruebas.get("extract_queue"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Iteración de la Queue
            iSuma = 0
            for i in self.cola:
                iSuma += i
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(55, iSuma, Nt3_1, le)

            # Extraer de la Queue, tamaño, iteración y frente
            tam_col2 = tam_col
            cr_i = 0
            for i_a in range(1, tam_col + 1):
                if i_a == 10:
                    iSuma = 0
                    for i in self.cola:
                        iSuma += i
                    le = (traceback.extract_stack()[-1])[1] + 1
                    self.comprobarAserción(10, iSuma, Nt3_1, le)
                elif i_a == 6:
                    iSuma = 0
                    for i in self.cola:
                        iSuma += i
                    le = (traceback.extract_stack()[-1])[1] + 1
                    self.comprobarAserción(40, iSuma, Nt3_1, le)
                elif i_a == 3:
                    iSuma = 0
                    for i in self.cola:
                        iSuma += i
                    le = (traceback.extract_stack()[-1])[1] + 1
                    self.comprobarAserción(52, iSuma, Nt3_1, le)

                le = (traceback.extract_stack()[-1])[1] + 2
                self.comprobarAserción(tam_col2, len(self.cola),
                                       Nt3_2, le, cr_i)
                self.comprobarAserción(i_a, self.cola.frente(),
                                       Nt3_3, le + 2, cr_i)
                self.comprobarAserción(i_a, self.cola.desencolar(),
                                       Nt3_4, le + 4, cr_i)
                tam_col2 -= 1
                cr_i += 1

            iSuma = 0
            for i in self.cola:
                iSuma += i
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(0, iSuma, Nt3_1, le)
            self.comprobarAserción(0, len(self.cola), Nt3_2, le + 1)
            self.comprobarAserción(None, self.cola.frente(), Nt3_3, le + 2)
            self.comprobarAserción(None, self.cola.desencolar(), Nt3_4, le + 3)
            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    # Pruebas varias del comportamiento de un Queue
    # Calificación Máxima = 0.75
    def test_4_varios_queue(self):
        iTest = 4
        sTitle = "Pruebas Varias Queue"
        fMax_nota = 0.75
        Nt4_1 = fMax_nota * 0.30 / 11   # Encolar
        Nt4_2 = fMax_nota * 0.10 / 7    # Tamaño
        Nt4_3 = fMax_nota * 0.30 / 20   # Desencolar
        Nt4_4 = fMax_nota * 0.20 / 7    # Iteración(Queue)
        Nt4_5 = fMax_nota * 0.10 / 7    # Frente
        if self.dict_pruebas.get("varios_queue"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Prueba de Homogeneidad
            iSuma = 0
            for i in self.cola:
                iSuma += i
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(False, self.cola.encolar('Z'), Nt4_1, le)
            self.comprobarAserción(10, len(self.cola), Nt4_2, le + 1)
            self.comprobarAserción(55, iSuma, Nt4_4, le + 2)

            # Pruebas varias sobre Queues
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(True, self.cola.encolar(11), Nt4_1, le)
            self.comprobarAserción(True, self.cola.encolar(12), Nt4_1, le + 1)

            iSuma = 0
            for i in self.cola:
                iSuma += i
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(12, len(self.cola), Nt4_2, le)
            self.comprobarAserción(78, iSuma, Nt4_4, le + 2)
            self.comprobarAserción(1, self.cola.desencolar(), Nt4_3, le + 3)
            self.comprobarAserción(2, self.cola.desencolar(), Nt4_3, le + 4)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(3, self.cola.desencolar(), Nt4_3, le)
            self.comprobarAserción(True, self.cola.encolar(13), Nt4_1, le + 1)
            self.comprobarAserción(False, self.cola.encolar(7.7),
                                   Nt4_1, le + 2)
            self.comprobarAserción(True, self.cola.encolar(14), Nt4_1, le + 4)
            self.comprobarAserción(4, self.cola.desencolar(), Nt4_3, le + 5)
            self.comprobarAserción(5, self.cola.desencolar(), Nt4_3, le + 6)
            self.comprobarAserción(6, self.cola.desencolar(), Nt4_3, le + 7)
            self.comprobarAserción(7, self.cola.desencolar(), Nt4_3, le + 8)

            iSuma = 0
            for i in self.cola:
                iSuma += i
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(8, self.cola.desencolar(), Nt4_3, le)
            self.comprobarAserción(6, len(self.cola), Nt4_2, le + 1)
            self.comprobarAserción(77, iSuma, Nt4_4, le + 2)
            self.comprobarAserción(9, self.cola.frente(), Nt4_5, le + 3)

            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(True, self.cola.encolar(14), Nt4_1, le)
            self.comprobarAserción(9, self.cola.frente(), Nt4_5, le + 1)
            self.comprobarAserción(9, self.cola.desencolar(), Nt4_3, le + 2)
            self.comprobarAserción(10, self.cola.desencolar(), Nt4_3, le + 3)
            self.comprobarAserción(11, self.cola.desencolar(), Nt4_3, le + 4)
            self.comprobarAserción(12, self.cola.desencolar(), Nt4_3, le + 5)

            iSuma = 0
            for i in self.cola:
                iSuma += i
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(13, self.cola.desencolar(), Nt4_3, le)
            self.comprobarAserción(2, len(self.cola), Nt4_2, le + 1)
            self.comprobarAserción(41, iSuma, Nt4_4, le + 2)
            self.comprobarAserción(14, self.cola.frente(), Nt4_5, le + 3)
            self.comprobarAserción(14, self.cola.desencolar(), Nt4_3, le + 4)
            self.comprobarAserción(14, self.cola.desencolar(), Nt4_3, le + 5)

            iSuma = 0
            for i in self.cola:
                iSuma += i
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(None, self.cola.desencolar(), Nt4_3, le)
            self.comprobarAserción(0, len(self.cola), Nt4_2, le + 1)
            self.comprobarAserción(0, iSuma, Nt4_4, le + 2)
            self.comprobarAserción(True, self.cola.encolar(15), Nt4_1, le + 3)
            self.comprobarAserción(True, self.cola.encolar(16), Nt4_1, le + 4)
            self.comprobarAserción(False, self.cola.encolar(100.5),
                                   Nt4_1, le + 5)
            self.comprobarAserción(True, self.cola.encolar(17), Nt4_1, le + 7)

            iSuma = 0
            for i in self.cola:
                iSuma += i
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(15, self.cola.frente(), Nt4_5, le)
            self.comprobarAserción(15, self.cola.desencolar(), Nt4_3, le + 1)
            self.comprobarAserción(2, len(self.cola), Nt4_2, le + 2)
            self.comprobarAserción(48, iSuma, Nt4_4, le + 3)
            self.comprobarAserción(16, self.cola.frente(), Nt4_5, le + 4)
            self.comprobarAserción(16, self.cola.desencolar(), Nt4_3, le + 5)
            self.comprobarAserción(17, self.cola.frente(), Nt4_5, le + 6)
            self.comprobarAserción(17, self.cola.desencolar(), Nt4_3, le + 7)
            self.comprobarAserción(None, self.cola.frente(), Nt4_5, le + 8)
            self.comprobarAserción(None, self.cola.desencolar(), Nt4_3, le + 9)
            self.comprobarAserción(0, len(self.cola), Nt4_2, le + 10)
            iSuma = 0
            for i in self.cola:
                iSuma += i
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(0, iSuma, Nt4_4, le)

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
