from production_rules import *
from tokens import spaces

def main(tokens):

    # List to store the identified syntax
    syntax_result = []
    token = ""
    code = ""
    for x in range(len(tokens)):
        valid = False

        # check if the tokens of one line exist in the production rules
        if tokens[x][0] == "NEWLINE":

            for statement in STATEMENTS_LIST:
                if token in statement:
                    valid = True

            print(token)
            if valid:
                syntax_result.append(("VALID", code))

            elif not valid and (code not in spaces and code != ""):
                syntax_result.append(("INVALID", code))

            token = ""  # reset
            code = ""

        # create a string containing tokens of one line
        else:
            format_token = f"<{tokens[x][2]}>"
            token += format_token
            code +=  f"{tokens[x][1]}"


    return syntax_result
