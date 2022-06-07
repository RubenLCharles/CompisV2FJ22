cuad = []

class cuadruplos():

    def add(self, op, opnA, opnB, res):
        cuad.append([(op, opnA, opnB, res)])

    def print(self):
        x = 0
        while x < len(cuad):
            print(cuad[x])
            x = x+1
    
    def len(self):
        return len(cuad)
    
    def __getitem__(self, i):
        return f"Value {i}"
    
    def modify1(self, place, memPas,result):
        cuad[place] = ('GOTOF',memPas,'',result)
    
    def modify2(self, place,result):
        cuad[place] = ('GOTO','','',result)
       