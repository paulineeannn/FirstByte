DATA_TYPES = ["<DT_INT>", "<DT_DECI>", "<DT_STR>", "<DT_CHAR>", "<DT_BOOL>"]
DATA_VALUES = ["<INTEGER>", "<DECIMAL>", "<STRING>", "<CHAR>", "<BOOL_VALUE>"]
ARITHMETIC_OPS = ["<PLUS>", "<MINUS>", "<MULTIPLY>", "<DIVIDE>"]
ASSIGNMENT_OPS = ["<ADD_ASS>", "<SUBTRACT_ASS>", "<MULTIPLY_ASS>", "<DIVIDE_ASS>", "<MODULO_ASS>"]
SPECIAL_CHARS = ['<PERIOD>', '<POUND>', '<SEMICOLON>', '<PIPE>', '<BACKSLASH>', '<UNDERSCORE>', '<TILDE>', '<AMPERSAND>']

DECLARATION_STMT = []
for dt in DATA_TYPES:
    DECLARATION_STMT.append(f"{dt}<WHITESPACE><IDENTIFIER>")

MULTI_DECLARATION_STMT = []

# generate production rule for multiple variable declaration
for num_variables in range(1, 20):  # can declare maximum of 20 variables in one line only
    for line in DECLARATION_STMT:
        token = '<COMMA><WHITESPACE><IDENTIFIER>' * num_variables
        MULTI_DECLARATION_STMT.append(f"{line}{token}")

# append production rules for multiple variable declaration in DECLARATION_STMT
DECLARATION_STMT = DECLARATION_STMT + MULTI_DECLARATION_STMT

#
ASSIGNMENT_STMT = [
    "<DT_INT><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><IDENTIFIER>",     # int age = x
    "<DT_DECI><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><IDENTIFIER>",    # deci gpa = y
    "<DT_STR><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><IDENTIFIER>",     # str y = z
    "<DT_CHAR><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><IDENTIFIER>",    # char z = y
    "<DT_BOOL><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><IDENTIFIER>",    # bool s = h
    "<DT_DECI><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><CONSTANT>",      # deci value_pi = pi
]

ASSIGNMENT_OPERATORS = []
for x in range(len(DATA_TYPES)):
    token = f"{DATA_TYPES[x]}<WHITESPACE><IDENTIFIER><WHITESPACE>{ASSIGNMENT_OPS[x]}<WHITESPACE><IDENTIFIER>"
    ASSIGNMENT_OPERATORS.append(token)

ARITHMETIC_EXP = []
for num in range(1, 10):
    for x in range(len(DATA_VALUES)):
        addition = f"{DATA_VALUES[x]}<WHITESPACE><PLUS><WHITESPACE>{DATA_VALUES[x]}" * num
        subtraction = f"{DATA_VALUES[x]}<WHITESPACE><MINUS><WHITESPACE>{DATA_VALUES[x]}" * num
        division = f"{DATA_VALUES[x]}<WHITESPACE><DIVIDE><WHITESPACE>{DATA_VALUES[x]}" * num
        multiplication = f"{DATA_VALUES[x]}<WHITESPACE><MULTIPLY><WHITESPACE>{DATA_VALUES[x]}" * num

        ARITHMETIC_EXP.append(addition)
        ARITHMETIC_EXP.append(subtraction)
        ARITHMETIC_EXP.append(division)
        ARITHMETIC_EXP.append(multiplication)

# int x = 10
ASSIGNMENT_IDENVALUE = []
for i in range(len(DATA_TYPES)):
    ASSIGNMENT_IDENVALUE.append(
        f"{DATA_TYPES[i]}<WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE>{DATA_VALUES[i]}")

MULTI_ASSIGNMENT_IDENVALUE = []
for num in range(1, 15):
    for i in range(len(DATA_TYPES)):
        token = f"<COMMA><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE>{DATA_VALUES[i]}" * num
        MULTI_ASSIGNMENT_IDENVALUE.append(f"{ASSIGNMENT_IDENVALUE[i]}{token}")

