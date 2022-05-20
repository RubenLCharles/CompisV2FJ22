import ply.yacc as yacc
from lexer import tokens
import re
import os

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
    asignacion : ID ASSIGN expresiones
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
    retorno : RETURN LPAREN expresiones RPAREN SEMIC
    '''

def p_lectura(p):
    '''
    lectura : READ LPAREN ID lec_aux RPAREN SEMIC
    '''

def p_lec_aux(p):
    '''
    lec_aux : COMMA ID lec_aux
            | empty
    '''

def p_escritura(p):
    '''
    escritura : WRITE LPAREN esc_aux RPAREN SEMIC
    '''

def p_esc_aux(p):
    '''
    esc_aux : STRING_CTE esc_rec
            | expresiones esc_rec
            | empty
    '''

def p_esc_rec(p):
    '''
    esc_rec : COMMA esc_aux
            | empty
    '''

def p_decision(p):
    '''
    decision : IF LPAREN expresiones RPAREN THEN bloque dec_aux
    '''

def p_dec_aux(p):
    '''
    dec_aux : else
            | empty
    '''

def p_else(p):
    '''
    else : ELSE bloque
    '''

def p_loop_cond(p):
    '''
    loop_cond : WHILE LPAREN expresiones RPAREN DO bloque
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
    or_check : OR_LOG expresiones
             | empty
    '''

def p_t_exp(p):
    '''
    t_exp : g_exp and_check
    '''

def p_and_check(p):
    '''
    and_check : AND_LOG t_exp
              | empty
    '''

def p_g_exp(p):
    '''
    g_exp : m_exp op_check
    '''

def p_op_check(p):
    '''
    op_check : empty
             | comparacion m_exp
    '''

def p_comparacion(p):
    '''
    comparacion : GT_LOG
                | LT_LOG
                | EQUAL_LOG
                | NE_LOG
    '''

def p_m_exp(p):
    '''
    m_exp : termino m_rec
    '''

def p_m_rec(p):
    '''
    m_rec : PLUS_OP m_exp
          | MINUS_OP m_exp
          | empty
    '''

def p_termino(p):
    '''
    termino : factor term_rec
    '''

def p_term_rec(p):
    '''
    term_rec : MULT_OP termino
             | DIV_OP termino
             | empty
    '''

def p_factor(p):
    '''
    factor : LPAREN expresiones RPAREN
           | INT_CTE
           | FLOAT_CTE
           | ID
           | llamada_func
    '''

# FUNCIONES ESPECIALES
def p_empty(p):
     'empty :'
     pass



parser = yacc.yacc()
res = parser.parse("program PRUEBA ; main () { 2 }")
