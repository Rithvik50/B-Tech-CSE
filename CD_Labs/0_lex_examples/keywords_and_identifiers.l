digit     [0-9]
letter    [_A-Za-z]
%{
#include<stdio.h>
%}
%%
auto|double|if|static|break|else|int|struct|case|enum|long|switch|char|extern|near|typedef|const|continue|register|union|unsigned|void|while|default|do|goto|signed|while|signed|unsigned printf("Keyword :\t %s\n",yytext);
{letter}({letter}|{digit})*    printf("Valid Identifier : %s\n",yytext);
. ;
\n ;
%% 
int yywrap()
{
    return(1);
}
int main(int argc, char *argv[]) 
{   
    yyin = fopen(argv[1], "r");
    yylex();
    fclose(yyin);
    return 0;
}
