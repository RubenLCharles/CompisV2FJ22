#Diccionarios e imports usados en el proyecto
from asyncio import create_subprocess_exec
import json
import ply.yacc as yacc
from lexer import tokens
import re
import os
from CuboSem import *
from cuadruplos import *
from TFunc import *
from MemVirtual import *
from Constantes import *
from MaquinaVirtual import *
import ast

# Globales y pilas
cuad = cuadruplos()
dirFunc = TFunc()
consta = Constantes()
pOperad = []
pOperan = []
pTipos = []
pSaltos = []
pFunc = []
temporal = []
pMemoria = []
cteInt = []
cteFlt = []
cteStr = []
pMemMod = []
espMem = 500
cuadJump = []
nombFunc = "global"
nombVar = ""
tipoAct = ""   
tipoActVar = ""         #Tipo de la Variable
voidBool = False
numVars = 0
numParams = 0
contArg = 0
TVARS = TVars()
MemVirtual = MemVirtual()


# INICIO
def p_program(p):
    'program : PROGRAM ID pn_GotoMain SEMIC dec_var_gob def_funciones main pn_final pn_print '

# VARIABLES Y TIPOS
def p_dec_var_gob(p):
    '''
    dec_var_gob : VARS tipos COLON lista_ids dec_var_aux
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
    tipos   : INT_TYPE pn_tipoAct
            | FLOAT_TYPE pn_tipoAct
            | CHAR_TYPE pn_tipoAct
    '''

# DEFINICION DE FUNCIONES
def p_def_funciones(p):
    '''
    def_funciones : FUNCTION tipos_func ID pn_func1 LPAREN parametros RPAREN pn_func3 SEMIC dec_var_loc bloque pn_func4
                  | empty
    '''

def p_tipos_func(p):
    '''
    tipos_func : INT_TYPE pn_tipoAct
               | VOID pn_tipoAct
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
    parametros : tipos COLON ID pn_func2 param_aux
    '''

def p_param_aux(p):
    '''
    param_aux : COMMA parametros
              | empty
    '''

# ESTRUCTURA Y ESTATUTOS

def p_main(p):
    '''
    main : MAIN LPAREN RPAREN pn_FillMain pn_cambioCtxt bloque
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
              | declaracion
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
    asignacion : ID pn_expresionID2 ASSIGN pn_secu1 expresiones pn_secu2 SEMIC
    '''

def p_declaracion(p):
    '''
    declaracion : tipos ID pn_expresionID declaracion_aux SEMIC
    '''

def p_declaracion_aux(p):
    '''
    declaracion_aux : ASSIGN pn_secu1 expresiones pn_secu2
                    | empty
    '''

def p_llamada_func(p):
    '''
    llamada_func : LLAMA ID pn_llamFunc1 LPAREN pn_expresion5 llamada_func_aux RPAREN pn_expresion6 pn_llamFunc3 SEMIC
    '''

def p_llamada_func_aux(p):
    '''
    llamada_func_aux : expresiones pn_llamFunc2 llama_func_auxb
                     | empty
    '''

def p_llama_func_auxb(p):
    '''
    llama_func_auxb : COMMA llamada_func_aux
                    | empty
    '''

def p_llamada_void(p):
    '''
    llamada_void : LLAMA ID pn_llamFunc1 LPAREN llamada_void_aux RPAREN pn_llamFunc3 SEMIC
    '''

def p_llamada_void_aux(p):
    '''
    llamada_void_aux : expresiones pn_llamFunc2 llama_void_auxb
                     | empty
    '''

def p_llama_void_auxb(p):
    '''
    llama_void_auxb : COMMA llamada_func_aux
                    | empty
    '''

def p_retorno(p):
    '''
    retorno : RETURN  pn_secu3 LPAREN expresiones RPAREN SEMIC
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
    escritura : WRITE LPAREN  RPAREN pn_secuPR2 SEMIC 
    '''

def p_decision(p):
    '''
    decision : IF LPAREN expresiones RPAREN pn_cond1 THEN bloque else pn_cond2
    '''

def p_else(p):
    '''
    else : ELSE pn_cond3 bloque
         | empty
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
    m_rec : PLUS_OP pn_expresion1 m_exp 
          | MINUS_OP pn_expresion1 m_exp 
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
    factor : llamada_func
           | LPAREN pn_expresion5 expresiones RPAREN pn_expresion6
           | cte
           | ID pn_busqueda
    '''
def p_cte(p):
    '''
    cte     : INT_CTE pn_constante
           | FLOAT_CTE pn_constante
    '''

# FUNCIONES ESPECIALES
def p_empty(p):
     'empty :'
     pass

