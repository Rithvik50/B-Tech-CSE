%{
    #include "sym_tab.c"
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    #define YYSTYPE char*

    void yyerror(char* s);
    int yylex();

    extern int yylineno;
    int type;
    int scope = 1;
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

VAR: T_ID '=' EXPR  
        { 
            if (!check_symbol_table($1)) {
                symbol *s = init_symbol($1, get_size(type), type, yylineno, scope);
                insert_into_table(s);
                insert_value_to_name($1, $3, type);
            } else {
                yyerror($1);
            }
        }
    | T_ID  
        { 
            if (!check_symbol_table($1)) {
                symbol *s = init_symbol($1, get_size(type), type, yylineno, scope);
                insert_into_table(s);
            } else {
                printf("Variable %s already declared\n", $1);
                yyerror($1);
            }
        }   

TYPE : T_INT { type = INT; }
     | T_FLOAT { type = FLOAT; }
     | T_DOUBLE { type = DOUBLE; }
     | T_CHAR { type = CHAR; }
     ;
	
ASSGN : T_ID '=' EXPR  
        { 
            if (check_symbol_table($1)) {
                symbol *s = t->head;
                while (s != NULL) {
                    if (strcmp(s->name, $1) == 0) {
                        if (s->type != type) {
                            printf("Mismatch type\n");
                            yyerror($3);
                        }
                        insert_value_to_name($1, $3, s->type);
                        break;
                    }
                    s = s->next;
                }
            } else {
                yyerror("Variable not declared before use");
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

BLOCK : '{' 
         { scope++; } 
       STMT 
       '}' 
         { scope--; };

COND : EXPR 
       | ASSGN
       ;
%%

void yyerror(char* s) {
    printf("Error: %s at line %d\n", s, yylineno);
}

int main() {
    init_table();
    yyparse();
    display_symbol_table();
    return 0;
}
