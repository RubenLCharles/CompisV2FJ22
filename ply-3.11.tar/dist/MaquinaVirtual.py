from MemoriaVirt2 import *
from Constantes import * 
from parser import *
from cuadruplos import *


#Variables y funciones globales

memGlobal = Global()
memLocal = Local()

archivo = open("ply-3.11.tar\dist\generados.json",'r')
temps = archivo.read()
archivo.close()

cuadJson = json.loads(temps)

print("valor: " + str(cuadJson[0][0]))





#print [cuad[1]]
#
#def llenarConst():
#    x = len(consta)
#    i = 0

#    while (i < x):
#        num = consta[i]["num"]
#        posMem = consta[i]["posmem"]
#        memGlobal.storeGlobal(posMem,num)

#while (cuad[x] != "ENDOFPROGRAM"):
#    if cuad[x] == "+":
#        print ("x")
        

