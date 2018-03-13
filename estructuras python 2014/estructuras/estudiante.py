class Estudiante:
    def __init__(self,codigo,nombre=None,nota=None):
        self.codigo=codigo
        self.nombre=nombre
        self.nota=nota
        #el dato a buscar no solamente va a ser de codigo sino de estudiantes
        
    def __str__(self):
        return(str(self.codigo)+" "+str(self.nombre)+" "+str(self.nota))
    
"""
            ctrl+alt+f2
            login:root
            password:fi2013b
"""