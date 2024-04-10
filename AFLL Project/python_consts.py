import ply.lex as lex

# List of tokens
tokens = (
    'VARIABLE_DECLARATION',
    'IF_STATEMENT',
    'WHILE_LOOP',
    'FUNCTION_DEFINITION',
    'FOR_LOOP',
    'OTHER',  # Catch-all for any other characters
)

# Regular expressions for tokens
t_VARIABLE_DECLARATION = r'[a-zA-Z_][a-zA-Z_0-9]*\s*=\s*.*'
t_IF_STATEMENT = r'if(\s?[(]\w+[=|<|>|!|(True)|(False)][=]?([\w+]|[0-9]+)[)][:])|(if\s\w+[=|<|>|!|(True)|(False)][=]?([\w+]|[0-9]+)[:])'
t_WHILE_LOOP = r'while(\s?[(][\w]+[<|>|(!=)](\w+|[0-9]+)[)][:])|while(\s?[(](True|False)[)][:])'
t_FUNCTION_DEFINITION = r'def\s\w+[(][\w+,|\w+]*[)][:]'
t_FOR_LOOP = r'for(\s\w+\s(in)\s(range)[(][0-9]+?[,]?[0-9]+[)][:])|(for\s(\w+\s(in)\s\w+)[:])'
t_OTHER = r'.'

# Error handling
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

if __name__ == "__main__":
    while True:
        code = input("Enter a Python construct (or type 'exit' to end): ")
        
        if code.lower() == 'exit':
            break  # Exit the loop if the user enters 'exit'
        
        lexer.input(code)
        token_found = False

        for token in lexer:
            if token.type != 'OTHER':
                token_found = True
                if token.type == 'VARIABLE_DECLARATION':
                    print("Valid and Variable Declaration")
                elif token.type == 'IF_STATEMENT':
                    print("Valid and If Statement")
                elif token.type == 'WHILE_LOOP':
                    print("Valid and While Loop")
                elif token.type == 'FUNCTION_DEFINITION':
                    print("Valid and Function Definition")
                elif token.type == 'FOR_LOOP':
                    print("Valid and For Loop")

        if not token_found:
            print("Invalid")