#Funcion para cambiar de contexto global a local y que la memoria se cambie
def p_pn_cambioCtxt(p):
    '''
    pn_cambioCtxt : 
    '''
    global nombFunc
    nombFunc = "local"

#Buscamos en memoria el tipo de variable que es una variable y agregamos a la tablad e variables
def p_pn_expresionID(p):
    '''
    pn_expresionID :
    '''
    global nombFunc
    global tipoAct
    nombre = p[-1]
    pMemoria.append(MemVirtual.memoria(tipoAct, nombFunc))
    pOperan.append(p[-1])
    pm = pMemoria.pop()
    TVARS.agregarVar(nombre, tipoAct,pm)
    pMemoria.append(pm)
    
#Busqueda de tipo en la tabla de variables
def p_pn_busqueda(p):
    '''
    pn_busqueda :
    '''
    global nombFunc
    global tipoAct
    nombre = p[-1]
    tipo = TVARS.buscarTipo(nombre)
    pMemoria.append(TVARS.buscarposMem(nombre))
    pOperan.append(p[-1])
    pTipos.append(tipo)

#funcion para una variable ya declarada que quiere tener una asignación nueva
def p_pn_expresionID2(p):
    '''
    pn_expresionID2 :
    '''
    global nombFunc
    global tipoAct
    nombre = p[-1]
    tipo = TVARS.buscarTipo(nombre)


    pMemoria.append(TVARS.buscarposMem(nombre))
    pOperan.append(p[-1])
    pTipos.append(tipo)

#Funciones para manejo de expresiones
def p_pn_expresion1(p):
    '''
    pn_expresion1 : 
    '''
    global pOperad
    if p[-1] != '+' and p[-1] != '-':
        print("error2")
    else:
        pOperad.append(p[-1])
    
def p_pn_secuPR2(p):
    '''
    pn_secuPR2 :
    '''
    resPR = pMemoria.pop()
    pTipos.pop()
    cuad.add("PRINT", resPR, '', '')

def p_pn_expresion2(p):
    '''
    pn_expresion2 :
    '''
    global pOperad
    if p[-1] != '*' and p[-1] != '/':
        print("error")
    else:
        pOperad.append(p[-1])

def p_pn_expresion3(p):
    '''
    pn_expresion3 : 
    '''
    global cuad
    if len(pOperad)-1 > 0:
        temp = pOperad[len(pOperad)-1]
        if temp == '+' or temp == '-':
            derOperan = pOperan.pop()
            derTipo = pTipos.pop()
            derMemoria = pMemoria.pop()

            izqOperan = pOperan.pop()
            izqTipo = pTipos.pop()
            izqMemoria = pMemoria.pop()

            operador = pOperad.pop()

            resultado = CuboSem(izqTipo, derTipo, operador)
            tempRes =  MemVirtual.temporales(resultado)

            if resultado == "error":
                print("Error de tipos")
            else:

                cuad.add(operador, izqMemoria, derMemoria, tempRes)
                pOperan.append(tempRes)
                pMemoria.append(tempRes)
                pTipos.append(resultado)

def p_pn_expresion4(p):
    '''
    pn_expresion4 : 
    '''
    if len(pOperad)-1 > 0:

        temp = pOperad[len(pOperad)-1]
        if temp == '*' or temp == '/':
            
            derOperan = pOperan.pop()
            derTipo = pTipos.pop()
            derMemoria = pMemoria.pop()

            izqOperan = pOperan.pop()
            izqTipo = pTipos.pop()
            izqMemoria = pMemoria.pop()

            operador = pOperad.pop()

            resultado = CuboSem(izqTipo, derTipo, operador)
            print(resultado)
            tempRes =  MemVirtual.temporales(resultado)

            if resultado == "error":
                print("Error de tipos")
            else:
                cuad.add(operador, izqMemoria, derMemoria, tempRes)
                pOperan.append(tempRes)
                pMemoria.append(tempRes)
                pTipos.append(resultado)

def p_pn_expresion5(p):
    '''
    pn_expresion5 :
    '''
    global pOperad
    pOperad.append('(')

def p_pn_expresion6(p):
    '''
    pn_expresion6 :
    '''
    pOperad.pop()
    

def p_pn_expresion7(p):
    '''
    pn_expresion7 :

    '''
    if p[-1] != '>' and p[-1] != '<' and p[-1] != '<=' and p[-1] != '>=' and p[-1] != '==':
        print("error")
    else:
        pOperad.append(p[-1])

