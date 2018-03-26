class Objeto1():
    """docstring for objeto1"""
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return("Clase Objeto1..."+str(self.num))

class Objeto2():
    """docstring for objeto2"""
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return("Clase Objeto2..."+str(self.num))

class ObjetoPrioridad():
    def __init__(self, num,prioridad):
        self.num = num
        self.prioridad = prioridad

    def __str__(self):
        return("Clase ObjetoPrioridad...<Num:"+str(self.num)+",Prior:"+str(self.prioridad)+">")
