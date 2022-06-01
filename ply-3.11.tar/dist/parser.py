from asyncio import create_subprocess_exec
import ply.yacc as yacc
from lexer import tokens
import re
import os
from CuboSem import *
from cuadruplos import *
from TFunc import *

# PRECEDENCIA DE OPERADORES
precedencia = {
    ('nonassoc', 'SEMIC'),
    ('right', 'ASSIGN'),
    ('left', 'NE_LOG'),
    ('nonassoc', 'LT_LOG','LTE_LOG','GTE_LOG','GTE_LOG'),
    ('left', 'PLUS_OP','MINUS_OP'),
    ('left', 'MULT_OP', 'DIV_OP'),
    ('left', 'LPAREN','RPAREN'),
    ('left', 'LBRACK', 'RBRACK'),
    ('left', 'LCURLY', 'RCURLY')
}

# INICIO
def p_program(p):
    'program : PROGRAM ID SEMIC dec_var_gob def_funciones main'

# VARIABLES Y TIPOS
def p_dec_var_gob(p):
    '''
    dec_var_gob : VARS tipos COLON lista_ids SEMIC dec_var_aux
                | empty
    '''

def p_dec_var_aux(p):
    '''
    dec_var_aux : tipos COLON lista_ids SEMIC dec_var_aux
                | empty
    '''

def p_lista_ids(p):
    '''
    lista_ids : ID lista_aux lista_aux_b
    '''

def p_lista_aux(p):
    '''
    lista_aux : LBRACK INT_CTE RBRACK
              | empty
    ''' 

def p_lista_aux_b(p):
    '''
    lista_aux_b : COMMA lista_ids
                | empty
    '''

def p_tipos(p):
    '''
    tipos   : INT_CTE
            | FLOAT_CTE
            | CHAR_CTE
    '''

# DEFINICION DE FUNCIONES
def p_def_funciones(p):
    '''
    def_funciones : FUNCTION tipos_func ID LPAREN parametros RPAREN SEMIC dec_var_loc bloque
                  | empty
    '''

def p_tipos_func(p):
    '''
    tipos_func : INT_CTE
               | FLOAT_CTE
               | CHAR_CTE
               | VOID
    '''

def p_dec_var_loc(p):
    '''
    dec_var_loc : VARS tipos COLON ID dec_var_loc_aux SEMIC var_loc_rec
                | empty
    '''

def p_dec_var_loc_aux(p):
    '''
    dec_var_loc_aux : COMMA ID dec_var_loc_aux
                    | empty
    '''

def p_var_loc_rec(p):
    '''
    var_loc_rec : tipos COLON ID dec_var_loc_aux SEMIC var_loc_rec
                | empty
    '''

def p_parametros(p):
    '''
    parametros : tipos COLON ID param_aux
    '''

def p_param_aux(p):
    '''
    param_aux : COMMA parametros
              | empty
    '''

# ESTRUCTURA Y ESTATUTOS

def p_main(p):
    '''
    main : MAIN LPAREN RPAREN bloque
    '''

def p_bloque(p):
    '''
    bloque : LCURLY estatutos estatu_rec RCURLY
    '''

def p_estatu_rec(p):
    '''
    estatu_rec : estatutos estatu_rec
               | empty
    '''

def p_estatutos(p):
    '''
    estatutos : asignacion
              | llamada_func
              | llamada_void
              | retorno
              | lectura
              | escritura
              | decision
              | loop_cond
              | loop_no_cond 
              | expresiones
              | empty
    '''

def p_asignacion(p):
    '''
    asignacion : ID ASSIGN pn_secu1 expresiones pn_secu2
    '''

def p_llamada_func(p):
    '''
    llamada_func : ID LPAREN llamada_func_aux RPAREN SEMIC
    '''

def p_llamada_func_aux(p):
    '''
    llamada_func_aux : ID llama_func_auxb
                     | empty
    '''