# int x = 1 + 1

ASSIGNMENT_EXP = []
for num in range(1, 15):
    for value, dt in zip(DATA_VALUES, DATA_TYPES):
        for operator in ARITHMETIC_OPS:
            arithmetic_expression = f"{dt}<WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE>{value}<WHITESPACE>{operator}<WHITESPACE>{value}" * num
            ASSIGNMENT_EXP.append(arithmetic_expression)

MULTI_ASSIGNMENT_EXP = []
for num in range(1, 15):
    for i in range(len(DATA_TYPES)):
        token = f"<COMMA><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE>{ARITHMETIC_EXP[i]}" * num
        MULTI_ASSIGNMENT_EXP.append(f"{ASSIGNMENT_EXP[i]}{token}")

VALID_ASSIGN = ASSIGNMENT_OPERATORS + ASSIGNMENT_IDENVALUE + MULTI_ASSIGNMENT_IDENVALUE + ASSIGNMENT_EXP + MULTI_ASSIGNMENT_EXP

for x in VALID_ASSIGN:
    ASSIGNMENT_STMT.append(x)

INPUT_STMT = [
    "<DT_STR><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><INPUT><PARENTHESIS_OPEN><PARENTHESIS_CLOSE>",
    "<DT_INT><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><INPUT><PARENTHESIS_OPEN><PARENTHESIS_CLOSE>",
    "<DT_DECI><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><INPUT><PARENTHESIS_OPEN><PARENTHESIS_CLOSE>",
    "<DT_CHAR><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><INPUT><PARENTHESIS_OPEN><PARENTHESIS_CLOSE>",
]

OUTPUT_STMT = [
    # e.g. output("hello")
    "<OUTPUT><PARENTHESIS_OPEN><STRING><PARENTHESIS_CLOSE>",
    "<OUTPUT><PARENTHESIS_OPEN><IDENTIFIER><PARENTHESIS_CLOSE>",
    "<OUTPUT><PARENTHESIS_OPEN><STRING><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<OUTPUT><PARENTHESIS_OPEN><STRING><PARENTHESIS_CLOSE><WHITESPACE>",
    "<OUTPUT><PARENTHESIS_OPEN><IDENTIFIER><PARENTHESIS_CLOSE><WHITESPACE>",
    "<OUTPUT><PARENTHESIS_OPEN><STRING><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE><WHITESPACE>",

    "<OUTPUT><PARENTHESIS_OPEN><STRING><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",
    "<OUTPUT><PARENTHESIS_OPEN><STRING><WHITESPACE><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",
    "<OUTPUT><PARENTHESIS_OPEN><IDENTIFIER><PARENTHESIS_CLOSE>",
    "<OUTPUT><PARENTHESIS_OPEN><STRING><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>"
]

ARITHMETIC_OPERATOR = [
    "<IDENTIFIER><WHITESPACE><PLUS><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><WHITESPACE><MINUS><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><WHITESPACE><MULTIPLY><WHITESPACE><IDENTIFIER>",
     "<IDENTIFIER><WHITESPACE><DIVIDE><WHITESPACE><IDENTIFIER>",
    ARITHMETIC_EXP
]

UNARY_OPERATOR = [
    # with data type
    "<DT_INT><WHITESPACE><INCREMENT><WHITESPACE><IDENTIFIER>",
    "<DT_INT><WHITESPACE><DECREMENT><WHITESPACE><IDENTIFIER>",
    "<DT_INT><WHITESPACE><IDENTIFIER><WHITESPACE><INCREMENT>",
    "<DT_INT><WHITESPACE><IDENTIFIER><WHITESPACE><DECREMENT>",

    "<DT_INT><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><PLUS><WHITESPACE><INTEGER>",
    "<DT_INT><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><MINUS><WHITESPACE><INTEGER>",

    # identifiers without data type e.g. ++ age
    "<INCREMENT><WHITESPACE><IDENTIFIER>",
    "<DECREMENT><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><WHITESPACE><INCREMENT>",
    "<IDENTIFIER><WHITESPACE><DECREMENT>",

    # numbers without data type e.g. ++ 10
    "<INCREMENT><WHITESPACE><INTEGER>",
    "<DECREMENT><WHITESPACE><INTEGER>",
    "<INTEGER><WHITESPACE><INCREMENT>",
    "<INTEGER><WHITESPACE><DECREMENT>",
]

