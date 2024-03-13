# Cpsc-323
Project-01

The following program is a lexer that translates a string from a file (input.txt) into tokens, and lexemes. Then once identified, and labeled appropiately a table with those tokens, and lexemes are outputted; once to the console, and once in a table form to another file (output.txt). 


Features:
+ The program is written a FSA form, therefore houses states; they are follows:


START: Is the inital state where the lexer starts to process each character of the input, and then identifies the character, and parse a token(i.e Separator, Operator), which will then which to another state accordingly.

REAL: This state is entered whenever a digit, or decimal point is caught in the START state. From here the lexer will parse a Real token.

IDENTIFIER: This state is entered when the lexer encounters an alphabetic character while in the START state. The lexer now enters the process of parsing an identifier token. However, lexer continues to accumulate alphanumeric characters and underscores until it encounters a non-alphanumeric character, at which point it determines whether the accumulated characters in the input buffer is a Keyword or an Identifier. Lastly, this state will parse a Keyword, or Identifier token depending on the outcome.

FINAL: This state is encounter once the end of the input string occurs, and goes back to the START state. This marks the end for the FSA lexer. 

+ Outputs a table of tokens, and lexemes in a tabular form