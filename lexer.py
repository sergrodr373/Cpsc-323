import re # used for analyzing regular expressions
import os # going to be used to get if the files exists or not

class Lexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.tokens = [] # holds the tokens
        self.current_position = 0 # current position in the text WITHIN the file

    def tokenize(self):
        while self.current_position < len(self.input_string):
            char = self.input_string[self.current_position]
            if char.isdigit() or char.isdecimal():
                integer_lexeme = self.parse_integer()
                self.tokens.append(("REAL", integer_lexeme))
            elif char.isalpha() or char == "": # checks if an instance in the text is a letter OR an empty string
                identifier_lexeme = self.parse_identifier()
                self.tokens.append(("IDENTIFIER", identifier_lexeme))
            
                separator_lexeme = self.parse_seperators() # Checks for . , ;
            
            else:
                keyword_lexeme = self.parse_keywords() # Checks for keywords like for, while, etc
                if keyword_lexeme:
                    
                    self.tokens.append(("KEYWORD", keyword_lexeme))
                else:
                    operator_lexeme = self.parse_operators()  # Checking for anything that not a letter or a number
                    if operator_lexeme:
                        self.tokens.append(("OPERATOR", operator_lexeme))
                    else:
                        separator_lexeme = self.parse_seperators() # Checks for . , ;
                        if separator_lexeme:
                            self.tokens.append(("SEPARATOR", separator_lexeme))
                        else:
                # For simplicity, let's skip other characters
                            self.current_position += 1

        return self.tokens

    def parse_integer(self): # Method will match a digit as an integer in the file
        integer_regex = re.compile(r'\d+(\.\d+)?') # This will account for decimals as well now
        match = integer_regex.match(self.input_string[self.current_position:])
        if match:
            integer_lexeme = match.group()
            self.current_position += len(integer_lexeme)
            return integer_lexeme

    def parse_identifier(self): # Method will match strings as identifers NOT including keywords (i.e "while", "for", "if", etc)
        identifier_regex = re.compile(r'[a-zA-Z][a-zA-Z0-9]*')
        match = identifier_regex.match(self.input_string[self.current_position:])
        if match:
            identifier_lexeme = match.group()
            self.current_position += len(identifier_lexeme)
            return identifier_lexeme

    def parse_operators(self):  # Method will match characters that are *+-/ as operators
        operator_regex = re.compile(r"[*+-/=<>()><]+")
        match = operator_regex.match(self.input_string[self.current_position:])
        if match:
            operator_lexeme = match.group()
            self.current_position += len(operator_lexeme)
            return operator_lexeme
    
    def parse_seperators(self): # Method will match characters that are ():;,) as seperators
        seperator_regex = re.compile(r"[,;:]+")
        match = seperator_regex.match(self.input_string[self.current_position:])
        if match:
            seperator_lexeme = match.group()
            self.current_position += len(seperator_lexeme)
            return seperator_lexeme

    def parse_keywords(self):
        keywords = ["while", "for", "if"]  # Add more keywords as needed
        keyword_regex = re.compile(r"\b(" + "|".join(map(re.escape, keywords)) + r")\b")
        match = keyword_regex.match(self.input_string[self.current_position:])
        if match:
            keyword_lexeme = match.group()
            self.current_position += len(keyword_lexeme)
            return keyword_lexeme
 

def main():
    if os.path.exists("input.txt"): # input.txt is going to be our RE to read
        with open(f"input.txt", "r") as file:
            input_string = file.read()

        lexer = Lexer(input_string)
        tokens = lexer.tokenize()

        with open(f"output.txt", "w") as file: # Output file will be our list of tokens/lexemes
            for token, lexeme in tokens:
                file.write(f"{token}, {lexeme}\n")
                print(f"{token}, {lexeme}\n") 
    else:
        print("The file does not exist")
if __name__ == "__main__":
    main()

