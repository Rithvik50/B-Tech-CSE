#!/bin/bash

# Step 1: Run Lex to generate lexer code
lex lexer.l || { echo "Lex failed"; exit 1; }

# Step 2: Run Yacc to generate parser code
bison -dy parser.y || { echo "Yacc failed"; exit 1; }

# Step 3: Compile the generated files with GCC
gcc y.tab.c lex.yy.c || { echo "GCC compilation failed"; exit 1; }

# Step 4: Clean up
rm -f y.tab.c y.tab.h lex.yy.c

# Step 5: Execute the program with input redirection
./a.out < input_file.c || { echo "Execution failed"; exit 1; }

# Step 6: Remove a.out
rm -f a.out

# Step 7: Print success message
echo "Execution completed successfully."
