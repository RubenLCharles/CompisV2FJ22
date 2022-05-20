import ply.lex as lex
import re
#Lista de Tokens para el lenguaje
tokens = [
    #asignacion
    'ASSIGN',
    #operadores aritmeticos
    'PLUS_OP','MINUS_OP','MULT_OP','DIV_OP',
    #operadores logicos
    'EQUAL_LOG','LT_LOG','LTE_LOG','GT_LOG','GTE_LOG','NE_LOG',
    'OR_LOG','AND_LOG',
    #simbolos para conjuntos y scope
    'LPAREN','RPAREN','LBRACK','RBRACK','LCURLY','RCURLY',
    #operadores especiales
    'COMMA','SEMIC','COLON',
    #constantes
    'FLOAT_CTE','INT_CTE','CHAR_CTE', 'STRING_CTE',
    'NEW_LINE','ID','COMMENT',
    #funciones
    'COLOR'
]

#palabras reservadas
keywords = {
    'program' : 'PROGRAM',
    'void' : 'VOID',
    'main' : 'MAIN',
    'while' : 'WHILE',
    'write' : 'WRITE',
    'read' : 'READ',
    'return' : 'RETURN',
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'vars' :'VARS',
    'function' : 'FUNCTION', 
    'while' : 'WHILE',
    'do' : 'DO', 
    'for' : 'FOR',
    'to' : 'TO', 
    'point' : 'POINT',
    'line' : 'LINE',
    'arc' : 'ARC',
    'penup' : 'PENUP',
    'pendown' : 'PENDOWN',
    'circle' : 'CIRCLE',
    'size' : 'SIZE',  
    #tipos de datos
    'int' : 'INT_TYPE',
    'float' : 'FLOAT_TYPE',
    'char' : 'CHAR_TYPE'

}

tokens = tokens + list(keywords.values())

#Expresiones Regulares para tokens
t_PLUS_OP = r'\+'
t_MINUS_OP = r'-'
t_MULT_OP = r'\*'
t_DIV_OP = r'/'
t_ASSIGN = r'\='
t_EQUAL_LOG = r'\=\='
t_LT_LOG = r'\<'
t_LTE_LOG = r'\<\='
t_GT_LOG = r'\>'
t_GTE_LOG = r'\>\='
t_NE_LOG = r'\<\>'
t_OR_LOG = r'\|'
t_AND_LOG = r'\&'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_COMMA = r'\,'
t_SEMIC = r'\;'
t_COLON = r'\:'
t_ignore = ' \t'



def t_FLOAT_CTE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT_CTE(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING_CTE(t):
    r"(\"([^\\\"]|\\.)+\")|(\'([^\\\']|\\.)+\')"
    t.value = str(t.value)
    return t

def t_CHAR_CTE(t):
    r"'[a-zA-Z]'"
    t.value = str(t.value)
    return t

def t_NEW_LINE(t):
    r'\n+'
    t.lexer.lineno += 1
    pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID')
    return t

#Error generico
def t_error(t):
    if t:
        print("Illegal character '{}' at: {}".format(t.value[0], t.lexer.lineno))
        t.lexer.skip(1)
    else:
        print ("Error from lex")
lexer = lex.lex()

def lex_test(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok :
            break
        else:
            print(tok)