from abc import ABCMeta, abstractmethod


class ListaDEA(metaclass=ABCMeta):  # class abstracta

    @abstractmethod
    def adicionar(self, nuevo_dato):
        raise NotImplementedError("implementar el metodo adicionar")

    @abstractmethod
    def borrar(self, dato_eliminar):
        raise NotImplementedError("implementar el meto a eliminar")

    @abstractmethod
    def recorrer_atras(self):
        raise NotImplementedError("implementar el metodon recorrer_atras")

    @abstractmethod
    def adelante(self):
        raise NotImplementedError("implementar el metodo adelante")
        """" metodo que avanza"del primero al ultimo" uno
         a uno sobre los elementos de la lista y los va devolviendo
          (dato) en cada una
         de las llamadas al metodo
        """
    @abstractmethod
    def atras(self):
        raise NotImplementedError("implementar el metodo atras")
        """"metodo que avanza"del ultimo al primero" uno
         a uno sobre los elementos de la lista y los va devolviendo
         (dato) en cada una
         de las llamadas al metodo
        """
