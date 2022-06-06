cuad = []

class cuadruplos():

    def add(self, op, opnA, opnB, res):
        cuad.append([(op, opnA, opnB, res)])

    def print(self):
        x = 0
        while x < len(cuad):
            print(cuad[x])
            x = x+1
        