def p_pn_expresion8(p):
    '''
    pn_expresion8 :

    '''
    
    temp = pOperad[len(pOperad)-1]
    if temp == '>' or temp == '<' or temp == '<=' or temp == '>=' or temp == '==':
        derOperan = pOperan.pop()
        derTipo = pTipos.pop()
        derMemoria = pMemoria.pop()

        izqOperan = pOperan.pop()
        izqTipo = pTipos.pop()
        izqMemoria = pMemoria.pop()

        operador = pOperad.pop()

        resultado = CuboSem(izqTipo, derTipo, operador)
        tempRes =  MemVirtual.temporales(resultado)
        if resultado == "error":
            print("Error de tipos")
        else:

            cuad.add(operador, izqMemoria, derMemoria, tempRes)
            pOperan.append(tempRes)
            pTipos.append(resultado)
            pMemoria.append(tempRes)

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
        derMemoria = pMemoria.pop()

        izqOperan = pOperan.pop()
        izqTipo = pTipos.pop()
        izqMemoria = pMemoria.pop()

        operador = pOperad.pop()

        resultado = CuboSem(izqTipo, derTipo, operador)
        tempRes =  MemVirtual.temporales(resultado)
        if resultado == "error":
            print("Error de tipos")
        else:
            cuad.add(operador, izqMemoria, derMemoria, tempRes)
            pOperan.append(tempRes)
            pTipos.append(resultado)
            pMemoria.append(tempRes)

'''
Secuenciales
'''

#Funciones para secuenciales 
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
    global cuad

    temp = pOperad[len(pOperad)-1]
    if temp == '=' :
        derOperan = pOperan.pop()
        derTipo = pTipos.pop()
        derMemoria = pMemoria.pop()

        izqOperan = pOperan.pop()
        izqMemoria = pMemoria.pop()
        if not pTipos :
            pTipos.append(MemVirtual.getMem(izqMemoria)) 
        
        izqTipo = pTipos.pop()
        operador = pOperad.pop()

        resultado = CuboSem(izqTipo, derTipo, operador)   

        if resultado == "error":
            print("Error de tipos")
        else:

            cuad.add(operador, derMemoria, '' , izqMemoria)
            #pOperan.append(MemVirtual.temporales(resultado))
            #pTipos.append(resultado)

def p_pn_secu3(p):
    '''
    pn_secu3 :
    '''
    if p[-1] != 'read'  and p[-1] != 'return':
        print("error")
    else:
        pOperad.append(p[-1])

def p_pn_secu4(p): 
    '''
    pn_secu4 :
    '''
    temp = pOperad.pop()
    if temp == 'read'  or temp == 'return':
        pOperad.append(temp)
        operador = pOperad.pop()
        operando = pOperan.pop()
        memoria = pMemoria.pop()

        cuad.add(operador, memoria,'' , '')

def p_pn_secuPR(p): 
    '''
    pn_secuPR :
    '''
    cuad.add("PRINT","",'' , '')

def p_pn_secu5(p):
    '''
    pn_secu5 :
    '''
    pOperad.pop()


#Puntos Neuralgicos para un IF 
def p_pn_cond1(p):
    '''
    pn_cond1 :
    '''
    tipo = pTipos.pop()
    if tipo != "error" :
        resultado = pOperan.pop()
       
        cuad.add('GOTOF',resultado,'','')
        pSaltos.append(cuad.len()-1)
        pMemMod.append(resultado)

def p_pn_cond2(p):
    '''
    pn_cond2 :
    '''
    global cuad
   
    falso = pSaltos.pop()
    cuad.modify2(falso,cuad.len())
    


def p_pn_cond3(p):
    '''
    pn_cond3 :
    '''
    global cuad
    cuad.add('GOTO','','','')
    ultimo = pSaltos.pop()
    cuad.modify1(ultimo,pMemMod.pop(),cuad.len())
    pSaltos.append(cuad.len()-1)
    


#Puntos Neuralgicos para un WHILE
def p_pn_loop1(p):
    '''
    pn_loop1 :
    '''
    pSaltos.append(cuad.len())

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
        pSaltos.append(cuad.len()-1)
        pMemMod.append(resultado)

def p_pn_loop3(p):
    '''
    pn_loop3 :
    '''
    ultimo = pSaltos.pop()
    retorna = pSaltos.pop()
    cuad.add('GOTO', '', '', retorna)
    cuad.modify1(ultimo,pMemMod.pop(),cuad.len())


#Regresa el tipo actual(ultimo elemento)
def p_pn_tipoAct(p):
    '''
    pn_tipoAct : 
    '''
    global tipoAct
    tipoAct = p[-1]
    pTipos.append(tipoAct)


#Puntos Neuralgicos para creacion funciones 
def p_pn_parametrosTipo(p):
    '''
    pn_parametrosTipo : 
    '''
    global tipoActVar
    tipoActVar = p[-1]

