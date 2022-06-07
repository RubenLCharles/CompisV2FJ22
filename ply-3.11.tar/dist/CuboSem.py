#Funcion que revisa dos tipos de operandos con un operador, los compara y si esta dentro de las asignaciones verdaderas regresara el valor correcto.
def CuboSem(operand1,operand2,operator):
    if operand1 == "entero":
        if operand2 == "entero":
            if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "=":
                return "entero"
            elif operator == "==" or operator == ">" or operator == "<" or operator == "<=" or operator == ">=" or operator == "!=":
                return "bool"

        elif operand2 == "float":
            if operator == "+" or operator == "-" or operator == "*" or operator == "/":
                return "float"
            elif operator == "=":
                return "entero"
            elif operator == "==" or operator == "<" or operator == ">" or operator == "<=" or operator  == ">=" or operator == "!=":
                return "bool"
    
        elif operand2 == "string":
            if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "="  or operator == ">" or operator == "<" or operator == "<=" or operator == ">=" or operator == "!=":
                return "error"
            elif operator == "==":
                return "bool"

    elif operand1 == "float":
        if operand2 == "entero":
            if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "=":
                return "float"
            elif operator == "==" or operator == ">" or operator == "<" or operator == "<=" or operator == ">=" or operator == "!=":
                return "bool"
        elif operand2 == "float":
            if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "=":
                return "float"
            elif operator == "==" or operator == ">" or operator == "<" or operator == "<=" or operator == ">=" or operator == "!=":
                return "bool"
        elif operand2 == "string":
            if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "="  or operator == "==" or operator == ">" or operator == "<" or operator == "<=" or operator == ">=" or operator == "!=":
                return "error"
                
    elif operand1 == "string":
        if operand2 == "entero":
             if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "="  or operator == "==" or operator == ">" or operator == "<" or operator == "<=" or operator == ">=" or operator == "!=":
                return "error"
        if operand2 == "float":
             if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "="  or operator == "==" or operator == ">" or operator == "<" or operator == "<=" or operator == ">=" or operator == "!=":
                return "error"
        if operand2 == "string":
            if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "="  or operator == "==" or operator == ">" or operator == "<" or operator == "<=" or operator == ">=" or operator == "!=":
                return "error"