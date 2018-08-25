"""
    MODULE: agenda.py

    DESCRIPTION:
    Construcción de una aplicación que registra y controla las llamadas
    realizadas a diferentes Contactos.


    DATE: 12.05.2018 14:00:07 COT
"""
from ei.arboles import ABinBus
from ei.recorridos import str_pre_orden
from ei.recorridos import str_post_orden
from ei.recorridos import str_in_orden
__author_1__ = "NOMBRE DEL ESTUDIANTE 1 EN MAYUSCULAS"
__author_2__ = "NOMBRE DEL ESTUDIANTE 2 EN MAYUSCULAS"


class Contacto:
    """
    Clase Contacto que modela un contacto telefónico según:
        + el nombre del contacto
        + el teléfono del contacto
        + el operador telefónico del contacto
        + el número de minutos de llamadas al contacto

    NOTA: Hay que tener en cuenta que los valores por defecto son:
        * para el operador, una cadena vacía ("")
        * para los minutos, el valor entero cero (0)
    También validar la situación en la cuál si el número de minutos pasados al
    constructor es negativo, tomarán automáticamente el valor por defecto.
    """

    # Constructor de la clase Contacto
    def __init__(self):
        pass

    def __eq__(self):
        """
        Método que compara 2 objetos de tipo Contacto y verifica si el propio
        objeto es igual al otro objeto pasado como parámetro. Se dice que dos
        objetos de tipo Contacto son iguales si su nombres y téléfonos son
        iguales.

        Parámetros:
        ===========
        - o_c [Contacto]: El otro contacto con el cual se va a ser las
        comparaciones.

        Retorna:
        ========
        True si los contactos comparados son iguales. False en caso contrario.
        """
        pass

    def __lt__(self):
        """
        Método que compara 2 objetos de tipo Contacto y verifica si el propio
        objeto es menor al otro objeto pasado como parámetro. La comprobación
        se realizará teniendo en cuenta únicamente el nombre y el teléfono de
        c/Contacto.

        Parámetros:
        ===========
        - o_c [Contacto]: El otro contacto con el cual se va a ser las
        comparaciones.

        Retorna:
        ========
        True si el propio objeto es menor que el otro. False en caso
        contrario o cuando no son del mismo tipo.
        """
        pass

    def __gt__(self):
        """
        Método que compara 2 objetos de tipo Contacto y verifica si el propio
        objeto es mayor al otro objeto pasado como parámetro. La comprobación
        se realizará teniendo en cuenta únicamente el nombre y el teléfono de
        c/Contacto.

        Parámetros:
        ===========
        - o_c [Contacto]: El otro contacto con el cual se va a ser las
        comparaciones.

        Retorna:
        ========
        True si el propio objeto es mayor que el otro. False en caso
        contrario o cuando no son del mismo tipo.
        """
        pass

    def __str__(self):
        """
        Método que retorna una cadena con la representación del objeto de tipo
        Contacto.

        Retorna:
        ========
        La cadena de presentación del Contacto, según el siguiente
        formato:
                "<nombre> #teléfono(operador):minutos"
        """
        pass


class Agenda:
    """
    Clase Agenda que modela el comportamiento del registro de llamadas
    telefónicas realizadas a una serie de contactos agregados. Para ello se
    utilizará un Arbol Binario de Búsqueda, que permita almacenar y ordenar los
    diferentes contactos.
    """

    # Constructor de la clase Agenda
    def __init__(self):
        pass

    def agregarContacto(self):
        """
        Método que permite agregar un nuevo contacto al registro telefónico.

        Parámetros:
        ===========
        - nombre: Cadena con el nombre del contacto.
        - teléfono: Cadena con el número telefónico del contacto
        - operador: Cadena con el nombre del operador telefónico del contacto
        - minutos: Número de minutos registrados de las diferentes llamadas
          realizadas al contacto. Si no se pasan los minutos, estos tomarán
          como valor por defecto cero(0).

        Retorna:
        ========
        True si el nuevo contacto es agregado satisfactoriamente en
        el registro de contactos. False en caso contrario.
        """
        pass

    def borrarContacto(self):
        """
        Método que quita un contacto del registro de contactos.

        Parámetros:
        ===========
        - nombre: Una cadena con el nombre del contacto a ser eliminado.
        - teléfono: Una cadena con el teléfono a ser eliminado del registro de
          contactos.
        - mayor: Por defecto True, es un valor booleano que si es True
          determina que el reemplazo del contacto a eliminar (cuando este
          tiene sus dos hijos) se lo haga por el mayor de los menores. Si es
          False, lo hará por el menor de los mayores.

        Retorna:
        ========
        True si el contacto es eliminado del registro. False en caso contrario.
        """
        pass

    def llamarContacto(self):
        """
        Método que simula el llamado a un contacto, según su nombre y número
        telefónico, acumulando los minutos de la llamada en el contacto.

        Parámetros:
        ===========
        - nombre: Una cadena con el nombre del contacto a llamar.
        - teléfono: Una cadena con el número del contacto telefónico que se va
          a llamar.
        - minutos: Un valor entero que representa el número de minutos de
          duración de la llamada. Si el valor es negativo

        Retorna:
        ========
        Un valor entero positivo, con el total de minutos de llamada,
        realizados al contacto, incluidos los de la llamada actual. -1 en caso
        de que el contacto no corresponda a ninguno registrado o cuando la
        cantidad de minutos es negativa.
        """
        pass

    def consumoOperador(self):
        """
        Método que reporta el total de minutos realizados a un determinado
        operador, dentro del registro de contactos.

        Parámetros:
        ===========
        - operador: Una cadena con el nombre del operador a consultar.

        Retorna:
        ========
        Un valor entero con el total de minutos de llamadas registradas sobre
        los contactos pertenecientes al operador consultado.
        Si el nombre del operador NO EXISTE, se retornará un cero(0).
        """
        pass

    def infoHistorico(self):
        """
        Método que permite consultar los contactos registrados utilizando un
        determinado recorrido.

        Parámetros:
        ===========
        - tipo: Un valor entero {1, 2, 3} donde 1 significa la presentación de
          los contactos en preorden; 2 significa la presentación de los
          contactos en postorden y 3 significa la presentación de los contactos
          en inorden. El valor por defecto es 1. Cualquier otro valor no será
          considerado.

        Retorna:
        ========
        Una cadena de presentación del todos los contactos registrados
        actualmente en la Agenda, según el tipo de presentación. O bien, una
        cadena vacía cuando el tipo de presentación sea incorrecto.
        """
        pass

    def __len__(self):
        """
        Método que ...

        Retorna:
        ========
        Devuelve la cantidad de contactos registrados hasta el momento.
        """
        pass
