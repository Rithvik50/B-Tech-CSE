%Start ML_COMMENT
%{
#include <stdio.h>
%}
%option yylineno
%%
"//".*        { printf("Comment at line %d\n", yylineno); }
"/*"          { printf("Multi line comment starts from %d ", yylineno); BEGIN(ML_COMMENT); }
<ML_COMMENT>"*/"    { printf("Multi line comment ends at %d\n", yylineno); BEGIN(INITIAL); }
<ML_COMMENT>[^*\n]+
<ML_COMMENT>"*"
<ML_COMMENT>"\n"    { ; }
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