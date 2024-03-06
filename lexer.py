import re # used for analyzing regular expressions


class Lexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.tokens = [] # holds the tokens
        self.current_position = 0 # current position in the text WITHIN the file

    def tokenize(self):
        while self.current_position < len(self.input_string):
            char = self.input_string[self.current_position]
            if char.isdigit(): # checks if an instance in the text is a digit
                integer_lexeme = self.parse_integer()
                self.tokens.append(("INTEGER", integer_lexeme))
            elif char.isalpha() or char == "": # checks if an instance in the text is a letter OR an empty string
                identifier_lexeme = self.parse_identifier()
                self.tokens.append(("IDENTIFIER", identifier_lexeme))
            else:
                operator_lexeme = self.parse_operators()  # Checking for anything that not a letter or a number
                seperator_lexeme = self.parse_seperators()
                if operator_lexeme:
                    self.tokens.append(("OPERATOR", operator_lexeme))
                elif seperator_lexeme:
                    self.tokens.append(("SEPERATOR", seperator_lexeme))
                else:
                # For simplicity, let's skip other characters
                        self.current_position += 1

        return self.tokens

    def parse_integer(self): # Method will match a digit as an integer in the file
        integer_regex = re.compile(r'\d+')
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
        pass

def main():

    with open(r"c:\Users\mrale\OneDrive\Desktop\output.txt") as file: 
        input_string = file.read()

    lexer = Lexer(input_string)
    tokens = lexer.tokenize()

    # Output tokens and lexemes to console
    with open("output.txt", "w") as output_file:
        for token, lexeme in tokens:
            print(f"{token}: {lexeme}\n")


if __name__ == "__main__":
    main()

    
