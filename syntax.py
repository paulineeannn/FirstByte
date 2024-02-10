from production_rules import *
from tokens import spaces
import errors

def main(token_list):

    # List to store the identified syntax
    invalid_list = []
    formatted_token = ""
    code = ""
    line = 0
    for x in range(len(token_list)):
        valid = False

        # check if the token of one line exist in the production rules
        if token_list[x][0] == "NEWLINE":
            line += 1
            for statement in STATEMENTS_LIST:
                if formatted_token in statement:
                    valid = True

            print(formatted_token)
            if not valid and (code not in spaces and code != ""):
                error_message = errors.find_error(formatted_token)
                invalid_list.append((line, code, error_message))

            formatted_token = ""  # reset
            code = ""

        # create a string containing token of one line
        else:
            format_token = f"<{token_list[x][2]}>"
            formatted_token += format_token
            code +=  f"{token_list[x][1]}"


    return line, invalid_list
