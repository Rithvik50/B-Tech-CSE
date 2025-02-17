lex lexer.l
bison -dy parser.y
gcc y.tab.c lex.yy.c
./a.out < assignment-1_nested_for_valid.c
rm -f a.out y.tab.c y.tab.h lex.yy.c