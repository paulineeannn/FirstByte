# Importing token sets from an external module
from tokens import alphabet, digits, special_chars, delimiters, constants, operators, keywords, reserved_words, data_type, noise_words, spaces

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
                # Append the string token to the list
                tokens.append(('STRING', current_token))
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

            # Check if the current token is in the delimiters set
            if current_token in delimiters:
                tokens.append((delimiters[current_token], current_token))

            # If not found in the delimiters set, consider it as an individual delimiter token
            elif current_token in delimiters:
                tokens.append((delimiters[current_token], current_token))

            current_token = ""  # Reset the current token

        # Handling comments starting with '@'
        elif char == '@':
            if i < len(input_string) - 1 and input_string[i + 1] == '@':  # Multi-line comment
                i += 2  # Skip the two '@' characters
                current_token = ""
                while i < len(input_string) and input_string[i:i + 2] != '@@':
                    current_token += input_string[i]
                    i += 1
                # Append multi-line comment tokens to the list
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
                # Append single-line comment tokens to the list
                tokens.append(('CHAR_COMMENT_SYM_SINGLE', '@'))
                tokens.append(('COMMENT_SYM_SINGLE', current_token))
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
                        tokens.append(('RESERVED_WORDS', possible_token))
                        current_token = current_token[j:]
                        break

                if current_token:
                    # Check if the current token is a noise word following a recognized data type, keyword, or reserved word
                    if current_token in noise_words and (tokens[-1][1] in data_type or tokens[-1][1] in keywords or tokens[-1][1] in reserved_words):
                        # Append the noise word token to the list
                        tokens.append(('NOISE_WORDS', current_token))

                    # Check if the current token is an operator
                    elif current_token in operators:
                        # Append the recognized operator token to the list
                        tokens.append((operators[current_token], current_token))

                    # If none of the above, consider it as a regular identifier
                    else:
                        # Append the regular identifier token to the list
                        tokens.append(('IDENTIFIER', current_token))

            current_token = ""  # Reset the current token

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

        # Handling numbers (integer and decimal)
        elif is_digit(char):
            current_token += char
            i += 1

            # Continue adding digits to the current token for integers
            while i < len(input_string) and input_string[i].isdigit():
                current_token += input_string[i]
                i += 1

            token_type = "INTEGER"

            # Check for the decimal point for decimal numbers
            if i < len(input_string) and input_string[i] == '.':
                current_token += input_string[i]
                i += 1
                # Continue adding digits to the current token for decimals
                while i < len(input_string) and input_string[i].isdigit():
                    current_token += input_string[i]
                    i += 1
                token_type = "DECIMAL"

            # Check for invalid delimiters, spaces, and operators following the number
            if input_string[i] not in delimiters and input_string[i] != ' ' and input_string[i] != '\n' and input_string[i] not in operators and input_string[i] != ',':
                current_token += input_string[i]
                i += 1
                # Continue collecting characters for an invalid token until a delimiter, space, newline, or operator is found
                while i < len(input_string) and input_string[i] not in delimiters and input_string[i] != ' ' and input_string[i] != '\n' and input_string[i] not in operators and input_string[i] != ',':
                    current_token += input_string[i]
                    i += 1
                    token_type = "INVALID_TOKEN"

            # Append the recognized number token to the list
            tokens.append((token_type, current_token))

            current_token = ""  # Reset the current token

        # Handling operators
        elif is_operator(char):
            current_token += char
            i += 1

            # Continue adding characters to the current token if they are also operators
            while i < len(input_string) and (is_operator(input_string[i])):
                current_token += input_string[i]
                i += 1

            # Check if the combined token is in operators
            if current_token in operators:
                # Append the recognized operator token to the list
                tokens.append((operators[current_token], current_token))
            else:
                # If not recognized, consider it as an invalid token
                tokens.append(("INVALID_TOKEN", current_token))

            current_token = ""  # Reset the current token

        # Handling invalid tokens
        elif is_invalid(char):
            current_token += char
            i += 1

            # Continue adding characters to the current token if they are also invalid
            while i < len(input_string) and is_invalid(input_string[i]):
                current_token += input_string[i]
                i += 1

            # Append the invalid token with its type to the list
            tokens.append(('INVALID_TOKEN', current_token))
            current_token = ""  # Reset the current token

        else:
            i += 1  # Move to the next character

    # Return the list of tokens for the symbol table
    return tokens