def p_llama_func_auxb(p):
    '''
    llama_func_auxb : COMMA llamada_func_aux
                    | empty
    '''

def p_llamada_void(p):
    '''
    llamada_void : ID LPAREN llamada_void_aux RPAREN SEMIC
    '''

def p_llamada_void_aux(p):
    '''
    llamada_void_aux : ID llama_void_auxb
                     | empty
    '''

def p_llama_void_auxb(p):
    '''
    llama_void_auxb : COMMA llamada_func_aux
                    | empty
    '''

def p_retorno(p):
    '''
    retorno : RETURN  pn_secu3 LPAREN expresiones RPAREN pn_secu5 SEMIC
    '''

def p_lectura(p):
    '''
    lectura : READ pn_secu3 LPAREN ID lec_aux RPAREN SEMIC pn_secu4 pn_secu5
    '''

def p_lec_aux(p):
    '''
    lec_aux : COMMA ID lec_aux
            | empty
    '''

def p_escritura(p):
    '''
    escritura : WRITE pn_secu3 LPAREN esc_aux RPAREN SEMIC pn_secu5
    '''

def p_esc_aux(p):
    '''
    esc_aux : STRING_CTE pn_secu4 esc_rec
            | expresiones pn_secu4 esc_rec
            | empty
    '''

def p_esc_rec(p):
    '''
    esc_rec : COMMA esc_aux
            | empty
    '''

def p_decision(p):
    '''
    decision : IF LPAREN expresiones RPAREN pn_cond1 THEN bloque dec_aux
    '''

def p_dec_aux(p):
    '''
    dec_aux : else pn_cond2
            | empty
    '''

def p_else(p):
    '''
    else : ELSE pn_cond3 bloque
    '''

def p_loop_cond(p):
    '''
    loop_cond : WHILE pn_loop1 LPAREN expresiones RPAREN pn_loop2 DO bloque pn_loop3    
    '''

def p_loop_no_cond(p):
    '''
    loop_no_cond : FOR ID nocond_aux ASSIGN expresiones TO expresiones DO bloque
    '''

def p_nocond_aux(p):
    '''
    nocond_aux : LBRACK expresiones RBRACK
               | empty
    '''

# EXPRESIONES

def p_expresiones(p):
    '''
    expresiones : t_exp or_check
    '''

def p_or_check(p):
    '''
    or_check : OR_LOG pn_expresion9 expresiones pn_expresion10
             | empty
    '''

def p_t_exp(p):
    '''
    t_exp : g_exp and_check
    '''

def p_and_check(p):
    '''
    and_check : AND_LOG pn_expresion9 t_exp pn_expresion10
              | empty
    '''

def p_g_exp(p):
    '''
    g_exp : m_exp op_check
    '''

def p_op_check(p):
    '''
    op_check : empty
             | comparacion m_exp pn_expresion8
    '''

def p_comparacion(p):
    '''
    comparacion : GT_LOG pn_expresion7
                | LT_LOG pn_expresion7
                | EQUAL_LOG pn_expresion7
                | NE_LOG pn_expresion7
    '''

def p_m_exp(p):
    '''
    m_exp : termino pn_expresion3 m_rec
    '''

def p_m_rec(p):
    '''
    m_rec : PLUS_OP m_exp pn_expresion1
          | MINUS_OP m_exp pn_expresion1
          | empty
    '''

def p_termino(p):
    '''
    termino : factor pn_expresion4 term_rec
    '''

def p_term_rec(p):
    '''
    term_rec : MULT_OP pn_expresion2 termino
             | DIV_OP pn_expresion2 termino
             | empty
    '''

def p_factor(p):
    '''
    factor : LPAREN pn_expresiones5 expresiones RPAREN pn_expresiones6
           | INT_CTE
           | FLOAT_CTE
           | ID
           | llamada_func
    '''

# FUNCIONES ESPECIALES
def p_empty(p):
     'empty :'
     pass