def p_pn_func1(p):
    '''
    pn_func1 :
    '''
    global nombFunc
    global voidBool
    nombFunc = p[-1]
    numParams = 0

    dirFunc.agregarFunc(tipoAct, nombFunc, numParams, cuad.len())

    if dirFunc.dicc[nombFunc]["tipo"] == "void":
        voidBool = True
    else :
        voidBool = False

def p_pn_func2(p):
    '''
    pn_func2 :
    '''
    global numParams
    global numVars

    nombVar = p[-1]
    numParams = numParams+1
    numVars = numVars+1
    posMem = MemVirtual.memoria(tipoAct, nombFunc)
    dirFunc.agregarVarFunc(nombFunc, nombVar, posMem)

def p_pn_func3(p):
    '''
    pn_func3 : 
    '''
    dirFunc.modificarVarsFunc(nombFunc,numParams)

def p_pn_func4(p):
    '''
    pn_func4 : 
    '''
    MemVirtual.eliminar()
    cuad.add("ENDFUNC",'','','')


#Puntos Neuralgicos para las llamadas de funciones
def p_pn_llamFunc1(p):
    '''
    pn_llamFunc1 :
    '''
    nomb = p[-1]

    if nomb in dirFunc.dicc:
        pFunc.append(nomb)
        cuad.add("ERA",nomb,'','')

def p_pn_llamFunc2(p):
    '''
    pn_llamFunc2 :
    '''
    global contArg
    pOperan.pop()
    pTipos.pop()
    #pFunc.pop()
    argMem = pMemoria.pop()
    contArg += 1

    cuad.add("PARAM", argMem,"",contArg)

def p_pn_llamFunc3(p):
    '''
    pn_llamFunc3 :
    '''
    nomFunc = pFunc.pop()
    cantCuad = dirFunc.dicc[nomFunc]['cantCuad']

    cuad.add("GOSUB",nomFunc,cuad.len()+1, cantCuad)
    tipoFunc = dirFunc.dicc[nomFunc]['tipo']

    if tipoFunc != "void":
        cuad.add("=",nomFunc,"",MemVirtual.temporales(tipoFunc))
        pOperan.append(MemVirtual.temporales(tipoFunc)) #cambio
        pMemoria.append(MemVirtual.temporales(tipoFunc))
        pTipos.append(tipoFunc)

#Punto Neuralgico para que se genere cuadruplo de gotomain
def p_pn_GotoMain(p):
    '''
    pn_GotoMain :
    '''
    cuad.add("GOTO",'','','')

def p_pn_FillMain(p):
    '''
    pn_FillMain :
    '''
    cuad.modify3(cuad.len())

#Punto Neuralgico que se encarga de las constantes
def p_pn_constante(p):
    '''
    pn_constante :
    '''
    global iniIntCNS
    global iniFltCNS
    global iniStrCNS

    if type(p[-1]) == int :
        if not consta.check(p[-1]) :
            if iniIntCNS < limIntCNS :
                cteInt.append(p[-1])
                consta.add(p[-1],iniIntCNS)
                iniIntCNS += 1
            else :
                print("Error: ya no hay memoria")
        pOperan.append(p[-1])
        pMemoria.append(consta.regresaMem(p[-1]))
        pTipos.append("entero")

    elif type(p[-1]) == float :
        if not consta.check(p[-1]) :
            if iniFltCNS < limFltCNS :
                cteFlt.append(p[-1])
                consta.add(p[-1],iniIntCNS)
                iniFltCNS += 1
            else :
                print("Error: ya no hay memoria")
        pOperan.append(p[-1])
        pMemoria.append(consta.regresaMem(p[-1]))
        pTipos.append("float")
    
    elif type(p[-1]) == str :
        if not consta.check(p[-1]) :
            if iniStrCNS < limStrCNS :
                cteStr.append(p[-1])
                consta.add(p[-1],iniIntCNS)
                iniStrCNS += 1
            else :
                print("Error: ya no hay memoria")
        pOperan.append(p[-1])
        pMemoria.append(consta.regresaMem(p[-1]))
        pTipos.append("string")

def p_pn_final(p):
    '''
    pn_final :
    '''    
    cuad.add("ENDOFPROGRAM", '', '', '')

    
def p_pn_print(p):
    '''
    pn_print :
    '''
    print("Cuads:")
    cuad.print()
    print("operadores:")
    print(pOperad)
    print("operandos:")
    print(pOperan)
    print("Tipos:")
    print(pTipos)
    print("Saltos:")
    print(pSaltos)
    print("Constantes:")
    cuad.toJson()
    consta.print()
    consta.toJson()
    #cuad.maquinaVirtualRun()
    

    
# Pruebas
archivo = open("ply-3.11.tar\dist\pruebas\caso_d.txt","r")
parser = yacc.yacc()
res = parser.parse(archivo.read())

