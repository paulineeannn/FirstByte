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
    "acter",
    "default",
    "continue"
}

constants = {
    "pi",
    "accGrav",
    "euler",
    "goldenRatio"
}

spaces = {' ', '\n', '\t'}

