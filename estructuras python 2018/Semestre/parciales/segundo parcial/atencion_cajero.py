from ei.colas_prioridad import PriorityQueue
from ei.pilas_colas import *

#!/usr/bin/env python3
"""
    PROJECT: Taller 3

    MODULE: atencion_cajero.py

    DESCRIPTION:
    El cajero de un banco necesita que se pueda registrar los diferentes
    movimientos que varios clientes realizan en él, a través de una cola de
    atención, en la cual tambien pueden venir infiltrados "clientes" con claras
    intensiones de robarlo.

    DATE: 14.04.2018 14:00:10 COT

    AUTHORS: Student 1 and Student 2
"""


class Cliente:
    """
    Esta clase se encarga de modelar un cliente que va a ser atentido por el
    cajero. Tiene como características:
        * Un número de operación asignado originalmente al cliente.
        * La operación a realizar en el cajero:
            - 'C', para consignación
            - 'R', para retiro
            - 'X', para robar el cajero (valor por defecto)
        * El monto en $$$ que interviene en la operación. El monto por defecto
          será cero.

    NOTA: Cualquier otra letra utilizada para la operación NO SERA PERMITIDA, y
    en este caso se asumirá que la operación se trata de un robo y el monto
    especificado, sea cual sea, será $0.
    """

    # Especifiquen y documenten el constructor de la clase Cliente
    def __init__(self,num,op="nope",mont=0):
        self.numero = num
        self.operacion = op
        self.monto = mont
        if(self.operacion not in ['C','R','X']):
            self.operacion = 'X'
            self.monto = 0


    def __str__(self):
        """
        Método que retorna la presentación de las características del cliente.

        Retorna:
        ========
        Una cadena con la siguiente especificación:

                "N-O <num. oper>
                 tipo de operación $monto de la operación"

        donde tipo de operación puede ser:
                 - "Consignación"
                 - "Retiro"
                 - "Robo"
        :rtype: str
        """
        operacion = ''
        if(self.operacion == 'X'):
            operacion = 'Robo'
        if(self.operacion == 'R'):
            operacion = 'Retiro'
        if(self.operacion == 'C'):
            operacion = 'Consignación'

        return 'N-O <'+str(self.numero)+'>\n'+operacion+' $'+str(self.monto)


