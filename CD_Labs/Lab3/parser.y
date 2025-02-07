%{
    #include "sym_tab.h"
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    #define YYSTYPE char*

    void yyerror(char* s);
    int yylex();
    extern int yylineno;

    int current_type;
    int size; 
    table* sym_table; 

%}

%token T_INT T_CHAR T_DOUBLE T_WHILE T_INC T_DEC T_OROR T_ANDAND T_EQCOMP 
       T_NOTEQUAL T_GREATEREQ T_LESSEREQ T_LEFTSHIFT T_RIGHTSHIFT T_PRINTLN 
       T_STRING T_FLOAT T_BOOLEAN T_IF T_ELSE T_STRLITERAL T_DO T_INCLUDE T_HEADER T_MAIN T_ID T_NUM

%start START

%%
START : PROG { printf("Valid syntax\n"); YYACCEPT; }	
    ;	
  
PROG :  MAIN PROG				
    | DECLR ';' PROG 				
    | ASSGN ';' PROG 			
    | 					
    ;
 
DECLR : TYPE LISTVAR 
    ;	

LISTVAR : LISTVAR ',' VAR 
      | VAR
      ;

VAR: T_ID '=' EXPR  
        { 
            /*
				to be done in lab 3
			*/
        }
    | T_ID  
        { 
            if (!check_symbol_table($1)) {
                insert_into_table($1, size, current_type, yylineno, 0);
            } else {
                yyerror("Redeclared variable");
            }
        }  

TYPE : T_INT { current_type = INT; size = 4; }
     | T_FLOAT { current_type = FLOAT; size = 2; }
     | T_DOUBLE { current_type = DOUBLE; size = 8; }
     | T_CHAR { current_type = CHAR; size = 1; }
     ;
	
ASSGN : T_ID '=' EXPR  
        { 
            /*
				to be done in lab 3
			*/
        }
    ;

EXPR : EXPR REL_OP E
       | E 
       ;
	   
E : E '+' T
    | E '-' T
    | T 
    ;
	
T : T '*' F
    | T '/' F
    | F
    ;

F : '(' EXPR ')'
    | T_ID
    | T_NUM 
    | T_STRLITERAL 
    ;

REL_OP : T_LESSEREQ
       | T_GREATEREQ
       | '<' 
       | '>' 
       | T_EQCOMP
       | T_NOTEQUAL
       ;	

MAIN : TYPE T_MAIN '(' EMPTY_LISTVAR ')' '{' STMT '}';

EMPTY_LISTVAR : LISTVAR
        |	
        ;

STMT : STMT_NO_BLOCK STMT
       | BLOCK STMT
       |
       ;

STMT_NO_BLOCK : DECLR ';'
       | ASSGN ';' 
       ;

BLOCK : '{' STMT '}';

COND : EXPR 
       | ASSGN
       ;

%%

void yyerror(char* s) {
    printf("Error: %s at line %d\n", s, yylineno);
}

int main() {
    sym_table = init_table();
    yyparse();
    display_symbol_table(sym_table);
    return 0;
}
