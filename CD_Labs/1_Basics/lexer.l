%{
    #define YYSTYPE char*
    #include "y.tab.h"
    #include <stdio.h>
    extern void yyerror(const char*); // declare the error handling function
    int yylineno;    
%}

/* Regular definitions */
digit	[0-9]
letter	[a-zA-Z]
id	({letter}|_)({letter}|{digit}|_)*
digits	{digit}+
opFraction	(\.{digits})?
opExponent	([Ee][+-]?{digits})?
number	{digits}{opFraction}{opExponent}

%%
\/\/(.*) ; // ignore comments
[\f\r\t ] ; // ignore whitespaces
\n		{++yylineno;}
"int" 		{return T_INT;}
"char"		{return T_CHAR;}
"double"	{return T_DOUBLE;}
"float"	{return T_FLOAT;}
"while" 	{return T_WHILE;}
"if"		{return T_IF;}
"else"		{return T_ELSE;}
"for"		{return T_FOR;} /* added to support for */
"do" 		{return T_DO;}
"#include" 	{return T_INCLUDE;}
"main" 	{return T_MAIN;}
\".*\"		{return T_STRLITERAL; }
"++"		{return T_INC;}   /* added to support unary increment op */
"--"		{return T_DEC;}   /* added to support unary decrement op */
"=="		{return T_EQCOMP;}
"!="		{return T_NOTEQUAL;}
">="        	{return T_GREATEREQ;}
"<="        	{return T_LESSEREQ;}
"||"        	{return T_OROR;}
"&&"        	{return T_ANDAND;}
"("		{return *yytext;}
")"		{return *yytext;}
"."         	{return *yytext;}
","         	{return *yytext;}
"{"         	{return *yytext;}
"}"         	{return *yytext;}
"["         	{return *yytext;} /* added to support arrays */
"]"         	{return *yytext;} /* added to support arrays */
"*"         	{return *yytext;}
"+"         	{return *yytext;}
";"         	{return *yytext;}
"-"         	{return *yytext;}
"/"         	{return *yytext;}
"="         	{return *yytext;}
">"         	{return *yytext;}
"<"         	{return *yytext;}
"!"         	{return *yytext;}
{number}	{return T_NUM;}
{id}\.h	{return T_HEADER;}  // ending in .h => header file name
{id}        	{return T_ID;}
.		{yyerror("Unrecognized token");}
%%







