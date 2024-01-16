alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

digits = '0123456789'

special_chars = {
    "." : "PERIOD",
    "@" : "COMMENT_SYM_SINGLE",
    "@@" : "COMMENT_SYM_MULTI",
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
    ":": "COLON",
    "(": "PARENTHESIS_L",
    ")": "PARENTHESIS_R",
    "[": "BRACKET_L",
    "]": "BRACKET_R",
    "{": "BRACE_L",
    "}": "BRACE_R",
}

operators= {
    "=": "EQUAL",
    "+=" : "ADD_ASSIGNMENT",
    "-=" : "SUBTRACT_ASSIGNMENT",
    "*=" : "MULTIPLICATION_ASSIGNMENT",
    "/=" : "DIVISION_ASSIGNMENT",
    "%=" : "MODULO_ASSIGNMENT",
    "++" : "INCREMENT",
    "--" : "DECREMENT",
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
    "char",
    "when",
    "otherwise",
    "loop",
    "to",
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
    "TRUE",
    "FALSE",
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

noise_words = {
    "ean",
    "eger",
    "mal",
    "er",
    "ing",
    "acter",
    "ault",
    "inue"
}

constants = {
    "pi",
    "accGrav",
    "euler",
    "goldenRatio"
}

spaces = {' ', '\n', '\t'}

