from vuelo import Pasajero, Vuelo
import unittest
from datetime import datetime
import sys
import traceback

nota = 0.0
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = list(range(8))


def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False  # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30 + colour) + str(text) + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)


class TestVuelo(unittest.TestCase):

    def comprobarAserción(self, val_esperado, val_evaluar, calif, linea):
        try:
            self.assertEqual(val_esperado, val_evaluar)
        except AssertionError:
            printout("\n---------- Error en la Comprobación ---------- \n",
                     RED)
            printout("Línea --> " + str(linea) + "\n", RED)
            printout("Valor Esperado: ", CYAN)
            printout(str(val_esperado), GREEN)
            printout("\nValor Obtenido: ", RED)
            printout(str(val_evaluar), MAGENTA)
            printout("\n----------------------------------------------\n", RED)
            printout("Prueba NO SUPERADA! (-" + str(calif) + ") \n", RED)
            calif = 0.0
        return calif

    # Configuración de las Pruebas: Creación inicial de 6 Pasajeros e
    # incorporación de los Pasajeros al Vuelo, con un máximo de 8 pasajeros
    def setUp(self):
        self.el_vuelo = Vuelo(8, "Bogotá", "30-abril-2014")

        # Creación del Pasajero 1
        self.p1 = Pasajero("c123", "Ana Gómez", "p123")
        self.el_vuelo.ingresar(self.p1)

        # Creación del Pasajero 2
        self.p2 = Pasajero("c234", "Blanca Solarte", "p234")
        self.el_vuelo.ingresar(self.p2)

        # Creación del Pasajero 3
        self.p3 = Pasajero("c345", "Carlos Benavides", "p345")
        self.el_vuelo.ingresar(self.p3)

        # Creación del Pasajero 4
        self.p4 = Pasajero("c456", "David Ocaña", "p456")
        self.el_vuelo.ingresar(self.p4)

        # Creación del Pasajero 5
        self.p5 = Pasajero("c567", "Esperanza Caicedo", "p567")
        self.el_vuelo.ingresar(self.p5)

        # Creación del Pasajero 6
        self.p6 = Pasajero("c678", "Francisco Díaz", "p678")
        self.el_vuelo.ingresar(self.p6)

    # Prueba de Presentación de Pasajeros del Vuelo
    # Calificación Máxima = 1.0
    def test_1_lista_Pasajeros(self):
        global nota
        smax_nota = '1.00'
        nota_test = nota
        self.maxDiff = None
        printout("\nIniciando Test #1: Lista de Pasajeros\n", BLUE)
        printout("==============================================\n", BLUE)

        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción('''Vuelo a <Bogotá>
Fecha: [30-abril-2014]
Capacidad (6/8)
{c123 - Ana Gómez - #p123}{c234 - Blanca Solarte - #p234}\
{c345 - Carlos Benavides - #p345}{c456 - David Ocaña - #p456}\
{c567 - Esperanza Caicedo - #p567}{c678 - Francisco Díaz - #p678}''',
                                       str(self.el_vuelo), 0.25, le)

        # Creación del Pasajero 7
        p7 = Pasajero("c789", "Gisella López", "p789")
        self.el_vuelo.ingresar(p7)
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción('''Vuelo a <Bogotá>
Fecha: [30-abril-2014]
Capacidad (7/8)
{c123 - Ana Gómez - #p123}{c234 - Blanca Solarte - #p234}\
{c345 - Carlos Benavides - #p345}{c456 - David Ocaña - #p456}\
{c567 - Esperanza Caicedo - #p567}{c678 - Francisco Díaz - #p678}\
{c789 - Gisella López - #p789}''',
                                       str(self.el_vuelo), 0.25, le)

        # Creación del Pasajero 8
        p8 = Pasajero("c890", "Humberto Mora", "p890")
        self.el_vuelo.ingresar(p8)
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción('''Vuelo a <Bogotá>
Fecha: [30-abril-2014]
Capacidad (8/8)
{c123 - Ana Gómez - #p123}{c234 - Blanca Solarte - #p234}\
{c345 - Carlos Benavides - #p345}{c456 - David Ocaña - #p456}\
{c567 - Esperanza Caicedo - #p567}{c678 - Francisco Díaz - #p678}\
{c789 - Gisella López - #p789}{c890 - Humberto Mora - #p890}''',
                                       str(self.el_vuelo), 0.25, le)

        # Creación del Pasajero 9 [NO ACEPTADO POR SOBRE-CUPO DEL VUELO]
        p9 = Pasajero("c901", "Ismael Cerón", "p901")
        self.el_vuelo.ingresar(p9)
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción('''Vuelo a <Bogotá>
Fecha: [30-abril-2014]
Capacidad (8/8)
{c123 - Ana Gómez - #p123}{c234 - Blanca Solarte - #p234}\
{c345 - Carlos Benavides - #p345}{c456 - David Ocaña - #p456}\
{c567 - Esperanza Caicedo - #p567}{c678 - Francisco Díaz - #p678}\
{c789 - Gisella López - #p789}{c890 - Humberto Mora - #p890}''',
                                       str(self.el_vuelo), 0.25, le)

        printout("\nNota Test #1 = ", GREEN)
        printout("{0:0.2f}".format(nota - nota_test) + "/" + smax_nota
                 + "\n", CYAN)
        printout("==============================================\n", BLUE)

    # Prueba para localizar un Pasajero por su cédula
    # Calificación Máxima = 0.8
    def test_2_localizar(self):
        global nota
        smax_nota = '0.80'
        nota_test = nota
        printout("\nIniciando Test #2: Localizar Pasajero\n", BLUE)
        printout("==============================================\n", BLUE)

        # Adición de Nuevos Pasajeros
        p7 = Pasajero("c789", "Gisella López", "p789")
        self.el_vuelo.ingresar(p7)
        p8 = Pasajero("c890", "Humberto Mora", "p890")
        self.el_vuelo.ingresar(p8)
        p9 = Pasajero("c901", "Ismael Cerón", "p901")
        self.el_vuelo.ingresar(p9)

        # El Pasajero 3 SI EXISTE!
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción(True, self.el_vuelo.localizar(self.p3),
                                       0.16, le)

        # El Pasajero 1 CLON SI EXISTE! Analiza sólo la cédula, no el nombre
        pC1 = Pasajero("c123", "Mario Moreno")
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción(True, self.el_vuelo.localizar(pC1),
                                       0.16, le)

        # El Pasajero 9 NO EXISTE! No fue Ingresado por sobre-cupo
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción(False, self.el_vuelo.localizar(p9),
                                       0.16, le)

        # El Pasajero 8 CLON SI EXISTE! Analiza sólo la cédula, no el pasaje
        pC8 = Pasajero("c890", pasaje="p890")
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción(True, self.el_vuelo.localizar(pC8),
                                       0.16, le)

        # El Pasajero 7 CLON NO EXISTE! Analiza sólo la cédula, que no existe
        pC7 = Pasajero("c789c")
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción(False, self.el_vuelo.localizar(pC7),
                                       0.16, le)

        printout("\nNota Test #2 = ", GREEN)
        printout("{0:0.2f}".format(nota - nota_test) + "/" + smax_nota
                 + "\n", CYAN)
        printout("==============================================\n", BLUE)

    # Prueba para Bajar un Pasajero del Vuelo
    # Calificación Máxima = 1.2
    def test_3_bajar(self):
        global nota
        smax_nota = '1.20'
        nota_test = nota
        printout("\nIniciando Test #3: Bajar Pasajeros\n", BLUE)
        printout("==============================================\n", BLUE)

        # Bajar al Pasajero 3, ubicándolo por su cédula, previa comprobación
        # de que exista y posterior comprobación de que ya no figura en lista
        le = (traceback.extract_stack()[-1])[1] + 1
        self.comprobarAserción(True, self.el_vuelo.localizar(self.p3), 0, le)
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción(True, self.el_vuelo.bajar(self.p3),
                                       0.25, le)
        le = (traceback.extract_stack()[-1])[1] + 1
        self.comprobarAserción(False, self.el_vuelo.localizar(self.p3), 0, le)

        # Bajar al Pasajero 6, ubicándolo por su cédula, previa comprobación
        # de que exista y posterior comprobación de que ya no figura en lista
        le = (traceback.extract_stack()[-1])[1] + 1
        self.comprobarAserción(True, self.el_vuelo.localizar(self.p6), 0, le)
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción(True, self.el_vuelo.bajar(self.p6),
                                       0.25, le)
        le = (traceback.extract_stack()[-1])[1] + 1
        self.comprobarAserción(False, self.el_vuelo.localizar(self.p6), 0, le)

        # Adición de un Nuevo Pasajero
        p7 = Pasajero("c789", "Gisella López", "p789")
        self.el_vuelo.ingresar(p7)

        # Bajar al Pasajero 1, ubicándolo por su cédula, previa comprobación
        # de que exista y posterior comprobación de que ya no figura en lista
        le = (traceback.extract_stack()[-1])[1] + 1
        self.comprobarAserción(True, self.el_vuelo.localizar(self.p1), 0, le)
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción(True, self.el_vuelo.bajar(self.p1),
                                       0.25, le)
        le = (traceback.extract_stack()[-1])[1] + 1
        self.comprobarAserción(False, self.el_vuelo.localizar(self.p1), 0, le)

        # Adición de un Nuevo Pasajero
        p8 = Pasajero("c890", "Humberto Mora", "p890")
        self.el_vuelo.ingresar(p8)

        # Comprobación de la cantidad de Pasajeros actualmente en el Vuelo
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción(5, len(self.el_vuelo), 0.25, le)

        # Comprobación de la presentación de los Pasajeros del vuelo, después
        # de las bajas
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción('''Vuelo a <Bogotá>
Fecha: [30-abril-2014]
Capacidad (5/8)
{c234 - Blanca Solarte - #p234}{c456 - David Ocaña - #p456}\
{c567 - Esperanza Caicedo - #p567}{c789 - Gisella López - #p789}\
{c890 - Humberto Mora - #p890}''',
                                       str(self.el_vuelo), 0.2, le)

        printout("\nNota Test #3 = ", GREEN)
        printout("{0:0.2f}".format(nota - nota_test) + "/" + smax_nota
                 + "\n", CYAN)
        printout("==============================================\n", BLUE)

    # Prueba para obtener un Pasajero según su posición actual en la lista
    # del Vuelo
    # Calificación Máxima = 2.2
    def test_4_psjro_atras_adelante(self):
        global nota
        smax_nota = '2.20'
        nota_test = nota
        printout(
            "\nIniciando Test #4: Obtener Pasajero por desplazamiento\n", BLUE)
        printout("==============================================\n", BLUE)

        # Devuleve el Pasajero 1
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción('{c123 - Ana Gómez - #p123}',
                                       str(self.el_vuelo.psjro_retrocede()),
                                       0.275, le)

        # Avanzamos 3 posiciones en la lista de Pasajeros y...
        self.el_vuelo.psjro_avanza()  # p2
        self.el_vuelo.psjro_avanza()  # p3
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción('{c456 - David Ocaña - #p456}',
                                       str(self.el_vuelo.psjro_avanza()),
                                       0.275, le)

        # Avanzamos y retrocedemos varias posiciones en la lista de Pasajeros..
        self.el_vuelo.psjro_avanza()  # p5
        self.el_vuelo.psjro_retrocede()  # p4
        self.el_vuelo.psjro_retrocede()  # p3
        self.el_vuelo.psjro_avanza()  # p4
        self.el_vuelo.psjro_avanza()  # p5
        self.el_vuelo.psjro_avanza()  # p6
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción('{c678 - Francisco Díaz - #p678}',
                                       str(self.el_vuelo.psjro_avanza()),
                                       0.275, le)

        # Ingresamos un nuevo pasajero y cambiamos de posición...
        p7 = Pasajero("c789", "Gisella López", "p789")
        self.el_vuelo.ingresar(p7)
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción('{c789 - Gisella López - #p789}',
                                       str(self.el_vuelo.psjro_avanza()),
                                       0.275, le)

        # Bajamos un pasajero y nos movemos al lugar del Pasajero bajado
        self.el_vuelo.bajar(self.p3)
        self.el_vuelo.psjro_retrocede()  # p6
        self.el_vuelo.psjro_retrocede()  # p5
        self.el_vuelo.psjro_retrocede()  # p4
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción('{c234 - Blanca Solarte - #p234}',
                                       str(self.el_vuelo.psjro_retrocede()),
                                       0.275, le)

        # Bajamos un pasajero, el de la posición actual
        self.el_vuelo.psjro_avanza()  # p4
        self.el_vuelo.bajar(self.p4)
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción('{c123 - Ana Gómez - #p123}',
                                       str(self.el_vuelo.psjro_retrocede()),
                                       0.275, le)

        # Bajamos pasajero del inicio y avanzamos
        self.el_vuelo.bajar(self.p1)
        le = (traceback.extract_stack()[-1])[1] + 1


        nota += self.comprobarAserción('{c234 - Blanca Solarte - #p234}',
                                       str(self.el_vuelo.psjro_retrocede()),
                                       0.275, le)

        # Avanzamos al último de lista de Pasajeros y lo eliminamos
        self.el_vuelo.psjro_avanza()  # p5
        self.el_vuelo.psjro_avanza()  # p6
        self.el_vuelo.psjro_avanza()  # p7
        self.el_vuelo.bajar(p7)
        self.el_vuelo.psjro_retrocede()  # p5
        self.el_vuelo.psjro_avanza()  # p6
        le = (traceback.extract_stack()[-1])[1] + 1
        nota += self.comprobarAserción('{c678 - Francisco Díaz - #p678}',
                                       str(self.el_vuelo.psjro_avanza()),
                                       0.275, le)

        printout("\nNota Test #4 = ", GREEN)
        printout("{0:0.2f}".format(nota - nota_test) + "/" + smax_nota
                 + "\n", CYAN)
        printout("==============================================\n", BLUE)

    # Prueba de VISUALIZACIÓN de los pasajeros listados para atrás ...
    # Calificación Máxima = 0.8
    def test_5_listar_pasajeros_atras(self):
        global nota
        smax_nota = '0.80'
        nota_test = nota
        printout(
            "\nIniciando Test #5: Visualización de los pasajeros para atrás\n",
            BLUE)
        printout("==============================================\n", BLUE)

        self.el_vuelo.listar_pasajeros_atras()
        while True:
            calificar = input(
                ":: ¿El orden y la visualización son correctos? [S/n]")
            if calificar.upper() in ['S', 'N']:
                break
        if calificar.upper() == 'S':
            nota += 0.8

        printout("\nNota Test #5 = ", GREEN)
        printout("{0:0.2f}".format(nota - nota_test) + "/" + smax_nota
                 + "\n", CYAN)
        printout("==============================================\n", BLUE)

    def test_nota(self):
        printout("\n\n================ ATENCIÓN =====================", GREEN)
        printout("\nNOTA mínima Aproximada = {0:0.2f}".format(nota), CYAN)
        printout("\nSujeta a VERIFICACIÓN!", RED)
        printout("\n" +
                 str(datetime.now().strftime("%A %d, %B %Y - %I:%M%p ")), BLUE)
        printout("\n===============================================\n", GREEN)


if __name__ == "__main__":
    unittest.main(verbosity=0)
