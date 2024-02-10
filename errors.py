from production_rules import BOOLEAN_RELATION
from itertools import product

DATA_TYPES = ['<DT_INT>', '<DT_DECI>', '<DT_STR>', '<DT_CHAR>', '<DT_BOOL>']
DATA_VALUES = ['<INTEGER>', '<DECIMAL>', '<STRING>', '<CHAR>', '<BOOL_VALUE>']
RELATIONAL_VALUES = ['<IDENTIFIER', '<INTEGER>', '<DECIMAL>', '<STRING>', '<CHAR>', '<BOOL_VALUE>']
ARITHMETIC_OPS = ['<PLUS>', '<MINUS>', '<MULTIPLY>', '<DIVIDE>']
ASSIGNMENT_OPS = ['<ADD_ASS>', '<SUBTRACT_ASS>', '<MULTIPLY_ASS>', '<DIVIDE_ASS>', '<MODULO_ASS>']
NEW_PRINCIPLES = ['<ARITHSEQ>', '<ARITHSER>', '<GEOSEQ>', '<GEOSER>', '<DISTANCE>', '<SLOPE>', '<PYTHAGOREAN>',
                  '<QUADRATIC>', '<FORCE>', '<WORK>', '<ACCELERATION>', '<POWER>', '<MOMENTUM>', '<POTENTIAL>',
                  '<KINETIC>', '<TOINT>', '<TODECI>', '<TOSTR>']
CONDITIONALS = ['<WHEN>', '<OTHERWISE>', '<OTHERWISE><WHITESPACE><WHEN>']
LOGICAL_OPERATORS = ['<LOGICAL_NOT>', '<LOGICAL_OR>', '<LOGICAL_AND>']
RELATIONAL_OPERATORS = ['<EQUAL_TO>', '<NOT_EQUAL>', '<GREATER_THAN>', '<LESS_THAN>', '<GREATER_THAN_EQ>', '<LESS_THAN_EQ>']