BOOLEAN_LOGIC = [
    # e.g. ! x
    "<LOGICAL_NOT><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><WHITESPACE><LOGICAL_OR><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><WHITESPACE><LOGICAL_AND><WHITESPACE><IDENTIFIER>",

    "<BOOL_VALUE><WHITESPACE><LOGICAL_NOT><WHITESPACE><BOOL_VALUE>",
    "<BOOL_VALUE><WHITESPACE><LOGICAL_OR><WHITESPACE><BOOL_VALUE>",
    "<BOOL_VALUE><WHITESPACE><LOGICAL_AND><WHITESPACE><BOOL_VALUE>",
    "BOOL_VALUE"
]

BOOLEAN_RELATION = [
    # e.g. x <= y
    "<IDENTIFIER><WHITESPACE><EQUAL_TO><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><WHITESPACE><NOT_EQUAL><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><WHITESPACE><GREATER_THAN><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><WHITESPACE><LESS_THAN><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><WHITESPACE><GREATER_THAN_EQ><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><WHITESPACE><LESS_THAN_EQ><WHITESPACE><IDENTIFIER>",

    # e.g. x <= 12
    "<IDENTIFIER><WHITESPACE><EQUAL_TO><WHITESPACE><INTEGER>",
    "<IDENTIFIER><WHITESPACE><NOT_EQUAL><WHITESPACE><INTEGER>",
    "<IDENTIFIER><WHITESPACE><GREATER_THAN><WHITESPACE><INTEGER>",
    "<IDENTIFIER><WHITESPACE><LESS_THAN><WHITESPACE><INTEGER>",
    "<IDENTIFIER><WHITESPACE><GREATER_THAN_EQ><WHITESPACE><INTEGER>",
    "<IDENTIFIER><WHITESPACE><LESS_THAN_EQ><WHITESPACE><INTEGER>",

    # e.g. x <= 12.34
    "<IDENTIFIER><WHITESPACE><EQUAL_TO><WHITESPACE><DECIMAL>",
    "<IDENTIFIER><WHITESPACE><NOT_EQUAL><WHITESPACE><DECIMAL>",
    "<IDENTIFIER><WHITESPACE><GREATER_THAN><WHITESPACE><DECIMAL>",
    "<IDENTIFIER><WHITESPACE><LESS_THAN><WHITESPACE><DECIMAL>",
    "<IDENTIFIER><WHITESPACE><GREATER_THAN_EQ><WHITESPACE><DECIMAL>",
    "<IDENTIFIER><WHITESPACE><LESS_THAN_EQ><WHITESPACE><DECIMAL>",

    # e.g. x <= "SDASD"
    "<IDENTIFIER><WHITESPACE><EQUAL_TO><WHITESPACE><STRING>",
    "<IDENTIFIER><WHITESPACE><NOT_EQUAL><WHITESPACE><STRING>",
    "<IDENTIFIER><WHITESPACE><GREATER_THAN><WHITESPACE><STRING>",
    "<IDENTIFIER><WHITESPACE><LESS_THAN><WHITESPACE><STRING>",
    "<IDENTIFIER><WHITESPACE><GREATER_THAN_EQ><WHITESPACE><STRING>",
    "<IDENTIFIER><WHITESPACE><LESS_THAN_EQ><WHITESPACE><STRING>",

    # e.g. x <= 12
    "<IDENTIFIER><WHITESPACE><EQUAL_TO><WHITESPACE><CHAR>",
    "<IDENTIFIER><WHITESPACE><NOT_EQUAL><WHITESPACE><CHAR>",
    "<IDENTIFIER><WHITESPACE><GREATER_THAN><WHITESPACE><CHAR>",
    "<IDENTIFIER><WHITESPACE><LESS_THAN><WHITESPACE><CHAR>",
    "<IDENTIFIER><WHITESPACE><GREATER_THAN_EQ><WHITESPACE><CHAR>",
    "<IDENTIFIER><WHITESPACE><LESS_THAN_EQ><WHITESPACE><CHAR>",

    # e.g. x <= "SDASD"
    "<IDENTIFIER><WHITESPACE><EQUAL_TO><WHITESPACE><BOOL_VALUE>",
    "<IDENTIFIER><WHITESPACE><NOT_EQUAL><WHITESPACE><BOOL_VALUE>",
    "<IDENTIFIER><WHITESPACE><GREATER_THAN><WHITESPACE><BOOL_VALUE>",
    "<IDENTIFIER><WHITESPACE><LESS_THAN><WHITESPACE><BOOL_VALUE>",
    "<IDENTIFIER><WHITESPACE><GREATER_THAN_EQ><WHITESPACE><BOOL_VALUE>",
    "<IDENTIFIER><WHITESPACE><LESS_THAN_EQ><WHITESPACE><BOOL_VALUE>",

    # e.g. 12 < X
    "<IDENTIFIER><INTEGER><EQUAL_TO><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><INTEGER><NOT_EQUAL><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><INTEGER><GREATER_THAN><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><INTEGER><LESS_THAN><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><INTEGER><GREATER_THAN_EQ><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><INTEGER><LESS_THAN_EQ><WHITESPACE><IDENTIFIER>",

    # e.g. 12.5 < X
    "<IDENTIFIER><DECIMAL><EQUAL_TO><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><DECIMAL><NOT_EQUAL><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><DECIMAL><GREATER_THAN><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><DECIMAL><LESS_THAN><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><DECIMAL><GREATER_THAN_EQ><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><DECIMAL><LESS_THAN_EQ><WHITESPACE><IDENTIFIER>",

    # e.g. 12.5 < X
    "<IDENTIFIER><STRING><EQUAL_TO><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><STRING><NOT_EQUAL><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><STRING><GREATER_THAN><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><STRING><LESS_THAN><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><STRING><GREATER_THAN_EQ><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><STRING><LESS_THAN_EQ><WHITESPACE><IDENTIFIER>",

    # e.g. "SFDFS" < X
    "<IDENTIFIER><CHAR><EQUAL_TO><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><CHAR><NOT_EQUAL><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><CHAR><GREATER_THAN><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><CHAR><LESS_THAN><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><CHAR><GREATER_THAN_EQ><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><CHAR><LESS_THAN_EQ><WHITESPACE><IDENTIFIER>",

    # e.g. TRUE < X
    "<IDENTIFIER><BOOL_VALUE><EQUAL_TO><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><BOOL_VALUE><NOT_EQUAL><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><BOOL_VALUE><GREATER_THAN><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><BOOL_VALUE><LESS_THAN><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><BOOL_VALUE><GREATER_THAN_EQ><WHITESPACE><IDENTIFIER>",
    "<IDENTIFIER><BOOL_VALUE><LESS_THAN_EQ><WHITESPACE><IDENTIFIER>",

    # 12 >= 13
    "<INTEGER><WHITESPACE><EQUAL_TO><WHITESPACE><INTEGER>",
    "<INTEGER><WHITESPACE><NOT_EQUAL><WHITESPACE><INTEGER>",
    "<INTEGER><WHITESPACE><GREATER_THAN><WHITESPACE><INTEGER>",
    "<INTEGER><WHITESPACE><LESS_THAN><WHITESPACE><INTEGER>",
    "<INTEGER><WHITESPACE><GREATER_THAN_EQ><WHITESPACE><INTEGER>",
    "<INTEGER><WHITESPACE><LESS_THAN_EQ><WHITESPACE><INTEGER>",

    # 12.312 <= 12.231
    "<DECIMAL><WHITESPACE><EQUAL_TO><WHITESPACE><DECIMAL>",
    "<DECIMAL><WHITESPACE><NOT_EQUAL><WHITESPACE><DECIMAL>",
    "<DECIMAL><WHITESPACE><GREATER_THAN><WHITESPACE><DECIMAL>",
    "<DECIMAL><WHITESPACE><LESS_THAN><WHITESPACE><DECIMAL>",
    "<DECIMAL><WHITESPACE><GREATER_THAN_EQ><WHITESPACE><DECIMAL>",
    "<DECIMAL><WHITESPACE><LESS_THAN_EQ><WHITESPACE><DECIMAL>",

    # TRUE == FALSE
    "<BOOL_VALUE><WHITESPACE><EQUAL_TO><WHITESPACE><BOOL_VALUE>",
    "<BOOL_VALUE><WHITESPACE><NOT_EQUAL><WHITESPACE><BOOL_VALUE>",
    "<BOOL_VALUE><WHITESPACE><GREATER_THAN><WHITESPACE><BOOL_VALUE>",
    "<BOOL_VALUE><WHITESPACE><LESS_THAN><WHITESPACE><BOOL_VALUE>",
    "<BOOL_VALUE><WHITESPACE><GREATER_THAN_EQ><WHITESPACE><BOOL_VALUE>",
    "<BOOL_VALUE><WHITESPACE><LESS_THAN_EQ><WHITESPACE><BOOL_VALUE>",

    # "TEST" >= "TASTY"
    "<STRING><WHITESPACE><EQUAL_TO><WHITESPACE><STRING>",
    "<STRING><WHITESPACE><NOT_EQUAL><WHITESPACE><STRING>",
    "<STRING><WHITESPACE><GREATER_THAN><WHITESPACE><STRING>",
    "<STRING><WHITESPACE><LESS_THAN><WHITESPACE><STRING>",
    "<STRING><WHITESPACE><GREATER_THAN_EQ><WHITESPACE><STRING>",
    "<STRING><WHITESPACE><LESS_THAN_EQ><WHITESPACE><STRING>",
]

