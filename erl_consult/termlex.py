#! /usr/bin/python
import ply.lex as lex

tokens = (
    'COMMENT',
    'BINARY',
    'ATOM',
    'STRING',
    'INTEGER',
    'FLOAT',
    'MAP_ASSIGN',
)

literals = '[]{},.#'
t_ignore = ' \t'

def t_COMMENT(t):
    r'%.*'

def t_BINARY(t):
    r'<<\s*\"[^\"]*\"\s*>>'
    start = t.value.find('"')
    end = t.value.rfind('"')
    t.value = t.value[start + 1:end]
    return t

def t_ATOM(t):
    r'([a-z][a-zA-Z0-9_]*)|(\'[^\']+\')'
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    t.value = t.value[1:-1]
    return t

def t_FLOAT(t):
    r'[\+\-]?[0-9]+\.[0-9]+'
    # print 'float %s' % t.value
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'[\+\-]?[0-9]+'
    # print 'integer %s' % t.value
    t.value = int(t.value)
    return t

def t_MAP_ASSIGN(t):
    r'=>'
    return t

def t_newline(t):
    r'\r?\n'
    t.lexer.lineno += 1

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)


lexer = lex.lex()

