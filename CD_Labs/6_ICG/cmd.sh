lex lexer.l
bison -dy parser.y
gcc y.tab.c lex.yy.c
./a.out < test_input_2.c
rm -f a.out y.tab.c y.tab.h lex.yy.c
