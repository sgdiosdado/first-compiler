
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLTGTDTleftPLUSMINUSleftMULTDIVrightUMINUSASSIGN COLON COMMA DIV DOT DT ELSE FLOAT GT ID IF INT LBRACE LPAR LT MINUS MULT PLUS PRINT PROGRAM RBRACE RPAR SEMICOLON STRING TYPE T_FLOAT T_INT VAR\n    calc    : EXPRESSION\n            | VAR_ASSIGN\n            | CONDITION\n            | WRITE\n            | PROGRA\n            | VARS\n            | epsilon\n    \n    epsilon : \n    \n    FACTOR  : INT\n            | FLOAT\n            | STRING\n    \n    FACTOR  : ID\n    \n    EXP : EXP PLUS EXP\n        | EXP MINUS EXP\n        | EXP MULT EXP\n        | EXP DIV EXP\n    \n    EXP  : FACTOR\n    \n    EXP  : LPAR EXPRESSION RPAR\n    \n    EXP : MINUS EXP %prec UMINUS\n    \n    EXPRESSION  : EXP\n                | EXPRESSION_REL\n    \n    EXPRESSION_REL  : EXP GT EXP\n                    | EXP LT EXP\n                    | EXP DT EXP\n    \n    VAR_ASSIGN  : ID ASSIGN EXPRESSION SEMICOLON\n                | ID ASSIGN ID SEMICOLON\n    \n    CONDITION   : IF LPAR EXPRESSION_REL RPAR BLOCK\n    \n    CONDITION   : IF LPAR EXPRESSION_REL RPAR BLOCK ELSE BLOCK\n    \n    BLOCK   : LBRACE BLOCK_ALT RBRACE\n    \n    BLOCK_ALT   : STATEMENT BLOCK_ALT\n    \n    BLOCK_ALT   : epsilon\n    \n    STATEMENT   : VAR_ASSIGN\n                | CONDITION\n                | WRITE\n    \n    WRITE   : PRINT LPAR WRITE_ALT RPAR SEMICOLON\n    \n    WRITE_ALT   : EXPRESSION\n    \n    WRITE_ALT   : EXPRESSION COMMA WRITE_ALT\n    \n    PROGRA  : PROGRAM ID SEMICOLON STATEMENT BLOCK\n            | PROGRAM ID SEMICOLON VARS BLOCK\n    \n    VARS    : VAR VARS_ALT\n    \n    VARS_ALT    : ID IDLIST COLON T_INT VARLIST SEMICOLON\n                | ID IDLIST COLON T_FLOAT VARLIST SEMICOLON\n    \n    IDLIST  : COMMA ID IDLIST\n    \n    IDLIST  : epsilon\n    \n    VARLIST : VARS_ALT\n            | epsilon\n    '
    
