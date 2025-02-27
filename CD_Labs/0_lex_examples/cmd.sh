lex lexer.l
gcc lex.yy.c
./a.out
rm -f a.out lex.yy.c
