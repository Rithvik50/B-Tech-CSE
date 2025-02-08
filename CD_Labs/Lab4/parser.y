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
    int current_scope = 1;
    char temp[100];
%}

%token T_INT T_CHAR T_DOUBLE T_WHILE T_INC T_DEC T_OROR T_ANDAND T_EQCOMP T_NOTEQUAL 
%token T_GREATEREQ T_LESSEREQ T_LEFTSHIFT T_RIGHTSHIFT T_PRINTLN T_STRING T_FLOAT 
%token T_BOOLEAN T_IF T_ELSE T_STRLITERAL T_DO T_INCLUDE T_HEADER T_MAIN T_ID T_NUM

%start START

%%

START : PROG { printf("Valid syntax\n"); YYACCEPT; }
      ;

PROG : MAIN PROG
     | DECLR ';' PROG
     | ASSGN ';' PROG
     |
     ;

DECLR : TYPE LISTVAR
      ;

LISTVAR : LISTVAR ',' VAR
        | VAR
        ;

VAR : T_ID '=' EXPR {
        int idx = find_symbol($1, current_scope);
        if(idx != -1) {
            printf("Variable %s already declared\n", $1);
            printf("Error :%s at %d\n", $1, yylineno);
        } else {
            insert_symbol($1, get_size(current_type), current_type, yylineno, current_scope, $3);
        }
    }
    | T_ID {
        int idx = find_symbol($1, current_scope);
        if(idx != -1) {
            printf("Variable %s already declared\n", $1);
            printf("Error :%s at %d\n", $1, yylineno);
        } else {
            insert_symbol($1, get_size(current_type), current_type, yylineno, current_scope, NULL);
        }
    }
    ;

TYPE : T_INT { current_type = 2; }
     | T_FLOAT { current_type = 3; }
     | T_DOUBLE { current_type = 4; }
     | T_CHAR { current_type = 1; }
     ;

ASSGN : T_ID '=' EXPR {
        int idx = find_symbol($1, current_scope);
        if(idx == -1) {
            printf("Variable %s not declared\n", $1);
            printf("Error :%s at %d\n", $1, yylineno);
        } else {
            update_symbol_value(idx, $3);
        }
    }
    ;

EXPR : EXPR REL_OP E { $$ = $1; }
     | E { $$ = $1; }
     ;

E : E '+' T {
        sprintf(temp, "%f", atof($1) + atof($3));
        $$ = strdup(temp);
    }
    | E '-' T {
        sprintf(temp, "%f", atof($1) - atof($3));
        $$ = strdup(temp);
    }
    | T { $$ = $1; }
    ;

T : T '*' F {
        sprintf(temp, "%f", atof($1) * atof($3));
        $$ = strdup(temp);
    }
    | T '/' F {
        if(atof($3) != 0) {
            sprintf(temp, "%f", atof($1) / atof($3));
            $$ = strdup(temp);
        } else {
            yyerror("Division by zero");
            $$ = strdup("0");
        }
    }
    | F { $$ = $1; }
    ;

F : '(' EXPR ')' { $$ = $2; }
    | T_ID {
        int idx = find_symbol($1, current_scope);
        if(idx == -1) {
            printf("Variable %s not declared\n", $1);
            printf("Error :%s at %d\n", $1, yylineno);
            $$ = strdup("0");
        } else if(!symtab[idx].value) {
            printf("Variable %s not initialized\n", $1);
            printf("Error :%s at %d\n", $1, yylineno);
            $$ = strdup("0");
        } else {
            $$ = strdup(symtab[idx].value);
        }
    }
    | T_NUM { $$ = $1; }
    | T_STRLITERAL { $$ = $1; }
    ;

REL_OP : T_LESSEREQ
       | T_GREATEREQ
       | '<'
       | '>'
       | T_EQCOMP
       | T_NOTEQUAL
       ;

MAIN : TYPE T_MAIN '(' EMPTY_LISTVAR ')' '{' STMT '}'
     ;

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

BLOCK : '{' STMT '}'
      ;

%%

void yyerror(char* s) {
    printf("Error :%s at %d \n", s, yylineno);
}

int main(int argc, char* argv[]) {
    init_table();
    yyparse();
    display_symbol_table();
    return 0;
}