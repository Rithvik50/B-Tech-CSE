#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sym_tab.h"

table* init_table() {
    table* t = (table*)malloc(sizeof(table));
    t->head = NULL;
    return t;
}

symbol* init_symbol(char* name, int size, int type, int lineno, int scope) {
    symbol* s = (symbol*)malloc(sizeof(symbol));
    s->name = strdup(name);
    s->size = size;
    s->type = type;
    s->line = lineno;
    s->scope = scope;
    s->val = "~";
    s->next = NULL;
    return s;
}

void insert_into_table(char* name, int size, int type, int lineno, int scope) {
    symbol* s = init_symbol(name, size, type, lineno, scope);
    if (t->head == NULL) {
        t->head = s;
    } else {
        symbol* temp = t->head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = s;
    }
}

int check_symbol_table(char* name) {
    symbol* temp = t->head;
    while (temp != NULL) {
        if (strcmp(temp->name, name) == 0) {
            return 1;  // Symbol found
        }
        temp = temp->next;
    }
    return 0;  // Symbol not found
}

void insert_value_to_name(char* name, char* value) {
    symbol* temp = t->head;
    while (temp != NULL) {
        if (strcmp(temp->name, name) == 0) {
            free(temp->val);
            temp->val = strdup(value);
            return;
        }
        temp = temp->next;
    }
}

void display_symbol_table() {
    if (t->head == NULL) {
        printf("Symbol table is empty\n");
        return;
    }

    printf("----------------------------------------------------\n");
    printf("| %-10s | %-4s | %-6s | %-6s | %-5s |\n", "Name", "Size", "Type", "Line", "Scope");
    printf("----------------------------------------------------\n");

    symbol* temp = t->head;
    while (temp != NULL) {
        printf("| %-10s | %-4d | %-6d | %-6d | %-5d |\n", temp->name, temp->size, temp->type, temp->line, temp->scope);
        temp = temp->next;
    }
    printf("----------------------------------------------------\n");
}
