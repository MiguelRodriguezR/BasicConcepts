from listas.listas import LDE


class Pasajero:

    """
    Clase que permite modelar un pasajero, teniendo en cuenta los atributos de:
        * cédula
        * nombre
        * número del pasaje
    """

    def __init__(self, ced, nom=None, pasaje=None):
        """
        Constructor de la clase Pasajero, el cuál recibirá los parámetros
        necesarios para poder inicializar los atributos
        """
        self.cédula = ced
        self.nombre = nom
        self.num_pas = pasaje

    def __eq__(self, otro_pas):
        """
        Método de igualdad entre pasajeros, el cuál realizará la comparación
        con otro pasajero, teniendo en cuenta su cédula
        Retorna True, si los pasajeros son iguales x cédula
        Retorna False, en caso contrario
        """
        return (isinstance(otro_pas, Pasajero) and
                self.cédula == otro_pas.cédula)

    def __str__(self):
        """
        Método de presentación de un pasajero
        Retorna una cadena con información del Pasajero en el formato:
                {cédula - nombre - #número del pasaje}
            Ejm:
                {101'205.790 - Carlos Díaz - #p526}
        """
        return("{" + str(self.cédula) + " - "
               + str(self.nombre) + " - #"
               + str(self.num_pas) + "}")


class Vuelo:

    """
    Clase Vuelo, que manejará una lista de pasajeros, teniendo en cuenta:
        * número máximo de pasajeros del vuelo
        * lugar de destino del vuelo
        * fecha del vuelo
    """

    def __init__(self, num_max, destino, fecha):
        """
        Constructor de la clase Vuelo, que inicializará los atributos de la
        clase, incluyendo la lista de pasajeros
        """
        self.num_max = num_max
        self.destino = destino
        self.fecha = fecha
        self.lst_pasajero = LDE()

    def ingresar(self, nuevo_pas):
        """
        Método que permite realizar el registro de un nuevo pasajero a la lista
        del vuelo. Hay que tener en cuenta de no permitir el registro de
        más pasajeros cuando ya se ha alcanzado el número máximo de pasajeros
        en el vuelo.
        Retorna True, siempre y cuando se pueda ingresar el nuevo pasajero
        Retorna False, en caso contrario (cuando ya no hay más cupos)
        """
        if len(self.lst_pasajero) < self.num_max:
            self.lst_pasajero.agregar(nuevo_pas)
            return True
        else:
            return False

    def localizar(self, pas_buscar):
        """
        Método para localizar un pasajero registrado en el vuelo
        Retorna True, si el pasajero ya se encuentra registrado en la lista
        Retorna False, en caso contrario
        """
        return self.lst_pasajero.encontrar(pas_buscar)

    def bajar(self, pas_bajar):
        """
        Método que quita un pasajero dado de la lista de registro del vuelo
        Retorna True, siempre y cuando el pasajero sea borrado de la lista
        Retorna False, en caso contrario
        """
        return self.lst_pasajero.remover(pas_bajar,False)

    def listar_pasajeros_atras(self):
        """
        Método que muestra un reporte de los pasajeros en orden inverso a como
        fueron registrados originalmente
        """
        self.lst_pasajero.recorrer(True)

    def psjro_avanza(self):
        """
        Método que devuelve un pasajero cada vez que es llamado, siempre
        dirigiéndose hacia el último que fue registrado
        """
        return self.lst_pasajero.adelante()

    def psjro_retrocede(self):
        """
        Método que devuelve un pasajero cada vez que es llamado, siempre
        dirigiéndose hacia el primero que fue registrado
        """
        return self.lst_pasajero.atras()

    def __len__(self):
        """
        Método que retorna la cantidad de pasajeros actualmente registrados
        en la lista del Vuelo
        """
        return(len(self.lst_pasajero))

    def __str__(self):
        """
        Método de presentación del Vuelo, donde generará una cadena con la
        información del vuelo y los pasajeros registrados, según el siguiente
        formato:
                Vuelo a <destino_vuelo>
                Fecha: [fecha_vuelo]
                Capacidad (número_actual_pasajeros/capacidad_máxima_vuelo)
                {pasajero_1}{pasajero_2}{pasajero_3}{pasajero_4}...{pasajero_n}
        """
        # ban=0
        text = ("Vuelo a <" + self.destino + ">\nFecha: ["
                + self.fecha + "]\nCapacidad ("
                + str(len(self.lst_pasajero)) + "/"
                + str(self.num_max) + ")\n")
        for pasa in self.lst_pasajero:
            text = text + str(pasa)
        return text
