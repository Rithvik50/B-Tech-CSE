#!/bin/bash

# Step 1: Run Lex to generate lexer code
lex lexer.l || { echo "Lex failed"; exit 1; }

# Step 2: Run Yacc to generate parser code
yacc -d parser.y -Wno || { echo "Yacc failed"; exit 1; }

# Step 3: Compile the generated files with GCC, including sym_tab.c
gcc -g y.tab.c lex.yy.c sym_tab.c -ll -o parser || { echo "GCC compilation failed"; exit 1; }

# Step 4: Execute the program with input redirection
./parser < sample_input1.c > output1.txt || { echo "Execution failed"; exit 1; }

# Step 5: Print success message
echo "Execution completed successfully. Output stored in output1.txt"
