from TVars import *

class TFunc:
    def __init__(self): self.dicc = {
        'global' : {
            'tipo':'void', 
            'nombre': 'global',
            'numParam':0, 
            'variables':TVars(), 
            'cantCuad':0 }
        }

    def agregarFunc(self, tipo, nombre, numParam, cantCuad):
        if nombre in self.dicc.keys():
            print("ya existe la funcion")
        else:
            self.dicc[nombre] = {
                "tipo" : tipo,
                "nombre" : nombre,
                "numParam" : numParam,
                "variables" : TVars(),
                "cantCuad" : cantCuad
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

    def listaTipos(self, nombre):
        return [self.dicc[nombre]['variables'].variable.dicc[i]['tipo'] for i in self.dicc[nombre]['variables'].dicc]

    def modificarVarsFunc(self, nombre, numParams):
         self.dicc[nombre]['numparams'] = numParams
    
    
