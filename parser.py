import ply.yacc as yacc
from lexer import tokens

symbol_table = {}

precedence = (
    ('nonassoc', 'LT', 'GT', 'DT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS')
)

def p_calc(p):
    """
    calc    : EXPRESSION
            | VAR_ASSIGN
            | CONDITION
            | WRITE
            | PROGRA
            | VARS
            | epsilon
    """
    evaluate(p[1])

def p_error(token):
    print(f"Syntax Error: {token.value!r}")
    token.lexer.skip(1)

def p_epsilon(p):
    """
    epsilon : 
    """
    p[0] = None

def p_factor(p):
    """
    FACTOR  : INT
            | FLOAT
            | STRING
    """
    p[0] = p[1]

def p_factor_id(p):
    """
    FACTOR  : ID
    """
    p[0] = ('var', p[1])

def p_exp(p):
    """
    EXP : EXP PLUS EXP
        | EXP MINUS EXP
        | EXP MULT EXP
        | EXP DIV EXP
    """
    p[0] = (p[2], p[1], p[3])

def p_exp_factor(p):
    """
    EXP  : FACTOR
    """
    p[0] = p[1]

def p_expression_paren(p):
    """
    EXP  : LPAR EXPRESSION RPAR
    """
    p[0] = p[2]

def p_exp_uminus(p):
    """
    EXP : MINUS EXP %prec UMINUS
    """
    p[0] = -p[2]

def p_expression(p):
    """
    EXPRESSION  : EXP
                | EXPRESSION_REL
    """
    p[0] = p[1]

def p_expression_relop(p):
    """
    EXPRESSION_REL  : EXP GT EXP
                    | EXP LT EXP
                    | EXP DT EXP
    """
    p[0] = (p[2], p[1], p[3])

def p_var_assign(p):
    """
    VAR_ASSIGN  : ID ASSIGN EXPRESSION SEMICOLON
                | ID ASSIGN ID SEMICOLON
    """
    p[0] = ('=', p[1], p[3])

def p_condition(p):
    """
    CONDITION   : IF LPAR EXPRESSION_REL RPAR BLOCK
    """
    p[0] = ('if', p[3], p[5])

def p_condition_else(p):
    """
    CONDITION   : IF LPAR EXPRESSION_REL RPAR BLOCK ELSE BLOCK
    """
    p[0] = ('ifelse', p[3], p[5], p[7])

def p_block(p):
    """
    BLOCK   : LBRACE BLOCK_ALT RBRACE
    """
    p[0] = p[2]

def p_block_alt(p):
    """
    BLOCK_ALT   : STATEMENT BLOCK_ALT
    """
    p[0] = (p[1], p[2])

def p_block_alt_epsilon(p):
    """
    BLOCK_ALT   : epsilon
    """
    p[0] = p[1]

def p_statement(p):
    """
    STATEMENT   : VAR_ASSIGN
                | CONDITION
                | WRITE
    """
    p[0] = p[1]

def p_write(p):
    """
    WRITE   : PRINT LPAR WRITE_ALT RPAR SEMICOLON
    """
    p[0] = ('print', p[3])

def p_write_alt(p):
    """
    WRITE_ALT   : EXPRESSION
    """
    p[0] = p[1]

def p_write_alt_chain(p):
    """
    WRITE_ALT   : EXPRESSION COMMA WRITE_ALT
    """
    p[0] = (p[1], p[3])

def p_progra(p):
    """
    PROGRA  : PROGRAM ID SEMICOLON STATEMENT BLOCK
            | PROGRAM ID SEMICOLON VARS BLOCK
    """
    p[0] = ('program', p[4], p[5]);

def p_vars(p):
    """
    VARS    : VAR VARS_ALT
    """
    p[0] = ('declare', p[2])

def p_vars_alt(p):
    """
    VARS_ALT    : ID IDLIST COLON T_INT VARLIST SEMICOLON
                | ID IDLIST COLON T_FLOAT VARLIST SEMICOLON
    """
    p[0] = (p[1], p[2])

def p_idlist(p):
    """
    IDLIST  : COMMA ID IDLIST
    """
    p[0] = (p[2], p[3])

def p_idlist_epsilon(p):
    """
    IDLIST  : epsilon
    """
    p[0] = None

def p_varlist(p):
    """
    VARLIST : VARS_ALT
            | epsilon
    """
    p[0] = p[1]


def print_func(p: tuple):
    if type(p) is not None and type(p) != tuple:
        print(evaluate(p))
    else:
        if p[0] == 'var':
            if p[1] not in symbol_table:
                print(f'Undeclared variable: {p[1]}')
                return
            print(symbol_table[p[1]])
            if len(p) == 2:
                return None
            if type(p[2]) == tuple:
                print_func(p[2])
            elif type(p[2]) is not None:
                print(evaluate(p[2]))
        else:
            print(evaluate(p[0]))
            if type(p[1]) == tuple:
                print_func(p[1])
            elif type(p[1]) is not None:
                print(evaluate(p[1]))
    return None

def save_in_symbol_table(p: tuple):
    global symbol_table
    if p[0] is None: return
    symbol_table[p[0]] = None
    if type(p[1]) == tuple:
        save_in_symbol_table(p[1])

def execute_block(p:tuple):
    if p is None: return
    evaluate(p[0])
    if len(p) > 1:
        execute_block(p[1])


def evaluate(p):
    global symbol_table
    if type(p) == tuple:
        if p[0] == '+':
            return evaluate(p[1]) + evaluate(p[2])
        elif p[0] == '-':
            return evaluate(p[1]) - evaluate(p[2])
        elif p[0] == '*':
            return evaluate(p[1]) * evaluate(p[2])
        elif p[0] == '/':
            return evaluate(p[1]) / evaluate(p[2])
        elif p[0] == '<':
            return evaluate(p[1]) < evaluate(p[2])
        elif p[0] == '>':
            return evaluate(p[1]) > evaluate(p[2])
        elif p[0] == '<>':
            return evaluate(p[1]) != evaluate(p[2])
        
        elif p[0] == '=':
            symbol_table[p[1]] = evaluate(p[2])
        elif p[0] == 'var':
            if p[1] not in symbol_table:
                return print(f'Undeclared variable: {p[1]}')
            else:
                return symbol_table[p[1]]
        
        elif p[0] == 'if':
            if evaluate(p[1]):
                return evaluate(p[2][0])
        elif p[0] == 'ifelse':
            if evaluate(p[1]):
                return evaluate(p[2][0])
            return evaluate(p[3][0])
        elif p[0] == 'print':
            return print_func(p[1])
        
        elif p[0] == 'declare':
            save_in_symbol_table(p[1])
        elif p[0] == 'program':
            evaluate(p[1])
            execute_block(p[2])
    else:
        return p
parser = yacc.yacc()

