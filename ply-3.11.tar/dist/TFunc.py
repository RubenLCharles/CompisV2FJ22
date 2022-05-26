from TVars import *

class TFunc:
    def __init__(self): self.dicc = {}

    def agregarFunc(self, tipo, nombre, numParam):
        if nombre in self.dicc.keys():
            print("ya existe")
        else:
            self.dicc[nombre] = {
                "tipo" : tipo,
                "nombre" : nombre,
                "numParam" : numParam,
                "variables" : TVars()
            }

    def agregarVarFunc(self, nombre, tipo, posMem):
        if self.dicc[nombre]["variables"].agregarVar(nombre, tipo, posMem):
            print("Se agregó con éxito")
        else:
            print("Error: no se agregó")
            
    def mostrar(self, nombre):
        print(self.dicc[nombre]["variables"].dicc)

    def buscarMemPos(self, nombre, nom):
        if self.dicc[nombre]["variables"].check(nom):
            return self.dicc[nombre]["variables"].buscarposMem(nom)

        else:
            print("no existe variable")


    