class Cajero:
    """
    Clase que modela el cajero de un banco, el cual se caracteriza por:
        * Manejar un recaudo, el cual comienza al inicio de operaciones en cero
          pesos.
        * Una cola de clientes para ser atendida.
    """

    def __init__(self):
        self.recaudo = 0
        self.clientes = PriorityQueue()

    # Especifiquen y documenten el constructor de la clase Cajero

    def a_la_cola(self, nuevo_cli):
        """
        Método que agrega un nuevo cliente a la cola del cajero. Validar que el
        nuevo cliente tenga un monto en su operación de al menos $0.

        Parámetros:
        ===========
        - nuevo_clie [Cliente]: El cliente que se va a adicionar a la cola del
          cajero.

        Retorna:
        ========
        True si el nuevo cliente es adicionado satisfactoriamente a la cola.
        False en caso contrario.
        """
        if(nuevo_cli.monto>=0):
            return self.clientes.encolar(nuevo_cli,1)
        return False

    def atención(self):
        """
        Método que atiende uno por uno los clientes del cajero, en cada llamada
        a éste método. Cuando el cliente atendido pretender retirar del cajero,
        se debe validar que existan suficientes recursos/fondos para realizar
        la operación. En el caso en que no se pueda realizar el retiro, el
        cliente deberá enviarse al FINAL de la cola. Cuando el cliente atendido
        pretende robar el cajero, éste deberá modificar su monto al valor
        robado, que en este caso será el total recaudado hasta el momento antes
        del robo por parte del cajero. En el caso de un retiro exitoso o de un
        robo, se deberá afectar el valor recaudado del cajero.

        Retorna:
        ========
        Una cadena con información del cliente y el estado actual de
        recaudación del cajero, después de realizar la operación, de acuerdo al
        siguiente formato:

            "Presentación
             del Cliente
             RECAUDO CAJERO $Recaudo del cajero
            "

        En caso de que no existan clientes en la cola, retornar en vez de la
        presentación del cliente una cadena con el siguiente formato:

            "COLA DE CLIENTES VACIA
             RECAUDO CAJERO $Recaudo del cajero
             "
        """
        if (not self.clientes.es_vacia()):
            cliente_actual = self.clientes.desencolar()
            if(cliente_actual.operacion == 'X'):
                cliente_actual.monto = self.recaudo
                self.recaudo = 0
            elif(cliente_actual.operacion == 'R'):
                dinero = self.recaudo - cliente_actual.monto
                if(dinero < 0):
                    self.clientes.encolar(cliente_actual,1)
                else:
                    self.recaudo = self.recaudo - cliente_actual.monto
            elif(cliente_actual.operacion == 'C'):
                self.recaudo+=cliente_actual.monto
            return str(cliente_actual)+'\nRECAUDO CAJERO $'+str(self.recaudo)
        return 'COLA DE CLIENTES VACIA\nRECAUDO CAJERO $'+str(self.recaudo)

    def seguridad(self):
        """
        Método que se encarga de la seguridad del cajero. Como la mayoría de
        servicios de seguridad, un tanto ineficientes, este sistema solamente
        permite la captura y expulsión de la cola de clientes de un ladrón en
        cada llamado. Por lo tanto, si existen 2 o más ladrones haciendo cola,
        este método solamente expulsará al primero que encuentre desde el
        frente.
        ATENCIÓN: con todo este desorden formado por la búsqueda del ladrón,
        ocurre que la cola de clientes original queda INVERTIDA.

        Retorna:
        ========
        True si el método encuentra un ladron formado en la cola de
        clientes. False en caso contrario, incluyendo cuando no hay clientes
        formados en la cola.
        """
        founded = False
        pila = Pila()
        while(not self.clientes.es_vacia()):
            cliente_actual = self.clientes.desencolar()
            if(cliente_actual.operacion=="X" and founded is False):
                founded=True
            else:
                pila.apilar(cliente_actual)
        while(not pila.es_vacia()):
            self.clientes.encolar(pila.desapilar(),1)
        return founded


    def escaneo(self):
        """
        Método que contabiliza el número de clientes que actualmente están
        realizando la cola del cajero, discriminados por Consignación, Retiro
        y Robo.

        Retorna:
        ========
        Una tupla con las cantidades de clientes discriminados así:

            (clientes_consignación, clientes_retiro, clientes_robo)
        """
        consignacion = 0
        retiro = 0
        robo = 0
        for x in self.clientes:
            if(x.operacion=='C'):
                consignacion+=1
            elif(x.operacion=='R'):
                retiro+=1
            elif(x.operacion=='X'):
                robo+=1
        return tuple([consignacion,retiro,robo])

    def info(self):
        """
        Método que genera un informe del estado actual de la cola de clientes
        del cajero del banco.

        Retorna:
        ========
        Una cadena con información de los clientes en la cola del cajero,
        presentado primero los que van a consignar, luego los que van a retirar
        y finalmente los que van a robar (separdos por una línea de caracteres
        especiales entre los clientes del mismo tipo de operación y entre
        clientes con diferente operación), en orden INVERSO a como serán
        atenidos, de la siguiente forma:

                    "N-O <num. oper>
                     Consignación $monto de la operación
                     +++++++++++++++++++++++++++++
                     N-O <num. oper>
                     Consignación $monto de la operación
                     +++++++++++++++++++++++++++++
                     N-O <num. oper>
                     Consignación $monto de la operación
                     .............................
                     N-O <num. oper>
                     Retiro $monto de la operación
                     -----------------------------
                     N-O <num. oper>
                     Retiro $monto de la operación
                     -----------------------------
                     N-O <num. oper>
                     Retiro $monto de la operación
                     .............................
                     N-O <num. oper>
                     Robo $monto de la operación
                     xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                     N-O <num. oper>
                     Robo $monto de la operación
                     xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                     N-O <num. oper>
                     Robo $monto de la operación"

        En caso de que no existan clientes en la cola del cajero se retornará
        una cadena vacía.
        """
        result = ''
        pila = Pila()
        for x in self.clientes:
            if(x.operacion=='X'):
                pila.apilar('\n')
                pila.apilar(str(x))
                pila.apilar('xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'+'\n')
        pila.desapilar()
        pila.apilar('.............................'+'\n')
        for x in self.clientes:
            if(x.operacion=='R'):
                pila.apilar('\n')
                pila.apilar(str(x))
                pila.apilar('-----------------------------'+'\n')
        pila.desapilar()
        pila.apilar('.............................'+'\n')
        for x in self.clientes:
            if(x.operacion=='C'):
                pila.apilar('\n')
                pila.apilar(str(x))
                pila.apilar('+++++++++++++++++++++++++++++'+'\n')
        pila.desapilar()
        while (not pila.es_vacia()):
            caracteres = pila.desapilar()
            if(not pila.es_vacia()):
                result+=caracteres
        if(len(result)>0):
            while (result[len(result)-1]=="\n" or result[len(result)-1]=="+" or result[len(result)-1]=="-" or result[len(result)-1]=="x"):
                result=result[0:len(result)-1]
        return result

    def __len__(self):
        """
        Método que devuelve el tamaño actual de la cola del Cajero.

        Retorna:
        ========
        El tamaño de la cola del Cajero.
        """
        return len(self.clientes)