# Globales y pilas
cuad = cuadruplos()
func = TFunc()
pOperad = []
pOperan = []
pTipos = []
pSaltos = []
temporal = []
currentfunc = 0



def p_pn_expresion1(p):
    '''
    pn_expresion1 : 
    '''
    global pOperad
    if p[-1] != '+' or p[-1] != '-':
        print("error")
    else:
        pOperad.append(p[-1])
    
    print(pOperad)

def p_pn_expresion2(p):
    '''
    pn_expresion2:
    '''
    global pOperad
    if p[-1] != '*' or p[-1] != '/':
        print("error")
    else:
        pOperad.append(p[-1])

def p_pn_expresion3(p):
    '''
    pn_expresion3 : 
    '''
    if pOperad.top() == '+' or pOperad.top() == '-':
        derOperan = pOperan.pop()
        derTipo = pTipos.pop()

        izqOperan = pOperan.pop()
        izqTipo = pTipos.pop()

        operador = pOperad.pop()

        resultado = CuboSem(izqTipo, derTipo, operador)

        if resultado == "error":
            print("Error de tipos")
        else:
            cuad = cuadruplos()

            cuad.add(operador, derOperan, izqOperan, temporal)
            pOperan.push(temporal)
            pTipos.push(resultado)

def p_pn_expresion4(p):
    '''
    pn_expresion4 : 
    '''
    if pOperad.top() == '*' or pOperad.top() == '/':
        derOperan = pOperan.pop()
        derTipo = pTipos.pop()

        izqOperan = pOperan.pop()
        izqTipo = pTipos.pop()

        operador = pOperad.pop()

        resultado = CuboSem(izqTipo, derTipo, operador)

        if resultado == "error":
            print("Error de tipos")
        else:
            cuad = cuadruplos()

            cuad.add(operador, derOperan, izqOperan, temporal)
            pOperan.push(temporal)
            pTipos.push(resultado)

def p_pn_expresion5(p):
    '''
    pn_expresion5 :
    '''
    global pOperad
    pOperad.push('(')

def p_pn_expresion6(p):
    '''
    pn_expresion6 :
    '''
    pOperad.pop()

def p_pn_expresion7(p):
    '''
    pn_expresion7 :

    '''
    if p[-1] != '>' or p[-1] != '<' or p[-1] != '<=' or p[-1] != '>=':
        print("error")
    else:
        pOperad.append(p[-1])

def p_pn_expresion8(p):
    '''
    pn_expresion8 :

    '''
    if pOperad.top() == '>' or pOperad.top() == '<' or pOperad.top() == '<=' or pOperad.top() == '>=':
        derOperan = pOperan.pop()
        derTipo = pTipos.pop()

        izqOperan = pOperan.pop()
        izqTipo = pTipos.pop()

        operador = pOperad.pop()

        resultado = CuboSem(izqTipo, derTipo, operador)

        if resultado == "error":
            print("Error de tipos")
        else:
            cuad = cuadruplos()

            cuad.add(operador, derOperan, izqOperan, temporal)
            pOperan.push(temporal)
            pTipos.push(resultado)

def p_pn_expresion9(p) :
    '''
    pn_expresion9 :
    '''
    if p[-1] != '&&' or p[-1] != '||':
        print("error")
    else:
        pOperad.append(p[-1])

def p_pn_expresion10(p) :
    '''
    pn_expresion10 :
    '''
    if pOperad.top() == '&&' or pOperad.top() == '||':
        derOperan = pOperan.pop()
        derTipo = pTipos.pop()

        izqOperan = pOperan.pop()
        izqTipo = pTipos.pop()

        operador = pOperad.pop()

        resultado = CuboSem(izqTipo, derTipo, operador)

        if resultado == "error":
            print("Error de tipos")
        else:
            cuad = cuadruplos()

            cuad.add(operador, derOperan, izqOperan, temporal)
            pOperan.push(temporal)
            pTipos.push(resultado)

