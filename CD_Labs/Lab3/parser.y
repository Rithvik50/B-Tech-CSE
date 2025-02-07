%{
    #include "sym_tab.c"
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #define YYSTYPE char*

    void yyerror(char* s); // error handling function
    int yylex(); // function performing lexical analysis
    extern int yylineno; // track the line number

    int curr_type; // To store the current variable type
%}

%token T_INT T_CHAR T_DOUBLE T_WHILE T_INC T_DEC T_OROR T_ANDAND T_EQCOMP T_NOTEQUAL 
       T_GREATEREQ T_LESSEREQ T_LEFTSHIFT T_RIGHTSHIFT T_PRINTLN T_STRING T_FLOAT 
       T_BOOLEAN T_IF T_ELSE T_STRLITERAL T_DO T_INCLUDE T_HEADER T_MAIN T_ID T_NUM

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

VAR: T_ID '=' EXPR {
        /*
            Check if variable exists in the symbol table.
            If it does, return an error (reassignment should be handled in ASSGN).
            Otherwise, insert into the table with the assigned value.
        */
        if (check_symbol_table($1)) {
            printf("Error: Redeclaration of variable %s at line %d\n", $1, yylineno);
        } else {
            insert_into_table($1, sizeof(int), curr_type, yylineno, 0); // Using int size as placeholder
            insert_value_to_name($1, $3, curr_type); // Insert the assigned value
        }
    }
    | T_ID {
        /*
            Check if the variable is already in the symbol table.
            If it is, print an error (redeclaration not allowed).
            Otherwise, insert the variable into the table.
        */
        if (check_symbol_table($1)) {
            printf("Error: Redeclaration of variable %s at line %d\n", $1, yylineno);
        } else {
            insert_into_table($1, sizeof(int), curr_type, yylineno, 0); // Using int size as placeholder
        }
    };

TYPE : T_INT { curr_type = INT; }  
     | T_FLOAT { curr_type = FLOAT; }  
     | T_DOUBLE { curr_type = DOUBLE; }  
     | T_CHAR { curr_type = CHAR; }  
     ;

/* Grammar for assignment */   
ASSGN : T_ID '=' EXPR {
        /*
            Check if the variable exists in the table.
            If not, print an error.
            Otherwise, update the value in the table.
        */
        if (!check_symbol_table($1)) {
            printf("Error: Variable %s not declared at line %d\n", $1, yylineno);
        } else {
            insert_value_to_name($1, $3, curr_type);
        }
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

/* Grammar for main function */
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

/* error handling function */
void yyerror(char* s)
{
    printf("Error: %s at line %d\n", s, yylineno);
}

int main(int argc, char* argv[])
{
    /* Initialize the symbol table */
    t = init_table();
    
    /* Start parsing */
    yyparse();

    /* Display final symbol table */
    display_symbol_table();
    
    return 0;
}
