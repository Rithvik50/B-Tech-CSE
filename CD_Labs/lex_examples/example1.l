%{
#include<stdio.h>
%}
%%
abb     printf("1");
aba     printf("2");
a       printf("3");
.   printf("X");
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