# e.g. x > y AMD u <= z
for x in BOOLEAN_RELATION:
    for y in BOOLEAN_RELATION:
        BOOLEAN_LOGIC.append(f"{x}<WHITESPACE><LOGICAL_NOT><WHITESPACE>{y}")
        BOOLEAN_LOGIC.append(f"{x}<WHITESPACE><LOGICAL_OR><WHITESPACE>{y}")
        BOOLEAN_LOGIC.append(f"{x}<WHITESPACE><LOGICAL_AND><WHITESPACE>{y}")

# e.g. x + y == x - y
for x in ARITHMETIC_OPERATOR:
    for y in ARITHMETIC_OPERATOR:
        BOOLEAN_RELATION.append(f"{x}<WHITESPACE><EQUAL_TO><WHITESPACE>{y}")
        BOOLEAN_RELATION.append(f"{x}<WHITESPACE><NOT_EQUAL><WHITESPACE>{y}")
        BOOLEAN_RELATION.append(f"{x}<WHITESPACE><GREATER_THAN><WHITESPACE>{y}")
        BOOLEAN_RELATION.append(f"{x}<WHITESPACE><LESS_THAN><WHITESPACE>{y}")
        BOOLEAN_RELATION.append(f"{x}<WHITESPACE><GREATER_THAN_EQ><WHITESPACE>{y}")
        BOOLEAN_RELATION.append(f"{x}<WHITESPACE><LESS_THAN_EQ><WHITESPACE>{y}")

