import re # used for analyzing regular expressions
# import os # going to be used to get if the files exists or not

class Lexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.tokens = [] # holds the tokens
        self.current_position = 0 # current position in the text WITHIN the file

    def tokenize(self):
        state = "START" # Intiailize state as START, as it will represent the start state
        buffer = ""

        while self.current_position < len(self.input_string):
            char = self.input_string[self.current_position]

            if state == "START": # If we are on the start state
                if char.isdigit() or char.isdecimal() : # Check is the next char is a digit
                    state = "REAL"
                    buffer += char
                elif char.isalpha():
                    state = "IDENTIFIER"
                    buffer += char
                elif char in "+-*/=<>":
                    self.tokens.append(("OPERATOR", char))
                elif char in ",;:()":
                    self.tokens.append(("SEPARATOR", char))
                elif char.isspace():
                    pass  # Skip whitespaces
                else:
                    # Handle unknown characters
                    print("Unknown character:", char)

            elif state == "REAL": # Case when the state is number
                if char.isdigit() or char == ".":
                    buffer += char
                else:
                    self.tokens.append(("REAL", buffer))
                    buffer = ""
                    state = "START"
                    continue

            elif state == "IDENTIFIER":
                if char.isalnum() or char == "_":
                    buffer += char
                else:
                    self.tokens.append(("IDENTIFIER", buffer))
                    buffer = ""
                    state = "START"
                    continue

            self.current_position += 1 # Goes to the next char position

        # Handles end of input string
        if state == "REAL":
            self.tokens.append(("REAL", buffer))
        elif state == "IDENTIFIER":
            self.tokens.append(("IDENTIFIER", buffer))


        return self.tokens


def main():

    with open(f"input.txt", "r") as file:
        input_string = file.read()

    lexer = Lexer(input_string)
    tokens = lexer.tokenize()

    with open(f"output.txt", "w") as file: # Output file will be our list of tokens/lexemes
        for token, lexeme in tokens:
            file.write(f"{token}, {lexeme}\n")
            print(f"{token}, {lexeme}\n") 

if __name__ == "__main__":
    main()