def find_error(token):
    # e.g. bool
    if token in DATA_TYPES:
        return 'DeclarationError: Variable name required'

    # e.g. x > y AND
    elif token.startswith("<IDENTIFIER><WHITESPACE>") and ("<EQUAL_TO>" in token or "<NOT_EQUAL>" in token or "<GREATER_THAN>" in token or "<LESS_THAN>" in token or "<GREATER_THAN_EQ>" in token or "<LESS_THAN_EQ>" in token) and "<WHITESPACE><IDENTIFIER><WHITESPACE>" in token and ("<LOGICAL_NOT>" in token or "<LOGICAL_OR>" in token or "<LOGICAL_AND>" in token):
        return "SyntaxError: Missing right-hand boolean relation"

    # e.g. AND u <= z
    elif ((token.startswith("<LOGICAL_NOT>")) or (token.startswith("<LOGICAL_OR>")) or (token.startswith("<LOGICAL_AND>"))) and "<WHITESPACE><IDENTIFIER><WHITESPACE>" in token and ("<EQUAL_TO>" in token or "<NOT_EQUAL>" in token or "<GREATER_THAN>" in token or "<LESS_THAN>" in token or "<GREATER_THAN_EQ>" in token or "<LESS_THAN_EQ>" in token) and "<WHITESPACE><IDENTIFIER>" in token:
        return "SyntaxError: Missing left-hand boolean relation"

    # e.g. x + y ==
    elif token.startswith("<IDENTIFIER><WHITESPACE>") and any(operator in token for operator in ARITHMETIC_OPS) and "<WHITESPACE><IDENTIFIER><WHITESPACE>" in token and ("<EQUAL_TO>" in token or "<NOT_EQUAL>" in token or "<GREATER_THAN>" in token or "<LESS_THAN>" in token or "<GREATER_THAN_EQ>" in token or "<LESS_THAN_EQ>" in token):
        return "SyntaxError: Missing right-hand boolean relation"

    # e.g. == x - y
    elif (token.startswith("<EQUAL_TO>") or token.startswith("<NOT_EQUAL>") or token.startswith("<GREATER_THAN>") or token.startswith("<LESS_THAN>") or token.startswith("<GREATER_THAN_EQ>") or token.startswith("<GREATER_THAN_EQ>") or token.startswith("<LESS_THAN_EQ>")) and "<WHITESPACE><IDENTIFIER><WHITESPACE>" in token and any(operator in token for operator in ARITHMETIC_OPS) and "<WHITESPACE><IDENTIFIER>" in token:
        return "SyntaxError: Missing left-hand boolean relation"

    # e.g <= x
    elif (token.startswith("<EQUAL_TO>") or token.startswith("<NOT_EQUAL>") or token.startswith("<GREATER_THAN>") or token.startswith("<LESS_THAN>") or token.startswith("<GREATER_THAN_EQ>") or token.startswith("<LESS_THAN_EQ>")) and "<WHITESPACE>" in token and ("<IDENTIFIER>" in token or "<INTEGER>" in token or "<DECIMAL>" in token or "<BOOL_VALUE>" in token or "<STRING>" in token):
        return "SyntaxError: Left-hand operand required"

    # e.g x <=
    elif any(token.startswith(f'{value}<WHITESPACE>{operator}') for value, operator in product(RELATIONAL_VALUES, RELATIONAL_OPERATORS)):
        return "SyntaxError: Right-hand operand required"

    elif token.startswith('<IDENTIFIER>') and all(operator not in token for operator in LOGICAL_OPERATORS) and all(op_part not in token for op in product(ARITHMETIC_OPS, ASSIGNMENT_OPS, LOGICAL_OPERATORS, RELATIONAL_OPERATORS) for op_part in op):
        return 'TypeError: Variable must be declared with a data type'

    # e.g. int 3age = 10
    elif (token.startswith('<DT_')) and (token[8:] == '<WHITESPACE><INVALID_TOKEN><WHITESPACE>' or token[8:] == '<WHITESPACE><INVALID_TOKEN>' or token[7:] == '<WHITESPACE><INVALID_TOKEN><WHITESPACE>' or token[7:] == '<WHITESPACE><INVALID_TOKEN>'):
        return 'DeclarationError: Invalid variable name'

    # e.g. int x= 10
    elif (token.startswith('<DT_')) and ('<IDENTIFIER>' in token) and ('<ASS_OP>' in token) and ('<WHITESPACE><ASS_OP><WHITESPACE>' not in token) and ((token.count('<VARIABLE><WHITESPACE>') == 0) or (token.count('<WHITESPACE><VARIABLE>') == 0)):
        return 'SyntaxError: Whitespace required before and after assignment operator'

    # str x = 32sad
    elif (token.startswith('<DT_')) and ('<ASS_OP><WHITESPACE><INVALID_TOKEN>' in token):
        return 'ValueError: Invalid value'

    # e.g. int x = 32.2
    elif (token.startswith('<DT_INT><WHITESPACE><IDENTIFIER>')) and ('<WHITESPACE><ASS_OP><WHITESPACE>' in token) and ('<INTEGER>' not in token) and ('<ASS_OP><WHITESPACE><VARIABLE>' not in token):
        return 'ValueError: Invalid value for int data type'

    # e.g. deci x = '32.12'
    elif (token.startswith('<DT_DECI><WHITESPACE><IDENTIFIER>')) and ('<WHITESPACE><ASS_OP><WHITESPACE>' in token) and ('<DECIMAL>' not in token) and ('<ASS_OP><WHITESPACE><VARIABLE>' not in token):
        return 'ValueError: Invalid value for deci data type'

    # e.g. str x = TRUE
    elif (token.startswith('<DT_STR><WHITESPACE><IDENTIFIER>')) and ('<WHITESPACE><ASS_OP><WHITESPACE>' in token) and ('<STRING>' not in token) and ('<ASS_OP><WHITESPACE><VARIABLE>' not in token):
        return 'ValueError: Invalid value for str data type'

    # e.g. char x = '23'
    elif (token.startswith('<DT_CHAR><WHITESPACE><IDENTIFIER>')) and ('<WHITESPACE><ASS_OP><WHITESPACE>' in token) and ('<CHAR>' not in token) and ('<ASS_OP><WHITESPACE><VARIABLE>' not in token):
        return 'ValueError: Invalid value for char data type'

    # e.g. BOOL = 'TRUE'
    elif (token.startswith('<DT_BOOL><WHITESPACE><IDENTIFIER>')) and ('<WHITESPACE><ASS_OP><WHITESPACE>' in token) and ('<BOOL_VALUE>' not in token) and ('<ASS_OP><WHITESPACE><VARIABLE>' not in token):
        return 'ValueError: Invalid value for bool data type'

    # e.g. int x y
    elif (token.startswith('<DT_')) and ('<WHITESPACE><IDENTIFIER><WHITESPACE><IDENTIFIER>' in token):
        return 'DeclarationError: Comma separator required'

    # e.g. int x,y
    elif (token.startswith('<DT_')) and ('<IDENTIFIER><COMMA><IDENTIFIER>' in token):
        return 'DeclarationError: Whitespace required after comma separator'

    # e.g. int x, 3num
    elif (token.startswith('<DT_')) and ('<WHITESPACE><IDENTIFIER><COMMA><WHITESPACE><INVALID_TOKEN>' in token or '<IDENTIFIER><COMMA><INVALID_TOKEN>' in token):
        return 'DeclarationError: Invalid variable name'

    elif (token.startswith('<DT_')) and ('<INVALID_TOKEN>' in token) and ('<ASS_OP>' in token) and (token.count('<WHITESPACE><ASS_OP>') == 0 and token.count('<ASS_OP><WHITESPACE>') == 0):
        return 'DeclarationError: Whitespace required before and after "="'

    elif (token.startswith('<DT_')) and ('<INVALID_TOKEN>' in token) and ('<ASS_OP>' in token) and (token.count('<COMMA><IDENTIFIER>') == 0):
        return 'DeclarationError: Whitespace required before and after "="'

    elif (token.startswith('<DT_')) and ('<INVALID_TOKEN>' in token) and ('<ASS_OP><INTEGER>' in token):
        return 'DeclarationError: Invalid token found'

    # e.g. int X =
    elif (token.startswith('<DT_')) and (token.endswith('<WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE>')):
        return 'DeclarationError: Value required'

    # e.g. bool x = input()
    elif ('<INPUT>' in token) and ('<DT_BOOL>' in token):
        return 'Input function cannot accept bool value'

    # e.g. x = input()
    elif ('<INPUT>' in token) and ('<DT_INT>' not in token and '<DT_STR>' not in token and 'DT_CHAR' not in token and 'DT_DECI' not in token):
        return 'Input must be assigned to valid data type'

    # e.g. int input()
    elif ('<INPUT>' in token) and ('<ASS_OP>' not in token):
        return 'Input must be assigned to data type'

    elif ('<OUTPUT><WHITESPACE>' in token or '<OUTPUT><STRING>' in token or '<OUTPUT><VARIABLE>' in token or '<OUTPUT><CONSTANT>' in token) and ('<PARENTHESIS_OPEN>' not in token):
        return 'Opening parenthesis required after output function'

    elif ('<OUTPUT><PARENTHESIS_OPEN>' in token) and ('<PARENTHESIS_CLOSE' not in token):
        return 'Parenthesis need to be closed'

    elif ('<OUTPUT><WHITESPACE>' in token):
        return 'Whitespace not required after output function'

    elif ('<OUTPUT><PARENTHESIS_OPEN>' in token) and ('<STRING>' not in token) and ('<VARIABLE>' not in token) and ('<CONSTANT>' not in token):
        return 'Output requires content inside parentheses'

    # e.g. int x = 10 + 10.5
    elif any(operator in token for operator in ARITHMETIC_OPS) and "<DT_INT>" in token and (('<DECIMAL>' in token) or ('<STRING>' in token) or ('<CHAR>' in token) or ('<BOOL_VALUE>' in token)):
        return "ValueError: Invalid value for int data type"

    # e.g. deci x = 10.5 + "string"
    elif any(operator in token for operator in ARITHMETIC_OPS) and "<DT_DECI>" in token and (('<CHAR>' in token) or ('<STRING>' in token) or ('<INTEGER>' in token) or ('<BOOL_VALUE>' in token)):
        return "ValueError: Invalid value for deci data type"

    # e.g. str x = "string" + 10
    elif any(operator in token for operator in ARITHMETIC_OPS) and "<DT_STR>" in token and (('<DECIMAL>' in token) or ('<INTEGER>' in token) or ('<INTEGER>' in token) or ('<BOOL_VALUE>' in token)):
        return "ValueError: Invalid value for str data type"

    # e.g. char x = "c" + "string"
    elif any(operator in token for operator in ARITHMETIC_OPS) and "<DT_CHAR>" in token and (('<DECIMAL>' in token) or ('<STRING>' in token) or ('<INTEGER>' in token) or ('<BOOL_VALUE>' in token)):
        return "ValueError: Invalid value for char data type"

    # e.g. bool x = TRUE + 100
    elif any(operator in token for operator in ARITHMETIC_OPS) and "<DT_BOOL>" in token and (('<DECIMAL>' in token) or ('<STRING>' in token) or ('<INTEGER>' in token) or ('<INTEGER>' in token)):
        return "ValueError: Invalid value for bool data type"

    elif any(operator in token for operator in ARITHMETIC_OPS) and "<DT_INT>" in token and (('<DECIMAL>' in token) or ('<STRING>' in token) or ('<CHAR>' in token) or ('<BOOL_VALUE>' in token)):
        return "ValueError: Invalid value for int data type"

    elif any(operator in token for operator in ARITHMETIC_OPS) and "<DT_DECI>" in token and (('<CHAR>' in token) or ('<STRING>' in token) or ('<INTEGER>' in token) or ('<BOOL_VALUE>' in token)):
        return "ValueError: Invalid value for deci data type"

    elif any(operator in token for operator in ARITHMETIC_OPS) and "<DT_STR>" in token and (('<DECIMAL>' in token) or ('<INTEGER>' in token) or ('<INTEGER>' in token) or ('<BOOL_VALUE>' in token)):
        return "ValueError: Invalid value for str data type"

    elif any(operator in token for operator in ARITHMETIC_OPS) and "<DT_CHAR>" in token and (('<DECIMAL>' in token) or ('<STRING>' in token) or ('<INTEGER>' in token) or ('<BOOL_VALUE>' in token)):
        return "ValueError: Invalid value for char data type"

    # e.g.
    elif any(operator in token for operator in ARITHMETIC_OPS) and "<DT_BOOL>" in token and (('<DECIMAL>' in token) or ('<STRING>' in token) or ('<INTEGER>' in token) or ('<INTEGER>' in token)):
        return "ValueError: Invalid value for bool data type"

    # loop i = 1 to 10
    elif token == "<LOOP><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><INTEGER><WHITESPACE><TO><WHITESPACE><INTEGER>":
        return "SyntaxError: Missing loop variable update expression"

    # loop i = 1 to 10:
    elif token == "<LOOP><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><INTEGER><WHITESPACE><TO><WHITESPACE><INTEGER><COLON>":
        return "SyntaxError: Missing loop variable update expression"

    elif token.startswith('<LOOP>') and not token.endswith('<COLON_DELIMITER>'):
        return "SyntaxError: Loop statement must end with colon."

    # loop i = 0 to (i ++):
    elif "<LOOP><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><INTEGER><WHITESPACE><TO><WHITESPACE><PARENTHESIS_OPEN>" in token:
        return "SyntaxError: Missing loop limit value"

    # e.g. loop i = 1 10 (i ++):
    elif "<LOOP><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><INTEGER><WHITESPACE><INTEGER>" in token:
        return "SyntaxError: 'to' keyword missing"

    # e.g. loop i = to 10 (i ++):
    elif "<LOOP><WHITESPACE><INTEGER><WHITESPACE><TO><WHITESPACE><INTEGER>" in token:
        return "SyntaxError: Missing loop variable initialization"

    # e.g. loop 1 to 5 (i ++):
    elif "<LOOP><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP>" in token:
        return "SyntaxError: Missing loop variable initialization"

    # e.g int ++
    elif "<DT_INT><WHITESPACE><INCREMENT>" in token or "<DT_INT><WHITESPACE><DECEREMENT>" in token:
        return "SyntaxError: Identifier or Integer required"

    # e.g ++
    elif token == "<INCREMENT>" or token == "<DECREMENT>":
        return "SyntaxError: Identifier or Integer required"

    # e.g AND z
    elif any(token.startswith(op) and ("<WHITESPACE><IDENTIFIER>" in token) for op in LOGICAL_OPERATORS):
        return "SyntaxError: Identifier required"

    # e.g TRUE OR
    elif "<BOOL_VALUE><WHITESPACE>" in token and (
            "<LOGICAL_NOT>" in token or "<LOGICAL_OR>" in token or "<LOGICAL_AND>" in token):
        return "SyntaxError: Boolean value required"

    # e.g ! FALSE
    elif ("<LOGICAL_NOT>" in token or "<LOGICAL_OR>" in token or "<LOGICAL_AND>" in token) and "<WHITESPACE><BOOL_VALUE>" in token:
        return "SyntaxError: Boolean value required"

    # e.g !
    elif token == "<LOGICAL_NOT>":
        return "SyntaxError: Identifier required"

    # e.g - 3
    elif any(operator in token for operator in ARITHMETIC_OPS) and "<WHITESPACE>" in token and ("INTEGER" in token or "DECIMAL" in token):
        return "SyntaxError: Missing operand"

    elif ("INTEGER" in token or "DECIMAL" in token) and "<WHITESPACE>" in token and any(operator in token for operator in ARITHMETIC_OPS) and ("INTEGER" in token or "DECIMAL" in token):
        return "SyntaxError: Missing operand"

    # errors for conditional statement
    elif ('<WHEN>' in token or '<OTHERWISE><WHITESPACE><WHEN>' in token) and ('<PARENTHESIS_OPEN>' not in token and '<PARENTHESIS_CLOSE>' not in token):
        return "SyntaxError: Opening and closing parenthesis required"

    elif ('<WHEN>' in token or '<OTHERWISE><WHITESPACE><WHEN>' in token) and ('<PARENTHESIS_OPEN>' not in token):
        return "SyntaxError: Opening parenthesis required"

    elif ('<WHEN>' in token or '<OTHERWISE><WHITESPACE><WHEN>' in token) and ('<PARENTHESIS_CLOSE>' not in token):
        return "SyntaxError: Closing parenthesis required"

    elif ('<WHEN>' in token or '<OTHERWISE><WHITESPACE><WHEN>' in token) and '<PARENTHESIS_CLOSE>' in token and '<PARENTHESIS_OPEN>' in token and any(prefix not in token for prefix in BOOLEAN_RELATION):
        return "SyntaxError: Invalid condition"

    elif any(token.startswith(prefix + '<WHITESPACE><PARENTHESIS_OPEN>') for prefix in CONDITIONALS):
        return "SyntaxError: Whitespace not required before opening parenthesis"

    elif (token.startswith('<WHEN>') or token.startswith('<OTHERWISE><WHITESPACE><WHEN>') or token.startswith('<OTHERWISE>')) and not token.endswith('<COLON_DELIMITER>'):
        return "SyntaxError: Colon after conditional statement required"

    elif token.startswith('<WHEN>') or token.startswith('<OTHERWISE><WHITESPACE><WHEN>') or token.startswith('<OTHERWISE>') and token.endswith('<WHITESPACE><COLON_DELIMITER>'):
        return "SyntaxError: Whitespace before colon not required"

    elif token.startswith('<WHEN>') or token.startswith('<OTHERWISE><WHITESPACE><WHEN>') or token.startswith('<OTHERWISE>') and '<PARENTHESIS_OPEN><PARENTHESIS_CLOSE>' in token:
        return "SyntaxError: Condition required inside the parentheses"

    elif token == "<OTHERWISE>" or token == "<OTHERWISE><WHITESPACE>":
        return "SyntaxError: Colon after otherwise required"

    # errors for new principles
    elif any(principle in token for principle in NEW_PRINCIPLES) and "<INTEGER>" not in token and "<IDENTIFIER>" not in token and '<PARENTHESIS_OPEN><PARENTHESIS_CLOSE>' in token:
        return "ValueError: Integer or Identifier Required"

    elif any(token.startswith(prefix + '<WHITESPACE>') for prefix in NEW_PRINCIPLES):
        return "SyntaxError: Whitespace not required before opening parenthesis"

    elif any(principle in token for principle in NEW_PRINCIPLES) and ('<PARENTHESIS_OPEN>' not in token or '<PARENTHESIS_CLOSE>' not in token):
        return "SyntaxError: Opening and closing parenthesis required"

    elif any(principle in token for principle in NEW_PRINCIPLES) and ('<PARENTHESIS_OPEN>' not in token and '<PARENTHESIS_CLOSE>' in token):
        return "SyntaxError: Opening parenthesis required"

    elif any(principle in token for principle in NEW_PRINCIPLES) and ('<PARENTHESIS_OPEN>' in token and '<PARENTHESIS_CLOSE>' not in token):
        return "SyntaxError: Closing parenthesis required"

    # e.g. arithSeq(1, 2)
    elif ('<ARITHSEQ>' in token or '<ARITHSER>' in token or '<GEOSEQ>' in token or '<GEOSER>' in token or '<QUADRATIC>' in token or '<SLOPE>' in token) and (token.count("<INTEGER>") != 3 and (token.count("<IDENTIFIER>") != 3 or token.count("<IDENTIFIER>") != 4)):
        return "SyntaxError: Expected 3 parameters"

    # e.g. power(1, 2, 3)
    elif ('<PYTHAGOREAN>' in token or '<QUADRATIC>' in token or '<FORCE>' in token or '<WORK>' in token or '<POWER>' in token or '<MOMENTUM>' in token or '<KINETIC>' in token or '<POTENTIAL>' in token) and (token.count("<INTEGER>") != 2 and (token.count("<IDENTIFIER>") != 3 or token.count("<IDENTIFIER>") != 2)):
        return "SyntaxError: Expected 2 parameters"

    # e.g. acceleration(1, 2, 3)
    elif ('<ACCELERATION>' in token or '<DISTANCE>' in token) and (token.count("<INTEGER>") != 4 and (token.count("<IDENTIFIER>") != 4 or token.count("<IDENTIFIER>") != 5)):
        return "SyntaxError: Expected 4 parameters"

    elif ('<ARITHSEQ>' in token or '<ARITHSER>' in token or '<GEOSEQ>' in token or '<GEOSER>' in token or '<QUADRATIC>' in token or '<SLOPE>' in token) and (token.count("<INTEGER>") == 3 or (token.count("<IDENTIFIER>") == 3 or token.count("<IDENTIFIER>") == 2)) and (token.count("<COMMA>") != 2):
        return "SyntaxError: Parameters must be separated by comma"

    elif ('<PYTHAGOREAN>' in token or '<QUADRATIC>' in token or '<FORCE>' in token or '<WORK>' in token or '<POWER>' in token or '<MOMENTUM>' in token or '<KINETIC>' in token or '<POTENTIAL>' in token) and (token.count("<INTEGER>") != 2 or token.count("<IDENTIFIER>") != 2 or token.count("<IDENTIFIER>") != 3) and (token.count("<COMMA>") != 1):
        return "SyntaxError: Parameters must be separated by comma"

    elif ('<ACCELERATION>' in token or '<DISTANCE>' in token) and ((token.count("<INTEGER>") == 4) or (token.count("<IDENTIFIER>") != 4) or (token.count("<IDENTIFIER>") != 5)) and (token.count("<COMMA>") != 3):
        return "SyntaxError: Parameters must be separated by comma"

    elif '<INVALID_TOKEN>' in token:
        return 'Invalid token found'

    else:
        return 'Syntax Error'
