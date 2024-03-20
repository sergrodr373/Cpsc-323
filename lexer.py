
# import os # going to be used to get if the files exists or not
from tabulate import tabulate

class Lexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.tokens = [] # holds the tokens
        self.current_position = 0 # current position in the text WITHIN the file

    def tokenize(self):
        state = "START" # Intiailize state as START, as it will represent the start state
        input_buffer = "" # acts as a temp storage, and used to check instances in the input.txt file

        while self.current_position < len(self.input_string):
            char = self.input_string[self.current_position]

            if state == "START": # state state
                if char.isdigit() or char == ".":
                    state = "REAL" # state turns into REAL state IF we get a digit
                    input_buffer += char
                elif char.isalpha():
                    state = "IDENTIFIER" # state turns into REAL state IF we get a letter
                    input_buffer += char
                elif char in "+-*/=<>": # state still is a START
                    self.tokens.append(("OPERATOR", char)) # pass operator when encountering chars above
                elif char in ",;:()": # state still at START
                    self.tokens.append(("SEPARATOR", char)) # pass separator when encountering chars above
                elif char.isspace():
                    pass  # Skip space chars
                else:
                    print("UNKNOWN", char)

            elif state == "REAL": # handles numbers (ints and decimals)
                if char.isdigit() or char == ".": # Checks if char is digit or contains "."
                    input_buffer += char
                else:
                    self.tokens.append(("REAL", input_buffer))
                    input_buffer = ""
                    state = "START"
                    continue

            elif state == "IDENTIFIER":
                if char.isalnum() or char == "_": # checks if char is letter or numeric has "_"
                    input_buffer += char
                else:
                    if input_buffer.isalpha() and input_buffer.lower() in ["while", "for", "if", 'else', 'int', 'in', 'range','elif']: #checks if char is letter AND if its one of the keywords listed
                        self.tokens.append(("KEYWORD", input_buffer.lower())) # if so pass KEYWORD
                    else:
                        self.tokens.append(("IDENTIFIER", input_buffer)) # anything else not mentioned above; must be a user defined variable
                    input_buffer = ""
                    state = "START"
                    continue

            self.current_position += 1 # move to the next char in the input string

        # Handle end of input string
        if state == "REAL": # When we are in the REAL state
            self.tokens.append(("REAL", input_buffer)) 
        elif state == "IDENTIFIER":# When we are in the identifier state
            if input_buffer.isalpha() and input_buffer.lower() in ["while", "for", "if", 'else', 'int', 'in', 'range', 'elif']:
                self.tokens.append(("KEYWORD", input_buffer.lower())) # pass keyword if input_buffer contains any of these
            else:
                self.tokens.append(("IDENTIFIER", input_buffer)) # pass indentifier if anything else
        elif state == "START":
            state = "FINAL" # This is the FINAL state, marking the end of the input string
            pass
        return self.tokens

def main():

    with open(f"input.txt", "r") as file: # input.txt will have all the input string
        input_string = file.read()

    lexer = Lexer(input_string)
    tokens = lexer.tokenize()
    table = tabulate(tokens, headers=['Token', 'Lexeme'], tablefmt='grid')
    with open(f"output.txt", "w") as file: # Output file will be our list of tokens/lexemes
        for token, lexeme in tokens:
            #file.write(f"{token}, {lexeme}\n") # outputs to file
            print(f"{token}, {lexeme}\n") 
        file.write(table)

if __name__ == "__main__":
    main()

