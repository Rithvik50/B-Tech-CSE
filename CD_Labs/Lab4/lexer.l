%{
    #define YYSTYPE char*
    #include "y.tab.h"
    #include <stdio.h>
    extern void yyerror(const char *); // declare error handling function
%}

/* Regular definitions */
digit   [0-9]
letter  [a-zA-Z]
id      {letter}({letter}|{digit})*
digits  {digit}+
opFraction   (\.{digits})?
opExponent   ([Ee][+-]?{digits})?
number  {digits}{opFraction}{opExponent}

%option yylineno

%%
\/\/(.*) ; // ignore comments
[\t\n]   ; // ignore whitespace

"int"       { return T_INT; }
"char"      { return T_CHAR; }
"double"    { return T_DOUBLE; }
"float"     { return T_FLOAT; }
"while"     { return T_WHILE; }
"if"        { return T_IF; }
"else"      { return T_ELSE; }
"do"        { return T_DO; }
"#include"  { return T_INCLUDE; }
"main"      { return T_MAIN; }
\".*\"      { yylval = strdup(yytext); return T_STRLITERAL; }
"=="        { return T_EQCOMP; }
"!="        { return T_NOTEQUAL; }
">="        { return T_GREATEREQ; }
"<="        { return T_LESSEREQ; }
"("         { return *yytext; }
")"         { return *yytext; }
"."         { return *yytext; }
","         { return *yytext; }
"{"         { return *yytext; }
"}"         { return *yytext; }
"*"         { return *yytext; }
"+"         { return *yytext; }
";"         { return *yytext; }
"-"         { return *yytext; }
"/"         { return *yytext; }
"="         { return *yytext; }
">"         { return *yytext; }
"<"         { return *yytext; }
{number}    { 
    yylval = strdup(yytext);  // store number value
    return T_NUM;
}
{id}\.h     { return T_HEADER; }  // header file name
{id}        { 
    yylval = strdup(yytext); // store identifier
    return T_ID;
}
.           { } // ignore anything else

%%

int yywrap() {
    return 1;
}