CONDITIONAL_STMT = [
    "<OTHERWISE><COLON_DELIMITER>",
    "<OTHERWISE><COLON_DELIMITER><WHITESPACE>",
    "<INVALID_TOKEN><OTHERWISE><COLON_DELIMITER>",
    "<INVALID_TOKEN><OTHERWISE><COLON_DELIMITER><WHITESPACE>"
]

NEW_PRINCIPLES = [
    "<ARITHSEQ><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE><INTEGER><COMMA><WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<ARITHSEQ><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<ARITHSER><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE><INTEGER><COMMA><WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<ARITHSER><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<GEOSEQ><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE><INTEGER><COMMA><WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<GEOSEQ><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<GEOSER><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE> <INTEGER><COMMA> <WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<GEOSER><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<DISTANCE><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE><INTEGER><COMMA><WHITESPACE><INTEGER><COMMA><WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<DISTANCE><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<SLOPE><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE><INTEGER><COMMA><WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<SLOPE><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<PYTHAGOREAN><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<PYTHAGOREAN><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<QUADRATIC><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE><INTEGER><COMMA><WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<QUADRATIC><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<FORCE><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<FORCE><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<WORK><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<WORK><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<ACCELERATION><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE><INTEGER><COMMA><WHITESPACE><INTEGER><COMMA><WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<ACCELERATION><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<POWER><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<POWER><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<MOMENTUM><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<MOMENTUM><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<POTENTIAL><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<POTENTIAL><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<KINETIC><PARENTHESIS_OPEN><INTEGER><COMMA><WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<KINETIC><PARENTHESIS_OPEN><IDENTIFIER><COMMA><WHITESPACE><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<TOINT><PARENTHESIS_OPEN><DIGIT><WHITESPACE>+<WHITESPACE><INTEGER><PARENTHESIS_CLOSE>",
    "<TOINT><PARENTHESIS_OPEN><DIGIT><PARENTHESIS_CLOSE>",
    "<TOINT><PARENTHESIS_OPEN><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<TODECI><PARENTHESIS_OPEN><INTEGER><PARENTHESIS_CLOSE>",
    "<TODECI><PARENTHESIS_OPEN><IDENTIFIER><PARENTHESIS_CLOSE>",

    "<TOSTR><PARENTHESIS_OPEN><INTEGER><PARENTHESIS_CLOSE>",
    "<TOSTR><PARENTHESIS_OPEN><DECIMAL><PARENTHESIS_CLOSE>",
    "<TOSTR><PARENTHESIS_OPEN><IDENTIFIER><PARENTHESIS_CLOSE>"
]

