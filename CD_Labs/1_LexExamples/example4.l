%{
#include<stdio.h>
%}
%%
a*b*    printf("1");
aab     printf("2");
bb      printf("3");
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