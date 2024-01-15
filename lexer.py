from tokens import alphabet, digits, special_chars, delimiters, operators, keywords, reserved_words, data_type, spaces

def main(input_string):
    def is_letter(char):
        return char in alphabet

    def is_digit(char):
        return char in digits

    def is_operator(char):
        return char in operators

    def is_special_char(char):
        return char in special_chars

    def is_delimiter(char):
        return char in delimiters

    def is_space(char):
        return char in spaces

    def is_inv_identifier(char):
        return (is_special_char(input_string[i]) or is_invalid(input_string[i])) and input_string[i] != '_' and input_string[i] != ','

    # Define a function to identify invalid tokens
    def is_invalid(char):
        return not (is_letter(char) or is_digit(char) or is_operator(char) or is_delimiter(char) or is_special_char(char) or is_space(char) or char == '"')

    tokens = []
    is_string = False
    current_token = ""
    i = 0
    while i < len(input_string):
        char = input_string[i]

        if char == '"':
            # Toggle the flag when encountering a double quotation mark
            is_string = not is_string
            if is_string:
                current_token += char
            else:
                current_token += char
                tokens.append(('STRING', current_token))  # Append the string token
                current_token = ""  # Reset the current token
            i += 1

        elif is_string:
            current_token += char
            i += 1


        elif is_delimiter(char):
            current_token += char
            i += 1

            if current_token in delimiters:
                tokens.append((delimiters[current_token], current_token))

            elif current_token in delimiters:
                tokens.append((delimiters[current_token], current_token))

            current_token = ""

        elif char == '@':
            if i < len(input_string) - 1 and input_string[i + 1] == '@':  # Multi-line comment
                i += 2  # Skip the two '@' characters
                current_token = ""
                while i < len(input_string) and input_string[i:i + 2] != '@@':
                    current_token += input_string[i]
                    i += 1
                tokens.append(('CHAR_COMMENT_SYM_MULTI', '@@'))
                tokens.append(('COMMENT_SYM_MULTI', current_token))
                tokens.append(('CHAR_COMMENT_SYM_MULTI', '@@'))
                current_token = ""
                i += 2  # Skip the ending '@@'
            else:  # Single-line comment
                i += 1  # Skip the initial '@'
                current_token = ""
                while i < len(input_string) and input_string[i] != "\n":
                    current_token += input_string[i]
                    i += 1
                tokens.append(('CHAR_COMMENT_SYM_SINGLE', '@'))
                tokens.append(('COMMENT_SYM_SINGLE', current_token))
                current_token = ""

        elif is_letter(char):
            # Handling data type, keywords, reserved words, and identifiers starting with letters
            current_token += char
            i += 1

            while i < len(input_string) and (is_letter(input_string[i]) or is_digit(input_string[i]) or input_string[i] == '_'):
                current_token += input_string[i]
                i += 1

            if is_inv_identifier(input_string[i]):
                current_token += input_string[i]
                i += 1

                while i < len(input_string) and (input_string[i] != ' ' and input_string[i] != '\n') and input_string[i] not in operators:
                    current_token += input_string[i]
                    i += 1

                tokens.append(('INVALID_TOKEN', current_token))

            elif current_token in data_type:
                tokens.append(('DATA_TYPE', current_token))
            elif current_token in keywords:
                tokens.append(('KEYWORD', current_token))
            elif current_token in reserved_words:
                tokens.append(('RESERVED_WORDS', current_token))
            elif current_token in operators:
                tokens.append((operators[current_token], current_token))
            else:
                tokens.append(('IDENTIFIER', current_token))

            current_token = ""

        # Handling identifiers starting with underscore
        elif char == '_':
            current_token += char
            i += 1
            while i < len(input_string) and (is_letter(input_string[i]) or is_digit(input_string[i]) or input_string[i] == '_'):
                current_token += input_string[i]
                i += 1

            token = 'IDENTIFIER'
            if is_inv_identifier(input_string[i]):
                current_token += input_string[i]
                i += 1

                while i < len(input_string) and (input_string[i] != ' ' and input_string[i] != '\n') and input_string[i] not in operators:
                    current_token += input_string[i]
                    i += 1

                token = 'INVALID_TOKEN'

            tokens.append((token, current_token))
            current_token = ""

        # Handling special characters and == (equal to operator)
        elif is_special_char(char):
            current_token += char
            i += 1

            # Check for consecutive equal signs
            if i < len(input_string) and input_string[i] == '=':
                current_token += input_string[i]
                i += 1

            # Check if the combined token is in special_chars or operators
            if current_token in special_chars:
                tokens.append((special_chars[current_token], current_token))
            elif current_token in operators:
                tokens.append((operators[current_token], current_token))
            else:
                tokens.append(("INVALID_TOKEN", current_token))

            current_token = ""

        # Handling  numbers
        # elif is_digit(char):
        #     current_token += char
        #     i += 1
        #
        #     period_count = 0
        #     invalid_count = 0
        #
        #     while i < len(input_string) and (is_digit(input_string[i]) or input_string[i] == '.' or is_special_char(input_string[i])) and input_string[i+1] != " ":
        #         if is_special_char(input_string[i]) and input_string[i] != '.' and input_string[i] != ',':
        #             invalid_count += 1
        #         if input_string[i] == '.':
        #             period_count += 1
        #         if period_count > 2:
        #             current_token += input_string[i]
        #             i += 1
        #             while i < len(input_string) and input_string[i].isdigit():
        #                 current_token += input_string[i]
        #                 i += 1
        #         current_token += input_string[i]
        #         i += 1
        #
        #
        #     if period_count > 0 and ',' in current_token:
        #         tokens.append(('INVALID_TOKEN', current_token))
        #
        #     elif invalid_count > 0:
        #         tokens.append(('INVALID_TOKEN', current_token))
        #
        #     elif period_count <= 1:
        #         token_type = "INTEGER" if '.' not in current_token else "DECIMAL"
        #         tokens.append((token_type, current_token))
        #
        #     elif period_count > 2:
        #         tokens.append(('INVALID_TOKEN', current_token))
        #
        #
        #
        #     current_token = ""

        # handling numbers
        elif is_digit(char):
            current_token += char
            i += 1

            while i < len(input_string) and input_string[i].isdigit():
                current_token += input_string[i]
                i += 1

            token_type = "INTEGER"

            if i < len(input_string) and input_string[i] == '.':
                current_token += input_string[i]
                i += 1
                while i < len(input_string) and input_string[i].isdigit():
                    current_token += input_string[i]
                    i += 1
                token_type = "DECIMAL"

            # valid_delimiters = [']', ')','}', ',']
            if input_string[i] not in delimiters and input_string[i] != ' ' and input_string[i] != '\n' and input_string[i] not in operators and input_string[i] != ',':
                current_token += input_string[i]
                i += 1
                while i < len(input_string) and input_string[i] not in delimiters and input_string[i] != ' ' and input_string[i] != '\n' and input_string[i] not in operators and input_string[i] != ',':
                    current_token += input_string[i]
                    i += 1
                    token_type = "INVALID_TOKEN"

            tokens.append((token_type, current_token))

            current_token = ""

        elif is_operator(char):
            current_token += char
            i += 1

            while i < len(input_string) and (is_operator(input_string[i])):
                current_token += input_string[i]
                i += 1

            if current_token in operators:
                tokens.append((operators[current_token], current_token))
            else:
                tokens.append(("INVALID_TOKEN", current_token))

            current_token = ""

        # Handling invalid tokens
        elif is_invalid(char):
            current_token += char
            i += 1

            while i < len(input_string) and is_invalid(input_string[i]):
                current_token += input_string[i]
                i += 1

            # Append the invalid token with its type
            tokens.append(('INVALID_TOKEN', current_token))
            current_token = ""

        else:
            i += 1

    # return list for symbol table
    return tokens