'''
Secuenciales
'''

def p_pn_secu1(p) :
    '''
    pn_secu1 :
    '''
    if p[-1] != '=':
        print("error")
    else:
        pOperad.append(p[-1])

def p_pn_secu2(p) :
    '''
    pn_secu2 :
    '''
    if pOperad.top() == '=' :
        derOperan = pOperan.pop()
        derTipo = pTipos.pop()

        izqOperan = pOperan.pop()
        izqTipo = pTipos.pop()

        operador = pOperad.pop()

        resultado = CuboSem(izqTipo, derTipo, operador)

        if resultado == "error":
            print("Error de tipos")
        else:
            cuad = cuadruplos()

            cuad.add(operador, izqOperan,'' , derOperan)
            pOperan.push(temporal)
            pTipos.push(resultado)

def p_pn_secu3(p):
    '''
    pn_secu3 :
    '''
    if p[-1] != 'read' or p[-1] != 'write' or p[-1] != 'return':
        print("error")
    else:
        pOperad.append(p[-1])

def p_pn_secu4(p): 
    '''
    pn_secu4 :
    '''
    if pOperad.top() == 'read' or pOperad.top() == 'write' or pOperad.top() == 'return':
        operador = pOperad.pop()
     
        operando = pOperan.pop()
        cuad = cuadruplos()
        cuad.add(operador, operando,'' , '')
        

def p_pn_secu5(p):
    '''
    pn_secu5 :
    '''
    pOperad.pop()

def p_pn_secu6(p):
    '''
    pn_secu6 : 
    '''
    operador = pOperad.pop()
    operando = pOperan.pop()
    tipo = pTipos.pop()
    cuad = cuadruplos()
    cuad.add(operador, '','' , operando)

def p_pn_cond1(p):
    '''
    pn_cond1 :
    '''
    cuadruplos
    tipo = pTipos.pop()
    if tipo != "error" :
        resultado = pOperan.pop()
        cuad = cuadruplos
        cuad.add('GOTOF',resultado,'','')
        pSaltos.append(len(cuad))

def p_pn_cond2(p):
    '''
    pn_cond2 :
    '''
    ultimo = pSaltos.pop()
    cuadFill = (cuad[ultimo][0], cuad[ultimo][1],cuad[ultimo][2], len(cuad))
    cuad[ultimo] = cuadFill

def p_pn_cond3(p):
    '''
    pn_cond3 :
    '''
    cuad.append('GOTO','','','')
    falso = pSaltos.pop()
    pSaltos.append(len(cuad)-1)
    cuadFill = (cuad[falso][0], cuad[falso][1],cuad[falso][2], len(cuad))
    cuad[falso] = cuadFill

def p_pn_loop1(p):
    '''
    pn_loop1 :
    '''
    pSaltos.append(len(cuad))

def p_pn_loop2(p):
    '''
    pn_loop2 :
    '''
    tipo = pTipos.pop()
    if tipo != "bool":
        print("Error")
    else: 
        resultado = pOperan.pop()
        cuad.add('GOTOF', resultado, '', '')
        pSaltos.append(len(cuad)-1)

def p_pn_loop3(p):
    '''
    pn_loop3 :
    '''
    ultimo = pSaltos.pop()
    retorna = pSaltos.pop()
    cuad.add('GOTO', '', '', retorna)

    cuadFill = (cuad[ultimo][0], cuad[ultimo][1],cuad[ultimo][2], len(cuad))
    cuad[ultimo] = cuadFill

#Agregar Funcion
def p_pn_func1(p):
    '''
    pn_func1 :
    '''


parser = yacc.yacc()
res = parser.parse("program PRUEBA; main () { cont = 2 + 3 * 8 * ( 2 + 4 ) }")

#program PRUEBA; main () { cont = 2 + 3 * 8 * ( 2 + 4 ) }