# assigning new principles to variables
for principle in NEW_PRINCIPLES:
    ASSIGNMENT_STMT.append(f"<DT_INT><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE>{principle}")
    ASSIGNMENT_STMT.append(f"<DT_DECI><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE>{principle}")
    OUTPUT_STMT.append(f"<OUTPUT><PARENTHESIS_OPEN>{principle}<PARENTHESIS_CLOSE>")

for condition in BOOLEAN_RELATION:
    CONDITIONAL_STMT.append(f"<WHEN><PARENTHESIS_OPEN>{condition}<PARENTHESIS_CLOSE><COLON_DELIMITER>")
    CONDITIONAL_STMT.append(
        f"<OTHERWISE><WHITESPACE><WHEN><PARENTHESIS_OPEN>{condition}<PARENTHESIS_CLOSE><COLON_DELIMITER>")

for condition in BOOLEAN_LOGIC:
    CONDITIONAL_STMT.append(f"<WHEN><PARENTHESIS_OPEN>{condition}<PARENTHESIS_CLOSE><COLON_DELIMITER>")
    CONDITIONAL_STMT.append(
        f"<OTHERWISE><WHITESPACE><WHEN><PARENTHESIS_OPEN>{condition}<PARENTHESIS_CLOSE><COLON_DELIMITER>")

