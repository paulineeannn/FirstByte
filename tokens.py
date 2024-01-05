alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

digits = '0123456789'

special_chars = {
    "." : "PERIOD",
    "@" : "COMMENT_SYM_SINGLE",
    "@@" : "COMMENT_SYM_MULTI",
    "#" : "POUND",
    "=": "EQUAL",
    # '"' : "DOUBLE_QUOTE",
    # "'" : "SINGLE_QUOTE",
    "," : "COMMA",
    ":" : "COLON",
    ";" : "SEMICOLON",
    "|" : "PIPE",
    "\\" : "BACKSLASH",
    "(" : "PARENTHESIS_L",
    ")" : "PARENTHESIS_R",
    "[" : "BRACKET_L",
    "]" : "BRACKET_R",
    "{": "BRACE_L",         # wala sa documentation
    "}": "BRACE_R",         # wala sa documentation
    "_" : "UNDERSCORE",
    "~" : "TILDE",
    "&" : "AMPERSAND"
}

operators= {
    "+=" : "ADD_ASSIGNMENT",
    "-=" : "SUBTRACT_ASSIGNMENT",
    "*=" : "MULTIPLICATION_ASSIGNMENT",
    "/=" : "DIVISION_ASSIGNMENT",
    "%=" : "MODULO_ASSIGNMENT",
    "+": "PLUS",
    "-": "MINUS",
    "*": "MULTIPLY",
    "/": "DIVIDE",
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

keywords = {
    "bool",
    "def",
    "pow",
    "char",
    "when",
    "otherwise",
    "loop",
    "input",
    "output",
    "stop",
    "jump",
    "arithSeq",
    "arithSer",
    "geoSeq",
    "geoSer",
    "distance",
    "slope",
    "pythagorean",
    "quadratic",
    "force",
    "work",
    "acceleration",
    "power",
    "momentum",
    "potential",
    "kinetic",
    "toInt",
    "toDeci",
    "toStr"
}

reserved_words = {
    "true",     # magkaiba case na nasa docu (true nasa #4 tas True sa #3)
    "false",
    "main",
    "cont"
}

data_type = {
    "int" : "INTEGER",
    "str" : "STRING",
    "char" : "CHARACTER",
    "deci" : "DECIMAL",
    "bool" : "BOOLEAN"
}

spaces = {' ', '\n', '\t'}

