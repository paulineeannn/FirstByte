from tokens import *

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
        return (is_special_char(input_string[i]) or is_invalid(input_string[i])) and input_string[i] != '_' and input_string[i] != ','

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

                if input_string[i] in spaces:
                    tokens.append(('STRING', current_token))
                    current_token = ""  # Reset the current token
                elif input_string[i] in delimiters:
                    tokens.append(('STRING', current_token))
                    tokens.append(('STRING', input_string[i]))
                    current_token = ""  # Reset the current token
                else:
                    while input_string[i] not in spaces:
                        current_token += input_string[i]
                        i += 1

                    tokens.append(('INVALID_TOKEN', current_token))
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

            tokens.append((delimiters[current_token], current_token))
            current_token = "" # Reset the current token


        # Handling comments
        elif char == '@':
            current_token += char
            i += 1

            # Check for consecutive '@' characters
            while i < len(input_string) and input_string[i] == '@':
                current_token += input_string[i]
                i += 1

            # Append the recognized special character token to the list
            if current_token in special_chars:
                tokens.append((special_chars[current_token], current_token))
            else:
                # If not recognized, consider it as an identifier
                tokens.append(('IDENTIFIER', current_token))

            current_token = ""  # Reset the current token

        # If currently inside a string or comment, continue adding characters to the current token
        elif is_string or char == '@':
            current_token += char
            i += 1

        elif is_letter(char):
            # Start building the current token with the first letter
            current_token += char
            i += 1

            # Continue adding characters to the current token until a non-letter character is encountered
            while i < len(input_string) and (is_letter(input_string[i]) or is_digit(input_string[i]) or input_string[i] == '_'):
                current_token += input_string[i]
                i += 1

            # Check for invalid identifiers
            if is_inv_identifier(input_string[i]):
                current_token += input_string[i]
                i += 1

                # Continue collecting characters for an invalid identifier until a space, newline, or operator is found
                while i < len(input_string) and (input_string[i] != ' ' and input_string[i] != '\n') and input_string[i] not in operators:
                    current_token += input_string[i]
                    i += 1

                # Append the invalid identifier token to the list
                tokens.append(('INVALID_TOKEN', current_token))

            else:
                # Check if the current token is a noise word or a valid token
                for j in range(len(current_token), 0, -1):
                    possible_token = current_token[:j]
                    # Check if the possible token is a recognized data type
                    if possible_token in data_type:
                        # Append the recognized data type token to the list
                        tokens.append(('DATA_TYPE', possible_token))
                        current_token = current_token[j:]
                        break

                    # Check if the possible token is a recognized keyword
                    elif possible_token in keywords:
                        # Append the recognized keyword token to the list
                        tokens.append(('KEYWORD', possible_token))
                        current_token = current_token[j:]
                        break

                    # Check if the possible token is a recognized reserved word
                    elif possible_token in reserved_words:
                        # Append the recognized reserved word token to the list
                        tokens.append(('RESERVED_WORD', possible_token))
                        current_token = current_token[j:]
                        break

                    # Check if the possible token is a recognized constant
                    elif possible_token in constants:
                        tokens.append(('CONSTANT', possible_token))
                        current_token = current_token[j:]
                        break

                if current_token:
                    if len(tokens) > 0:
                        if current_token in noise_words and (tokens[-1][1] in data_type or tokens[-1][1] in keywords or tokens[-1][1] in reserved_words):
                            tokens.append(('NOISE_WORD', current_token))

                        elif current_token in operators:
                            tokens.append((operators[current_token], current_token))

                        else:
                            tokens.append(('IDENTIFIER', current_token))

                    elif current_token in operators:
                        tokens.append((operators[current_token], current_token))

                    else:
                        tokens.append(('IDENTIFIER', current_token))

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
            if is_inv_identifier(input_string[i]):
                current_token += input_string[i]
                i += 1

                # Continue collecting characters for an invalid identifier until a space, newline, or operator is found
                while i < len(input_string) and (input_string[i] != ' ' and input_string[i] != '\n') and input_string[i] not in operators:
                    current_token += input_string[i]
                    i += 1

                token = 'INVALID_TOKEN'

            # Append the identifier or invalid identifier token to the list
            tokens.append((token, current_token))
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
                tokens.append((special_chars[current_token], current_token))
            elif current_token in operators:
                # Append the recognized operator token to the list
                tokens.append((operators[current_token], current_token))
            else:
                # If not recognized, consider it as an invalid token
                tokens.append(("INVALID_TOKEN", current_token))

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

            if input_string[i] not in delimiters and input_string[i] != ' ' and input_string[i] != '\n' and input_string[i] not in operators and input_string[i] != ',':
                current_token += input_string[i]
                i += 1
                while i < len(input_string) and input_string[i] not in delimiters and input_string[i] != ' ' and input_string[i] != '\n' and input_string[i] not in operators and input_string[i] != ',':
                    current_token += input_string[i]
                    i += 1
                token_type = "INVALID_TOKEN"

            tokens.append((token_type, current_token))

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
            if current_token in operators and input_string[i] in spaces:  # checks if the next char is in space
                # Append the recognized operator token to the list
                tokens.append((operators[current_token], current_token))
            else:
                # If not recognized, consider it as an invalid token
                current_token += input_string[i]
                i += 1
                while i < len(input_string) and input_string[i] not in spaces:
                    current_token += input_string[i]
                    i += 1
                tokens.append(("INVALID_TOKEN", current_token))

            i += 1
            current_token = ""  # Reset the current token


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