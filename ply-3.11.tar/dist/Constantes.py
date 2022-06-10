
class Constantes :
    def __init__(self):
        self.dicc = {}

    def add(self,num, posmem):
        if num in self.dicc.keys():
            print("Ya existe")
        else:
            self.dicc[num] = {
                "num" : num,
                "posmem" : posmem
            }


    def regresaMem(self, num):
        if num in self.dicc.keys():
            return self.dicc[num]["posmem"]
        else:
            print("No se encontro memoria de constante")


    def check(self, num):
        if num in self.dicc.keys():
            return True
        else:
            return False

    def print(self):
        for x in self.dicc.values():
            print(x)