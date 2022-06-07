#Lista de cuadruplos
cuad = []

class cuadruplos():

    #Agregamos cuadruplos
    def add(self, op, opnA, opnB, res):
        cuad.append([(op, opnA, opnB, res)])

    #Imprimimos cuadruplos
    def print(self):
        x = 0
        while x < len(cuad):
            print(cuad[x])
            x = x+1
    
    def len(self):
        return len(cuad)
    
    #Funcion para poder modificar valores de la lista
    def __getitem__(self, i):
        return f"Value {i}"
    
    #Funcion que modifica el gotof con la memoria y el resultado de a donde viene
    def modify1(self, place, memPas,result):
        cuad[place] = ('GOTOF',memPas,'',result)
    #Funcion que modifica el goto con la memoria y el resultado de a donde viene
    def modify2(self, place,result):
        cuad[place] = ('GOTO','','',result)
       