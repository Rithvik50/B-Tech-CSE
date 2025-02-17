lex lexer.l
bison -dy parser.y
gcc y.tab.c lex.yy.c
./a.out < assignment-1_simple_for_valid.c > output.txt
rm -f a.out y.tab.c y.tab.h lex.yy.c