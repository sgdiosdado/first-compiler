import ply.lex as lex
import re

keywords = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'int': 'T_INT',
    'float': 'T_FLOAT'
}

tokens = [
    "ID",
    "INT",
    "FLOAT",
    "STRING",
    "PLUS",
    "MINUS",
    "MULT",
    "DIV",
    "ASSIGN",
    "COLON",
    "COMMA",
    "SEMICOLON",
    "DOT",
    "LPAR",
    "RPAR",
    "LBRACE",
    "RBRACE",
    "LT",
    "GT",
    "DT",
    "TYPE",
] + list(keywords.values())

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_ASSIGN = r'='
t_COLON = r':'
t_COMMA = r','
t_SEMICOLON = r';'
t_DOT = r'\.'
t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LT = r'<'
t_GT = r'>'
t_DT = r'<>'
t_PRINT = r'print'
t_STRING = r'\".*?\"'
# t_TYPE = r'(int|float|str)'

def t_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)

def t_ID(token):
    r'[A-Za-z]([A-Za-z]|[0-9])*'
    token.type = keywords.get(token.value, 'ID')
    return token

def t_FLOAT(token):
    r'[0-9]+(\.[0-9]+)'
    token.value = float(token.value)
    return token

def t_INT(token):
    r'[0-9]+'
    token.value = int(token.value)
    return token

def t_error(token):
    print("Illegal character '%s'" % token.value[0])
    token.lexer.skip(1)

lexer = lex.lex()