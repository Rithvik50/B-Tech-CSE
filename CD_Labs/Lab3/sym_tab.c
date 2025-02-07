#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sym_tab.h"

table* init_table() {
    t = (table*)malloc(sizeof(table));
    t->head = NULL;
    return t;
}

symbol* init_symbol(char* name, int size, int type, int lineno, int scope) {
    symbol *s = (symbol*)malloc(sizeof(symbol));
    s->name = strdup(name);
    s->size = size;
    s->type = type;
    s->line = lineno;
    s->scope = scope;
    s->val = "~";
    s->next = NULL;
    return s;
}

void insert_into_table(symbol* sym) {
    symbol *s;
	if (t->head == NULL) {
		t->head = sym;
    } else {
		s = t->head;
		while (s->next != NULL) {
            s = s->next;
        }
		s->next = sym;
	}
}

int check_symbol_table(char* name) {
    symbol *s = t->head;
    while (s != NULL) {
        if (strcmp(s->name, name) == 0) {
            return 1;
        }
        s = s->next;
    }
    return 0;
}

void insert_value_to_name(char* name, char* value, int type) {
    /*
        if value is default value return back
        check if table is empty
        else traverse the table and find the name
        insert value into the entry structure
    */
}

void display_symbol_table() {
    if (t->head == NULL) {
        printf("Symbol table is empty\n");
        exit(0);
    }

    printf("----------------------------------------------------\n");
    printf("| %-10s | %-4s | %-6s | %-6s | %-5s |\n", "Name", "Size", "Type", "Line", "Scope");
    printf("----------------------------------------------------\n");

    symbol *s = t->head;
    while (s != NULL) {
        printf("| %-10s | %-4d | %-6d | %-6d | %-5d |\n", s->name, s->size, s->type, s->line, s->scope);
        s = s->next;
    }
    printf("----------------------------------------------------\n");

    symbol *s1, *s2 = NULL;
	s1 = t->head;
	while (s1->next != NULL) {
		s2 = s1;
		s1 = s1->next;
		free(s2);
	}
	free(t);
}
