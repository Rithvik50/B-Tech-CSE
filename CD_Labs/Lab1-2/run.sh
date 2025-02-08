#!/bin/bash

# Step 1: Run Lex to generate lexer code
lex lexer.l || { echo "Lex failed"; exit 1; }

# Step 2: Run Yacc to generate parser code
bison -dy parser.y || { echo "Yacc failed"; exit 1; }

# Step 3: Compile the generated files with GCC
gcc y.tab.c lex.yy.c || { echo "GCC compilation failed"; exit 1; }

# Step 4: Execute the program with input redirection
./a.out < input_file.c || { echo "Execution failed"; exit 1; }

# Step 5: Print success message
echo "Execution completed successfully."

# Step 6: Clean up
rm -f y.tab.c y.tab.h lex.yy.c a.out