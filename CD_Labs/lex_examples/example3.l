%{
#include<stdio.h>
%}
%%
aa          printf("1");
b?a+b?      printf("2");
b?a*b?      printf("3");
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