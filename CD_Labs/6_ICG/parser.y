%{
	#include "quad_generation.c"
	#include <stdio.h>
	#include <stdlib.h>
	#include <string.h>

	#define YYSTYPE char*

	void yyerror(char* s); 											// error handling function
	int yylex(); 													// declare the function performing lexical analysis
	extern int yylineno; 											// track the line number

	FILE* icg_quad_file;
	int temp_no = 1;
	int label_no=1;
%}


%token T_ID T_NUM T_IF T_ELSE T_DO T_WHILE GTEQ LTEQ EQQ NEQ GT LT OC CC
 
/* specify start symbol */
%start START

%nonassoc T_IF
%nonassoc T_ELSE

%%
START : S { 
		printf("-----------------------------------------------------\n");
		printf("Valid syntax\n");
		YYACCEPT;
	};
	 			

/* Grammar for assignment */
ASSGN : T_ID '=' E	{		
		quad_code_gen($1, $3, "=", " ");			
	}
;

/* Expression Grammar */
E : E '+' T 	{	
		$$ = new_temp();
		quad_code_gen($$, $1, "+", $3);
	}
	| E '-' T 	{	
		$$ = new_temp();
		quad_code_gen($$, $1, "-", $3);
	}
	| T
;
	
	
T : T '*' F 	{	
		$$ = new_temp();
		quad_code_gen($$, $1, "*", $3);
	}
	| T '/' F 	{		
		$$ = new_temp();
		quad_code_gen($$, $1, "/", $3);
	}
	| F
;

F : '(' E ')' 	{		
		$$=strdup($2);
	}
	| T_ID 		{		
		$$=strdup($1);
	}
	| T_NUM 	{		
		$$=strdup($1);
	}
;
	
S : T_IF '('C')' OC S CC {quad_code_gen($3,"","Label","");} S 
	| T_IF '('C')' OC S CC {
		$2 = new_label();
		quad_code_gen($2,"","goto","");		
		quad_code_gen($3,"","Label","");} T_ELSE OC S CC {quad_code_gen($2,"","Label","");}S
	| T_DO OC S CC T_WHILE '('C')' ';' {
		char* L1 = new_label();
		char* L2 = new_label();
		quad_code_gen(L2,"","Label","");
		quad_code_gen($6,"","if","");
		quad_code_gen(L1,"","goto","");
		quad_code_gen(L2,"","Label","");
	}
	| T_WHILE '('C')' OC S CC {
		char* L1 = new_label();
		char* L2 = new_label();
		quad_code_gen(L1,"","Label","");
		quad_code_gen($3,"","if","");
		quad_code_gen(L2,"","goto","");
		quad_code_gen($5,"","Label","");
		quad_code_gen(L1,"","goto","");
		quad_code_gen(L2,"","Label","");
	}
	| ASSGN ';' S 
	| '{' S '}'
	| 
	;

C : E rel E  {	
		$$ = new_temp();
		quad_code_gen($$, $1, $2, $3);
		$1 = new_label();
		quad_code_gen($1,$$,"if","");	
		$$ = new_label();
		quad_code_gen($$,"","goto","");
		quad_code_gen($1,"","Label","");	
	}
;

rel :  GT {strcpy($$,">");}
     | LT {strcpy($$,"<");}
     | LTEQ {strcpy($$,"<=");}
     | GTEQ {strcpy($$,">=");}
     | EQQ {strcpy($$,"==");}
     | NEQ {strcpy($$,"!=");}
     ;

%%


/* error handling function */
void yyerror(char* s)
{
	printf("Error :%s at %d \n",s,yylineno);
}

int yywrap() {
    return 1;
}

/* main function - calls the yyparse() function which will in turn drive yylex() as well */
int main(int argc, char* argv[])
{
	printf("Generated Intermediate Code \n");
	printf("-----------------------------------------------------\n");
    	printf("| %-10s | %-10s | %-10s | %-10s |\n", "op", "arg1", "arg2", "result");
    	printf("-----------------------------------------------------\n");
	yyparse();
	return 0;
}