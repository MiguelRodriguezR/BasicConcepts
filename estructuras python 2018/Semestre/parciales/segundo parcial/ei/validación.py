class Validacion:
    def __init__(self):
        pass

    def homogeneidad(self, dato1, dato2):
        if(dato1 is None and dato2 is None):
            return True
        elif(dato1 is not None and isinstance(dato2, type(dato1))):
            return True
        return False
