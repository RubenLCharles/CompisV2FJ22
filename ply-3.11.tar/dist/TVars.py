class TVars :
    #Iniciamos diccionario de variables
    def __init__(self):
        self.dicc = {}

    #regresamos el nombre si esta en el diccionario
    def check(self, nombre):
        return nombre in self.dicc.keys()

    #Agregamos una variable con su memoria, tipo y nombre al diccionario
    def agregarVar(self, nombre, tipo, posMem):
        if nombre in self.dicc.keys():
            print("Variable ya existe")
        else:
            self.dicc[nombre] = {
                "nombre" : nombre,
                "tipo" : tipo,
                "posMem" : posMem
            }
        return True

    #Busca una variable en el diccionario
    def buscarVar(self, nombre):
        if nombre in self.dicc.keys():
            return self.dicc[nombre]
        else:
            print("No existe")

    #Busca una tipo en el diccionario
    def buscarTipo(self, nombre):
        if nombre in self.dicc.keys():
            return self.dicc[nombre]["tipo"]
        else:
            print("No existe")

    #Busca la memoria de una variable
    def buscarposMem(self, nombre):
        if nombre in self.dicc.keys():
            return self.dicc[nombre]["posMem"]
        else:
            print("No existe")
