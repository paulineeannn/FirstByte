from tokens import *
import syntax

def main(input_string):
    # Function to check if a character is a letter
    def is_letter(char):
        return char in alphabet

    # Function to check if a character is a digit
    def is_digit(char):
        return char in digits

    # Function to check if a character is an operator
    def is_operator(char):
        return char in operators

    # Function to check if a character is a special character
    def is_special_char(char):
        return char in special_chars

    # Function to check if a character is a delimiter
    def is_delimiter(char):
        return char in delimiters

    # Function to check if a character is a space
    def is_space(char):
        return char in spaces

    # Function to check if a character is part of an invalid identifier
    def is_inv_identifier(char):
        return (is_special_char(input_string[i]) or is_operator(input_string[i]) or is_invalid(input_string[i])) and input_string[i] != '_' and input_string[i] != ','

    # Function to check if a character is invalid
    def is_invalid(char):
        return not (is_letter(char) or is_digit(char) or is_operator(char) or is_delimiter(char) or is_special_char(char) or is_space(char) or char == '"')

    # List to store the identified tokens
    tokens = []
    # Flag to track if we are inside a string
    is_string = False
    # Variable to store the current token being processed
    current_token = ""
    # Index variable to iterate through the input string
    i = 0

    # Main loop to iterate through each character in the input string
    while i < len(input_string):
        char = input_string[i]

        # Handling double quotation marks for strings
        if char == '"':
            # Toggle the string flag when encountering a double quotation mark
            is_string = not is_string
            if is_string:
                current_token += char
            else:
                current_token += char
                i += 1

                if len(current_token) == 3 and current_token[1].isalpha():  # Check if current_token is a single alphabet enclosed in double quotes
                    tokens.append(('CHAR', current_token, 'CHAR'))
                else:
                    tokens.append(('STRING', current_token, 'STRING'))

                if input_string[i] in spaces:
                    tokens.append((spaces[input_string[i]], input_string[i], spaces[input_string[i]]))
                elif input_string[i] in delimiters:
                    tokens.append((delimiters[input_string[i]], input_string[i], delimiters[input_string[i]]))
                else:
                    while input_string[i] not in spaces:
                        current_token += input_string[i]
                        i += 1
                    tokens.append(('INVALID_TOKEN', current_token, 'INVALID_TOKEN'))

                current_token = ""  # Reset the current token
            i += 1

        # If currently inside a string, continue adding characters to the current token
        elif is_string:
            current_token += char
            i += 1

        # Handling delimiters
        elif is_delimiter(char):
            current_token += char
            i += 1

            tokens.append((delimiters[current_token], current_token, delimiters[current_token]))
            current_token = "" # Reset the current token


        # Handling comments
        elif char == '@':
            if i < len(input_string) - 1 and input_string[i + 1] == '@':  # Multi-line comment
                i += 2  # Skip the two '@' characters
                current_token = ""

                tokens.append(('COMMENT_SYM_MULTI', '@@', 'COMMENT_SYM_MULTI'))
                while i < len(input_string) and input_string[i:i + 2] != '@@':
                    current_token += input_string[i]

                    i += 1

                # Append multi-line comment tokens to the list
                tokens.append(('COMMENT_MULTI', current_token, 'COMMENT_MULTI'))

                if i < len(input_string) and input_string[i:i + 2] == '@@':
                    tokens.append(('CHAR_COMMENT_SYM_MULTI', '@@', 'CHAR_COMMENT_SYM_MULTI'))

                current_token = ""
                i += 2  # Skip the ending '@@'

            else:  # Single-line comment
                i += 1  # Skip the initial '@'
                current_token = ""

                while i < len(input_string) and input_string[i] != "\n":
                    current_token += input_string[i]
                    i += 1

                # Append single-line comment tokens to the list
                tokens.append(('COMMENT_SYM_SINGLE', '@', 'CHAR_COMMENT_SYM_SINGLE'))
                tokens.append(('COMMENT_SINGLE', current_token, 'COMMENT_SINGLE'))

                current_token = ""

                # Handling identifiers starting with letters

        elif is_letter(char):
            # Start building the current token with the first letter
            current_token += char
            i += 1

            # Continue adding characters to the current token until a non-letter character is encountered
            while i < len(input_string) and (is_letter(input_string[i]) or is_digit(input_string[i]) or input_string[i] == '_'):
                current_token += input_string[i]
                i += 1

            # Check for invalid identifiers
            if  i < len(input_string) and is_inv_identifier(input_string[i]) and input_string[i+1] not in spaces:
                current_token += input_string[i]
                i += 1

                # Continue collecting characters for an invalid identifier until a space, newline, or operator is found.
                while i < len(input_string) and input_string[i] not in spaces:
                    current_token += input_string[i]
                    i += 1

                # Append the invalid identifier token to the list
                tokens.append(('INVALID_TOKEN', current_token, 'INVALID_TOKEN'))


            else:
                if current_token in full_words:
                    # Check if the current token is a noise word or a valid token
                    for j in range(len(current_token), 0, -1):
                        possible_token = current_token[:j]
                        # Check if the possible token is a recognized data type
                        if possible_token in data_type:
                            # Append the recognized data type token to the list
                            tokens.append(("DATA_TYPE", possible_token, "DATA_TYPE"))
                            current_token = current_token[j:]
                            break

                        # Check if the possible token is a recognized keyword
                        elif possible_token in keywords:
                            # Append the recognized keyword token to the list
                            tokens.append(('KEYWORD', possible_token, keywords[current_token]))
                            current_token = current_token[j:]
                            break

                        # Check if the possible token is a recognized keyword
                        elif possible_token in reserved_words:
                            # Append the recognized keyword token to the list
                            tokens.append(('RESERVED_WORD', possible_token, reserved_words[current_token]))
                            current_token = current_token[j:]
                            break

                    if current_token:
                        if len(tokens) > 0:
                            if current_token in noise_words and (tokens[-1][1] in data_type or tokens[-1][1] in keywords or tokens[-1][1] in reserved_words):
                                tokens.append(('NOISE_WORD', current_token, 'NOISE_WORD'))

                            elif current_token in operators:
                                tokens.append((operators[current_token], current_token, operators[current_token]))

                            else:
                                tokens.append(('IDENTIFIER', current_token, 'IDENTIFIER'))


                        elif current_token in operators:
                            tokens.append((operators[current_token], current_token, operators[current_token]))

                        else:
                            tokens.append(('IDENTIFIER', current_token, 'IDENTIFIER'))

                elif current_token in data_type:
                    tokens.append(("DATA_TYPE", current_token, data_type[current_token]))
                elif current_token in keywords:
                    tokens.append(('KEYWORD', current_token, keywords[current_token]))
                elif current_token in reserved_words:
                    tokens.append(('RESERVED_WORDS', current_token, reserved_words[current_token]))
                elif current_token in operators:
                    tokens.append((operators[current_token], current_token, operators[current_token]))
                elif current_token in constants:
                    tokens.append(('CONSTANT', current_token, 'CONSTANT'))

                else:
                    tokens.append(('IDENTIFIER', current_token, 'IDENTIFIER'))

            current_token = ""


        # Handling identifiers starting with underscore
        elif char == '_':
            current_token += char
            i += 1

            # Continue adding characters to the current token until a non-letter character is encountered
            while i < len(input_string) and (is_letter(input_string[i]) or is_digit(input_string[i]) or input_string[i] == '_'):
                current_token += input_string[i]
                i += 1

            token = 'IDENTIFIER'
            # Check for invalid identifiers
            if  i < len(input_string) and is_inv_identifier(input_string[i]) and input_string[i+1] not in spaces:
                current_token += input_string[i]
                i += 1

                # Continue collecting characters for an invalid identifier until a space, newline, or operator is found
                while i < len(input_string) and input_string[i] not in spaces:
                    current_token += input_string[i]
                    i += 1

                token = 'INVALID_TOKEN'

            # Append the identifier or invalid identifier token to the list
            tokens.append((token, current_token, token))
            current_token = ""  # Reset the current token

        # Handling special characters and equal-to operator '=='
        elif is_special_char(char):
            current_token += char
            i += 1

            # Check for consecutive equal signs
            if i < len(input_string) and input_string[i] == '=':
                current_token += input_string[i]
                i += 1

            # Check if the combined token is in special_chars or operators
            if current_token in special_chars:
                # Append the recognized special character token to the list
                tokens.append((special_chars[current_token], current_token, special_chars[current_token]))
            elif current_token in operators:
                # Append the recognized operator token to the list
                tokens.append((operators[current_token], current_token, operators[current_token]))
            else:
                # If not recognized, consider it as an invalid token
                tokens.append(("INVALID_TOKEN", current_token, "INVALID_TOKEN"))

            current_token = ""  # Reset the current token

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
                if is_digit(input_string[i]):
                    while i < len(input_string) and input_string[i].isdigit():
                        current_token += input_string[i]
                        i += 1
                    token_type = "DECIMAL"
                else:
                    token_type = "INVALID_TOKEN"

            if input_string[i] not in delimiters and input_string[i] not in spaces and input_string[i] != ',':
                current_token += input_string[i]
                i += 1
                while i < len(input_string) and input_string[i] not in delimiters and input_string[i] != ' ' and input_string[i] != '\n' and input_string[i] not in operators and input_string[i] != ',':
                    current_token += input_string[i]
                    i += 1
                token_type = "INVALID_TOKEN"

            tokens.append((token_type, current_token, token_type))

            current_token = ""

        # Handling operators
        elif is_operator(char):
            current_token += char
            i += 1

            # Continue adding characters to the current token if they are also operators
            while i < len(input_string) and (is_operator(input_string[i])):
                current_token += input_string[i]
                i += 1

            # Check if the combined token is in operators
            if current_token == "++" or current_token == "--":
                tokens.append((operators[current_token], current_token, operators[current_token]))

            elif current_token in operators and input_string[i] in spaces:  # checks if the next char is in space
                # Append the recognized operator token to the list
                tokens.append((operators[current_token], current_token, operators[current_token]))

            else:
                # If not recognized, consider it as an invalid token
                current_token += input_string[i]
                i += 1
                while i < len(input_string) and input_string[i] not in spaces and input_string[i] not in delimiters:
                    current_token += input_string[i]
                    i += 1
                tokens.append(("INVALID_TOKEN", current_token, 'INVALID_TOKEN'))

            current_token = ""  # Reset the current token

        elif is_space(char):
            current_token += input_string[i]
            i += 1

            tokens.append((spaces[current_token], current_token, spaces[current_token]))

            current_token = ""


        # Handling invalid tokens
        elif is_invalid(char):
            current_token += char
            i += 1

            while i < len(input_string) and is_invalid(input_string[i]):
                current_token += input_string[i]
                i += 1

            # Append the invalid token with its type
            tokens.append(('INVALID_TOKEN', current_token, 'INVALID_TOKEN'))
            current_token = ""


        else:
            i += 1

    # return list for symbol table
    return tokens


def call_syntax(input_string):
    tokens = main(input_string)
    line_numbers, result_syntax = syntax.main(tokens)

    return line_numbers, result_syntax
