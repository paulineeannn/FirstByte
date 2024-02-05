
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

digits = '0123456789'

special_chars = {
    "." : "PERIOD",
    "@" : "COMMENT_SYM_SINGLE",
    "@@" : "COMMENT_SYM_MULTI",
    "'" : "SINGLE_QUOTE",
    "#" : "POUND",
    "," : "COMMA",
    ";" : "SEMICOLON",
    "|" : "PIPE",
    "\\" : "BACKSLASH",
    "_" : "UNDERSCORE",
    "~" : "TILDE",
    "&" : "AMPERSAND"
}

delimiters = {
    ":": "COLON_DELIMITER",
    "(": "PARENTHESIS_OPEN",
    ")": "PARENTHESIS_CLOSE",
    "[": "BRACKET_OPEN",
    "]": "BRACKET_CLOSE",
    "{": "BRACE_OPEN",
    "}": "BRACE_CLOSE",
}

operators= {
    "=": "EQUAL",
    "+=" : "ADD_ASS",
    "-=" : "SUBTRACT_ASS",
    "*=" : "MULTIPLY_ASS",
    "/=" : "DIVIDE_ASS",
    "%=" : "MODULO_ASS",
    "++" : "INCREMENT", # unary
    "--" : "DECREMENT", # unary
    "+": "PLUS",    # arithmetic op
    "-": "MINUS",   # arithmetic op
    "*": "MULTIPLY",    # arithmetic op
    "/": "DIVIDE",  # arithmetic op
    "%": "MODULO",
    "^": "EXPONENT",
    "!": "LOGICAL_NOT",
    "OR": "LOGICAL_OR",
    "AND": "LOGICAL_AND",
    "==": "EQUAL_TO",
    "!=": "NOT_EQUAL",
    ">" : "GREATER_THAN",
    "<" : "LESS_THAN",
    ">=" : "GREATER_THAN_EQUAL",
    "<=" : "LESS_THAN_EQUAL",
}

# binary_ops = {
#     "=": "EQUAL",
#     "+=": "ADD_ASS",
#     "-=": "SUBTRACT_ASS",
#     "*=": "MULTIPLY_ASS",
#     "/=": "DIVIDE_ASS",
#     "%=": "MODULO_ASS",
#     "+": "PLUS",
#     "-": "MINUS",
#     "*": "MULTIPLY",
#     "/": "DIVIDE",
#     "%": "MODULO",
#     "^": "EXPONENT",
#     "==": "EQUAL_TO",
#     "!=": "NOT_EQUAL",
#     ">": "GREATER_THAN",
#     "<": "LESS_THAN",
#     ">=": "GREATER_THAN_EQUAL",
#     "<=": "LESS_THAN_EQUAL",
# }
#
# logical_ops = {
#     "!": "LOGICAL_NOT",
#     "OR": "LOGICAL_OR",
#     "AND": "LOGICAL_AND",
# }
#
# unary_ops = {
#     "!": "LOGICAL_NOT",
#     "++": "INCREMENT",
#     "--": "DECREMENT",
# }

keywords = {
    "def" : "DEF",
    "when" : "WHEN",
    "otherwise" : "OTHERWISE",
    "loop" : "LOOP",
    "to" : "TO",
    "input" : "INPUT",
    "output" : "OUTPUT",
    "stop" : "STOP",
    "jump" : "JUMP",
    "arithSeq" : "ARITHSEQ",
    "arithSer" : "ARITHSER",
    "geoSeq" : "GEOSEQ",
    "geoSer" : "GEOSER",
    "distance" : "DISTANCE",
    "slope" : "SLOPE",
    "pythagorean" : "PYTHAGOREAN",
    "quadratic" : "QUADRATIC",
    "force" : "FORCE",
    "work" : "WORK",
    "acceleration" : "ACCELERATION",
    "power" : "POWER",
    "momentum" : "MOMENTUM",
    "potential" : "POTENTIAL",
    "kinetic" : "KINETIC",
    "toInt" : "TOINT",
    "toDeci" : "TODECI",
    "toStr" : "TOSTR"
}

reserved_words = {
    "TRUE" : "BOOL_VALUE",
    "FALSE" : "BOOL_VALUE",
    "main" : "MAIN",
    "cont" : "CONT"
}

data_type = {
    "int" : "DT_INT",
    "str" : "DT_STR",
    "char" : "DT_CHAR",
    "deci" : "DT_DECI",
    "bool" : "DT_BOOL"
}

noise_words = {
    "ean",
    "eger",
    "mal",
    "ing",
    "acter",
    "ault",
    "inue"
}

full_words = {
    "boolean",
    "integer",
    "decimal",
    "string",
    "character",
    "default",
    "continue"
}

constants = {
    "pi" : "PI",
    "accGrav" : "ACCGRAV",
    "euler" : "EULER",
    "goldenRatio" : "GOLDENRATIO"
}

spaces = {' ' : "WHITESPACE",
          '\n' : "NEWLINE",
          '/t' : "INDENT",
          '        ' : "INDENT2",
}

# ALL_TOKENS = {
#     'alphabet': alphabet,
#     'digits': digits,
#     'special_chars': special_chars,
#     'delimiters': delimiters,
#     'operators': operators,
#     'keywords': keywords,
#     'reserved_words': reserved_words,
#     'data_type': data_type,
#     'noise_words': noise_words,
#     'full_words': full_words,
#     'constants': constants,
#     'spaces': spaces,
# }
