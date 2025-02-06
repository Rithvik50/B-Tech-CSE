%{
    int nchar, nword, nline;
%}
%%
\n         { nline++; nchar++; }
[^ \t\n]+  { nword++, nchar += yyleng; }
.          { nchar++; }
%%
int yywrap()
{
    return(1);
}
int main(int argc, char *argv[])  {
    yyin = fopen(argv[1], "r");
    yylex();
    printf("Number of Characters : %d\nNumber of Words: %d\nNumber of lines: %d\n", nchar, nword, nline);
    return 0;
}
