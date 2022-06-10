from audioop import add
from MemVirtual import *



class Global: 
    def __init__(self):
        self.varGBL = [[],[],[]]
        self.cteGBL = [[],[],[]]
    
    def fetchGlobal(self, address):
        try:
            if (address >= 0 and address < 500):
                return self.varGBL[address]
            elif (address >= 500 and address < 1000):
                return self.varGBL[address-500]
            elif (address >= 1000 and address < 1500):
                return self.varGBL[address-1000]
            elif (address >= 5000 and address < 5500):
                return self.cteGBL[address-5000]
            elif (address >= 5500 and address < 6000):
                return self.varGBL[address-5500]
            elif (address >= 6000 and address < 6500):
                return self.varGBL[address-6000]
        except:
            print("Error, variable no existe o no ha sido asignada un valor")
            exit()

    def storeGlobal(self,address,valor):
        offset = 0
        try:
            if (address >= 0 and address < 500):
                offset = address-500
                if offset < len(self.varGBL[0]):
                    self.varGBL[0][offset] = valor
                else:
                    self.varGBL[0][offset].append(valor)
            elif (address >= 500 and address < 1000):
                offset = address-1000
                if offset < len(self.varGBL[1]):
                    self.varGBL[1][offset] = valor
                else:
                    self.varGBL[1][offset].append(valor)
            elif (address >= 1000 and address < 1500):
                offset = address-1500
                if offset < len(self.varGBL[2]):
                    self.varGBL[2][offset] = valor
                else:
                    self.varGBL[2][offset].append(valor)
            elif (address >= 5000 and address < 5500):
                offset = address-5000
                self.cteGBL[0][offset].append(valor)
            elif (address >= 5500 and address < 6000):
                offset = address-5500
                self.cteGBL[1][offset].append(valor)
            elif (address >= 6000 and address < 6500):
                offset = address-6000
                self.cteGBL[2][offset].append(valor)
        except:
            print("Error, variable no existe o no ha sido asignada un valor")
            exit()


class Local:
    def __init__(self):
        self.varLC = [[],[],[]]
        self.temp = [[],[],[],[]]

    def fetchLocal(self, address):
        try:
            if (address >= 1500 and address < 2000):
                return self.varGBL[address-1500]
            elif (address >= 2000 and address < 2500):
                return self.varGBL[address-2000]
            elif (address >= 2500 and address < 3000):
                return self.varGBL[address-2500]
            elif (address >= 3000 and address < 3500):
                return self.cteGBL[address-3000]
            elif (address >= 3500 and address < 4000):
                return self.varGBL[address-3500]
            elif (address >= 4000 and address < 4500):
                return self.varGBL[address-4000]
            elif (address >= 4500 and address < 5000):
                return self.varGBL[address-4500]
        except:
            print("Error, variable no existe o no ha sido asignada un valor")
            exit()

    def storeLocal(self, address, valor):
        offset = 0
        try:
            if (address >= 1500 and address < 2000):
                offset = address-1500
                if offset < len(self.varLC[0]):
                    self.varLC[0][offset] = valor
                else:
                    self.varLC[0][offset].append(valor)
            elif (address >= 2000 and address < 2500):
                offset = address-2000
                if offset < len(self.varLC[1]):
                    self.varLC[1][offset] = valor
                else:
                    self.varLC[1][offset].append(valor)
            elif (address >= 2500 and address < 3000):
                offset = address-2500
                if offset < len(self.varLC[2]):
                    self.varLC[2][offset] = valor
                else:
                    self.varLC[2][offset].append(valor)
            elif (address >= 3000 and address < 3500):
                offset = address-3000
                if offset < len(self.temp[0]):
                    self.temp[0][offset] = valor
                else:
                    self.temp[0][offset].append(valor)
            elif (address >= 3500 and address < 4000):
                offset = address-3500
                if offset < len(self.temp[1]):
                    self.temp[1][offset] = valor
                else:
                    self.temp[1][offset].append(valor)
            elif (address >= 3500 and address < 4000):
                offset = address-3500
                if offset < len(self.temp[2]):
                    self.temp[2][offset] = valor
                else:
                    self.temp[2][offset].append(valor)
            elif (address >= 4000 and address < 4500):
                offset = address-4000
                if offset < len(self.temp[3]):
                    self.temp[3][offset] = valor
                else:
                    self.temp[3][offset].append(valor)
        except:
            print ("Error")
            exit()