ITERATIVE_STMT = [
    # e.g. loop i = 1 to 10 (i ++):
    "<LOOP><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><INTEGER><WHITESPACE><TO><WHITESPACE><INTEGER><WHITESPACE><PARENTHESIS_OPEN><IDENTIFIER><WHITESPACE><INCREMENT><PARENTHESIS_CLOSE><COLON_DELIMITER>",
    "<LOOP><WHITESPACE><IDENTIFIER><WHITESPACE><ASS_OP><WHITESPACE><INTEGER><WHITESPACE><TO><WHITESPACE><INTEGER><WHITESPACE><PARENTHESIS_OPEN><IDENTIFIER><WHITESPACE><DECREMENT><PARENTHESIS_CLOSE><COLON_DELIMITER>"
]

BODY_STMT = []
COMMENT_STMT = [
    "<COMMENT_MULTI>",
    "<COMMENT_SYM_MULTI><COMMENT_MULTI><CHAR_COMMENT_SYM_MULTI>",
    "<CHAR_COMMENT_SYM_SINGLE><COMMENT_SINGLE>"
]

STATEMENTS_LIST = [DECLARATION_STMT, ASSIGNMENT_STMT, INPUT_STMT, OUTPUT_STMT, ARITHMETIC_OPERATOR, UNARY_OPERATOR,
                   BOOLEAN_LOGIC, BOOLEAN_RELATION, CONDITIONAL_STMT, NEW_PRINCIPLES, ITERATIVE_STMT, BODY_STMT]
combined_list = sum(STATEMENTS_LIST, [])

# accept indented
for x in combined_list:
    indented = f"<WHITESPACE><WHITESPACE><WHITESPACE><WHITESPACE><WHITESPACE><WHITESPACE><WHITESPACE><WHITESPACE>{x}"
    BODY_STMT.append(indented)

    indented = f"<WHITESPACE><INDENT>{x}"
    BODY_STMT.append(indented)

    indented = f"<INDENT>{x}"
    BODY_STMT.append(indented)

    indented = f"<INDENT2>{x}"
    BODY_STMT.append(indented)

    indented = f"<INDENT><INDENT>{x}"
    BODY_STMT.append(indented)

    indented = f"<INDENT2><INDENT2>{x}"
    BODY_STMT.append(indented)

    indented = f"<INDENT><INDENT><INDENT>{x}"
    BODY_STMT.append(indented)

    indented = f"<INDENT2><INDENT2><INDENT2>{x}"
    BODY_STMT.append(indented)

# handle line of codes that have whitespace/indent in the end of line
for x in combined_list:
    excess_space = f"{x}<INDENT>"
    BODY_STMT.append(excess_space)

    excess_space = f"{x}<WHITESPACE>"
    BODY_STMT.append(excess_space)

    excess_space = f"<WHITESPACE><WHITESPACE>{x}"
    BODY_STMT.append(excess_space)

    excess_space = f"<WHITESPACE><WHITESPACE><WHITESPACE>{x}"
    BODY_STMT.append(excess_space)

for x in combined_list:
    comment_s = f"{x}<WHITESPACE><CHAR_COMMENT_SYM_SINGLE><COMMENT_SINGLE>"
    comment_m = f"{x}<WHITESPACE><CHAR_COMMENT_SYM_MULTI><COMMENT_MULTI>"
    COMMENT_STMT.append(comment_s)
    COMMENT_STMT.append(comment_m)

STATEMENTS_LIST = [DECLARATION_STMT, MULTI_DECLARATION_STMT, ASSIGNMENT_STMT, INPUT_STMT, OUTPUT_STMT,
                   ARITHMETIC_OPERATOR, UNARY_OPERATOR, BOOLEAN_LOGIC, BOOLEAN_RELATION, CONDITIONAL_STMT,
                   NEW_PRINCIPLES, ITERATIVE_STMT, BODY_STMT, COMMENT_STMT]
