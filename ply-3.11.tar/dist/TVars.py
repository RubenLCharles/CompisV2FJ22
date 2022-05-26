class TVars :
    def __init__(self): self.dicc = {}


    def check(self, nombre):
        return nombre in self.dicc.keys()

    def agregarVar(self, nombre, tipo, posMem):
        if nombre in self.dicc.keys():
            print("Variable ya existe")
        else:
            self.dicc[nombre] = {
                "nombre" : nombre,
                "tipo" : tipo,
                "posMem" : posMem
            }
    
    def buscarVar(self, nombre):
        if nombre in self.dicc.keys():
            return self.dicc[nombre]
        else:
            print("No existe")

    def buscarTipo(self, nombre):
        if nombre in self.dicc.keys():
            return self.dicc[nombre]["tipo"]
        else:
            print("No existe")

    def buscarposMem(self, nombre):
        if nombre in self.dicc.keys():
            return self.dicc[nombre]["posMem"]
        else:
            print("No existe")
