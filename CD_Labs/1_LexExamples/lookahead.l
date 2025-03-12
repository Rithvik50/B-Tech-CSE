letter    [A-Za-z]
%{
#include<stdio.h>
%}
%%
IF/\(.*\){letter}*   printf("FORTRAN IF detected");
. ;
\n ;
%% 
int yywrap()
{
    return (1); 
}
int main(int argc, char *argv[]) 
{   
    yyin = fopen(argv[1], "r");
    yylex();
    fclose(yyin);
    return 0;
}
