#! /usr/bin/python
import ply.yacc as yacc

import termlex
from termlex import tokens

def p_bodys(p):
    '''bodys : empty '''
    p[0] = p[1]

def p_comment_bodys(p):
    '''bodys : comment bodys'''
    p[0] = p[2]

def p_term_bodsy(p):
    '''bodys : term '.' bodys'''
    p[0] = [p[1]] + p[3]

def p_empty(p):
    '''empty :'''
    p[0] = []


def p_comment(p):
    '''comment : COMMENT'''
    p[0] = p[1]

def p_term(p):
    '''term : list
            | tuple
            | atom
            | number
            | string
            | binary
            | maps'''
    p[0] = p[1]

def p_empty_list(p):
    '''list : '[' ']' '''
    p[0] = []

def p_single_elem_list(p):
    '''list : '[' term ']' '''
    p[0] = [p[2]]

def p_multi_elem_list(p):
    '''list : '[' term ',' terms ']' '''
    p[0] = [p[2]] + p[4]

def p_single_term_terms(p):
    '''terms : term '''
    p[0] = [p[1]]

def p_multi_term_terms(p):
    '''terms : term ',' nn_terms '''
    p[0] = [p[1]] + p[3]

def p_nn_terms(p):
    '''nn_terms : terms '''
    p[0] = p[1]

def p_empty_tuple(p):
    '''tuple : '{' '}' '''
    p[0] = ()

def p_single_elem_tuple(p):
    '''tuple : '{' term '}' '''
    p[0] = (p[2],)

def p_multi_elem_tuple(p):
    '''tuple : '{' term ',' terms '}' '''
    p[0] = (p[2], ) + tuple(p[4])

def p_empty_maps(p):
    '''maps : '#' '{' '}'  '''
    p[0] = {}

def p_nn_maps(p):
    '''maps : '#' '{' maps_items '}' '''
    p[0] = dict(p[3])

def p_single_elem_maps_items(p):
    '''maps_items : term MAP_ASSIGN term'''
    p[0] = [(p[1], p[3])]

def p_multi_elem_maps_items(p):
    '''maps_items : term MAP_ASSIGN term ',' maps_items'''
    p[0] = [(p[1], p[3])] + p[5]

def p_atom(p):
    'atom : ATOM'
    p[0] = p[1]

def p_string(p):
    'string : STRING'
    p[0] = p[1]

def p_binary(p):
    'binary : BINARY'
    p[0] = p[1]

def p_number(p):
    '''number : INTEGER
              | FLOAT'''
    p[0] = p[1]

def p_error(p):
    print 'Syntax error in input'
    print p

def consult(filename):
    lexer = termlex.lexer
    parser = yacc.yacc()
    f = open(filename, mode='r')
    s = f.read()
    f.close()
    result = parser.parse(s, lexer)
    return result


data = '''
#{abc => 100, bcd => 200, [1,2,3] => [900]}.
'''
lexer = termlex.lexer
parser = yacc.yacc()

result = parser.parse(data, lexer)
print result