_lr_action_items = {'ID':([0,13,15,16,17,22,23,24,25,26,27,28,29,30,33,52,54,56,57,60,64,65,66,69,70,71,75,76,80,86,87,],[11,32,34,36,32,32,32,32,32,32,32,32,45,32,32,61,68,-26,-25,32,-32,-33,-34,-27,61,-35,36,36,61,-28,-29,]),'IF':([0,52,56,57,64,65,66,69,70,71,80,86,87,],[12,12,-26,-25,-32,-33,-34,-27,12,-35,12,-28,-29,]),'PRINT':([0,52,56,57,64,65,66,69,70,71,80,86,87,],[14,14,-26,-25,-32,-33,-34,-27,14,-35,14,-28,-29,]),'PROGRAM':([0,],[15,]),'VAR':([0,52,],[16,16,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,18,19,20,21,32,35,37,38,39,40,41,42,43,44,49,56,57,69,71,73,74,86,87,89,90,],[-8,0,-1,-2,-3,-4,-5,-6,-7,-20,-21,-12,-17,-9,-10,-11,-12,-40,-19,-13,-14,-15,-16,-22,-23,-24,-18,-26,-25,-27,-35,-38,-39,-28,-29,-41,-42,]),'LPAR':([0,12,13,14,17,22,23,24,25,26,27,28,29,30,33,60,],[13,30,13,33,13,13,13,13,13,13,13,13,13,13,13,13,]),'MINUS':([0,9,11,13,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,37,38,39,40,41,42,43,44,45,48,49,60,],[17,23,-12,17,17,-17,-9,-10,-11,17,17,17,17,17,17,17,17,17,-12,17,-19,-13,-14,-15,-16,23,23,23,-12,23,-18,17,]),'INT':([0,13,17,22,23,24,25,26,27,28,29,30,33,60,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'FLOAT':([0,13,17,22,23,24,25,26,27,28,29,30,33,60,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'STRING':([0,13,17,22,23,24,25,26,27,28,29,30,33,60,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'RPAR':([9,10,18,19,20,21,31,32,37,38,39,40,41,42,43,44,47,49,50,51,72,],[-20,-21,-17,-9,-10,-11,49,-12,-19,-13,-14,-15,-16,-22,-23,-24,58,-18,59,-36,-37,]),'SEMICOLON':([9,10,18,19,20,21,32,34,37,38,39,40,41,42,43,44,45,46,49,59,75,76,82,83,84,85,89,90,],[-20,-21,-17,-9,-10,-11,-12,52,-19,-13,-14,-15,-16,-22,-23,-24,56,57,-18,71,-8,-8,89,-45,-46,90,-41,-42,]),'COMMA':([9,10,18,19,20,21,32,36,37,38,39,40,41,42,43,44,49,51,68,],[-20,-21,-17,-9,-10,-11,-12,54,-19,-13,-14,-15,-16,-22,-23,-24,-18,60,54,]),'PLUS':([9,11,18,19,20,21,32,37,38,39,40,41,42,43,44,45,48,49,],[22,-12,-17,-9,-10,-11,-12,-19,-13,-14,-15,-16,22,22,22,-12,22,-18,]),'MULT':([9,11,18,19,20,21,32,37,38,39,40,41,42,43,44,45,48,49,],[24,-12,-17,-9,-10,-11,-12,-19,24,24,-15,-16,24,24,24,-12,24,-18,]),'DIV':([9,11,18,19,20,21,32,37,38,39,40,41,42,43,44,45,48,49,],[25,-12,-17,-9,-10,-11,-12,-19,25,25,-15,-16,25,25,25,-12,25,-18,]),'GT':([9,11,18,19,20,21,32,37,38,39,40,41,45,48,49,],[26,-12,-17,-9,-10,-11,-12,-19,-13,-14,-15,-16,-12,26,-18,]),'LT':([9,11,18,19,20,21,32,37,38,39,40,41,45,48,49,],[27,-12,-17,-9,-10,-11,-12,-19,-13,-14,-15,-16,-12,27,-18,]),'DT':([9,11,18,19,20,21,32,37,38,39,40,41,45,48,49,],[28,-12,-17,-9,-10,-11,-12,-19,-13,-14,-15,-16,-12,28,-18,]),'ASSIGN':([11,61,],[29,29,]),'LBRACE':([35,56,57,58,62,63,64,65,66,69,71,78,86,87,89,90,],[-40,-26,-25,70,70,70,-32,-33,-34,-27,-35,70,-28,-29,-41,-42,]),'COLON':([36,53,55,68,77,],[-8,67,-44,-8,-43,]),'RBRACE':([56,57,64,65,66,69,70,71,79,80,81,86,87,88,],[-26,-25,-32,-33,-34,-27,-8,-35,87,-8,-31,-28,-29,-30,]),'T_INT':([67,],[75,]),'T_FLOAT':([67,],[76,]),'ELSE':([69,87,],[78,-29,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'calc':([0,],[1,]),'EXPRESSION':([0,13,29,33,60,],[2,31,46,51,51,]),'VAR_ASSIGN':([0,52,70,80,],[3,64,64,64,]),'CONDITION':([0,52,70,80,],[4,65,65,65,]),'WRITE':([0,52,70,80,],[5,66,66,66,]),'PROGRA':([0,],[6,]),'VARS':([0,52,],[7,63,]),'epsilon':([0,36,68,70,75,76,80,],[8,55,55,81,84,84,81,]),'EXP':([0,13,17,22,23,24,25,26,27,28,29,30,33,60,],[9,9,37,38,39,40,41,42,43,44,9,48,9,9,]),'EXPRESSION_REL':([0,13,29,30,33,60,],[10,10,10,47,10,10,]),'FACTOR':([0,13,17,22,23,24,25,26,27,28,29,30,33,60,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'VARS_ALT':([16,75,76,],[35,83,83,]),'WRITE_ALT':([33,60,],[50,72,]),'IDLIST':([36,68,],[53,77,]),'STATEMENT':([52,70,80,],[62,80,80,]),'BLOCK':([58,62,63,78,],[69,73,74,86,]),'BLOCK_ALT':([70,80,],[79,88,]),'VARLIST':([75,76,],[82,85,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> calc","S'",1,None,None,None),
  ('calc -> EXPRESSION','calc',1,'p_calc','parser.py',15),
  ('calc -> VAR_ASSIGN','calc',1,'p_calc','parser.py',16),
  ('calc -> CONDITION','calc',1,'p_calc','parser.py',17),
  ('calc -> WRITE','calc',1,'p_calc','parser.py',18),
  ('calc -> PROGRA','calc',1,'p_calc','parser.py',19),
  ('calc -> VARS','calc',1,'p_calc','parser.py',20),
  ('calc -> epsilon','calc',1,'p_calc','parser.py',21),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','parser.py',31),
  ('FACTOR -> INT','FACTOR',1,'p_factor','parser.py',37),
  ('FACTOR -> FLOAT','FACTOR',1,'p_factor','parser.py',38),
  ('FACTOR -> STRING','FACTOR',1,'p_factor','parser.py',39),
  ('FACTOR -> ID','FACTOR',1,'p_factor_id','parser.py',45),
  ('EXP -> EXP PLUS EXP','EXP',3,'p_exp','parser.py',51),
  ('EXP -> EXP MINUS EXP','EXP',3,'p_exp','parser.py',52),
  ('EXP -> EXP MULT EXP','EXP',3,'p_exp','parser.py',53),
  ('EXP -> EXP DIV EXP','EXP',3,'p_exp','parser.py',54),
  ('EXP -> FACTOR','EXP',1,'p_exp_factor','parser.py',60),
  ('EXP -> LPAR EXPRESSION RPAR','EXP',3,'p_expression_paren','parser.py',66),
  ('EXP -> MINUS EXP','EXP',2,'p_exp_uminus','parser.py',72),
  ('EXPRESSION -> EXP','EXPRESSION',1,'p_expression','parser.py',78),
  ('EXPRESSION -> EXPRESSION_REL','EXPRESSION',1,'p_expression','parser.py',79),
  ('EXPRESSION_REL -> EXP GT EXP','EXPRESSION_REL',3,'p_expression_relop','parser.py',85),
  ('EXPRESSION_REL -> EXP LT EXP','EXPRESSION_REL',3,'p_expression_relop','parser.py',86),
  ('EXPRESSION_REL -> EXP DT EXP','EXPRESSION_REL',3,'p_expression_relop','parser.py',87),
  ('VAR_ASSIGN -> ID ASSIGN EXPRESSION SEMICOLON','VAR_ASSIGN',4,'p_var_assign','parser.py',93),
  ('VAR_ASSIGN -> ID ASSIGN ID SEMICOLON','VAR_ASSIGN',4,'p_var_assign','parser.py',94),
  ('CONDITION -> IF LPAR EXPRESSION_REL RPAR BLOCK','CONDITION',5,'p_condition','parser.py',100),
  ('CONDITION -> IF LPAR EXPRESSION_REL RPAR BLOCK ELSE BLOCK','CONDITION',7,'p_condition_else','parser.py',106),
  ('BLOCK -> LBRACE BLOCK_ALT RBRACE','BLOCK',3,'p_block','parser.py',112),
  ('BLOCK_ALT -> STATEMENT BLOCK_ALT','BLOCK_ALT',2,'p_block_alt','parser.py',118),
  ('BLOCK_ALT -> epsilon','BLOCK_ALT',1,'p_block_alt_epsilon','parser.py',124),
  ('STATEMENT -> VAR_ASSIGN','STATEMENT',1,'p_statement','parser.py',130),
  ('STATEMENT -> CONDITION','STATEMENT',1,'p_statement','parser.py',131),
  ('STATEMENT -> WRITE','STATEMENT',1,'p_statement','parser.py',132),
  ('WRITE -> PRINT LPAR WRITE_ALT RPAR SEMICOLON','WRITE',5,'p_write','parser.py',138),
  ('WRITE_ALT -> EXPRESSION','WRITE_ALT',1,'p_write_alt','parser.py',144),
  ('WRITE_ALT -> EXPRESSION COMMA WRITE_ALT','WRITE_ALT',3,'p_write_alt_chain','parser.py',150),
  ('PROGRA -> PROGRAM ID SEMICOLON STATEMENT BLOCK','PROGRA',5,'p_progra','parser.py',156),
  ('PROGRA -> PROGRAM ID SEMICOLON VARS BLOCK','PROGRA',5,'p_progra','parser.py',157),
  ('VARS -> VAR VARS_ALT','VARS',2,'p_vars','parser.py',163),
  ('VARS_ALT -> ID IDLIST COLON T_INT VARLIST SEMICOLON','VARS_ALT',6,'p_vars_alt','parser.py',169),
  ('VARS_ALT -> ID IDLIST COLON T_FLOAT VARLIST SEMICOLON','VARS_ALT',6,'p_vars_alt','parser.py',170),
  ('IDLIST -> COMMA ID IDLIST','IDLIST',3,'p_idlist','parser.py',176),
  ('IDLIST -> epsilon','IDLIST',1,'p_idlist_epsilon','parser.py',182),
  ('VARLIST -> VARS_ALT','VARLIST',1,'p_varlist','parser.py',188),
  ('VARLIST -> epsilon','VARLIST',1,'p_varlist','parser.py',189),
]
