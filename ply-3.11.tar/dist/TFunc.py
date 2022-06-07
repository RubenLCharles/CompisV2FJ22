#Importamos tabla de variable para que cada funcion tenga su propia tabla de variables
from TVars import *

#Clase de tabla de funciones
class TFunc:
    #Iniciamos el diccionario
    def __init__(self): self.dicc = {
        'global' : {
            'tipo':'void', 
            'nombre': 'global',
            'numParam':0, 
            'variables':TVars(), 
            'cantCuad':0 }
        }
    #Agregamos una funcion a la tabla de funciones
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

    #Agregamos una variable a la funcion
    def agregarVarFunc(self, nombre, tipo, posMem):
        if self.dicc[nombre]["variables"].agregarVar(nombre, tipo, posMem):
            print("Se agregó con éxito")
        else:
            print("Error: no se agregó")

    #Mostramos la las variables de una funcion    
    def mostrar(self, nombre):
        print(self.dicc[nombre]["variables"].dicc)

    #Buscamos la memoria de una variable de la funcion
    def buscarMemPos(self, nombre, nom):
        if self.dicc[nombre]["variables"].check(nom):
            return self.dicc[nombre]["variables"].buscarposMem(nom)

        else:
            print("no existe variable")

    #Modifica el numero de parametros de una funcion
    def modificarVarsFunc(self, nombre, numParams):
         self.dicc[nombre]['numparams'] = numParams
    
    
