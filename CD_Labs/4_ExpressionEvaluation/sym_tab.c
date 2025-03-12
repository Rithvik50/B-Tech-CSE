#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sym_tab.h"

// Allocate memory for a symbol table
table* allocate_space_for_table() {
    table *t = (table*)malloc(sizeof(table));
    if (t) {
        t->head = NULL;
    }
    return t;
}

// Allocate memory for a symbol table entry
symbol* allocate_space_for_table_entry(const char *name, int type, int lineno, int scope) {
    symbol *s = (symbol*)malloc(sizeof(symbol));
    if (s) {
        s->name = (char*)malloc(strlen(name) + 1);
        strcpy(s->name, name);
        s->size = size_type_map[type];
        s->type = type;
        s->line = lineno;
        s->scope = scope;
        s->val = (char*)malloc(32);
        strcpy(s->val, "~");
        s->next = NULL;
    }
    return s;
}

// Insert a symbol into the table
int insert_into_table(const char *name, int type, int lineno, int scope) {
    symbol *s = allocate_space_for_table_entry(name, type, lineno, scope);
    if (!s) {
        fprintf(stderr, "Memory allocation failed for symbol: %s\n", name);
        return 1;
    }

    if (!t->head) {
        t->head = s;
    } else {
        symbol *curr = t->head;
        while (curr) {
            if (!strcmp(curr->name, name) && curr->scope == scope) {
                fprintf(stderr, "Error: %s cannot be redeclared in the same scope\n", name);
                free(s->name);
                free(s->val);
                free(s);
                return 1;
            }
            if (!curr->next) break;
            curr = curr->next;
        }
        curr->next = s;
    }
    return 0;
}

// Check if a symbol exists in the table
symbol* check_symbol_table(const char *name, int scope) {
    symbol *curr = t->head;
    while (curr) {
        if (!strcmp(curr->name, name) && curr->scope == scope) {
            return curr;
        }
        curr = curr->next;
    }
    return NULL;
}

// Insert a value into a symbol entry
int insert_value_to_name(const char *name, const char *val, int scope) {
    if (!strcmp(val, "~")) return 1;

    symbol *curr = t->head, *prev_scope = NULL;
    while (curr) {
        if (!strcmp(curr->name, name)) {
            if (curr->scope == scope) {
                strncpy(curr->val, val, 32);
                return 0;
            } else if (curr->scope < scope) {
                prev_scope = curr;
            }
        }
        curr = curr->next;
    }

    if (prev_scope) {
        strncpy(prev_scope->val, val, 32);
        return 0;
    }
    fprintf(stderr, "Error: %s has not been declared\n", name);
    return 1;
}

// Retrieve a symbol from the table
symbol* get_symbol(const char *name, int scope) {
    symbol *curr = t->head, *prev_scope = NULL;
    while (curr) {
        if (!strcmp(curr->name, name)) {
            if (curr->scope == scope) return curr;
            else if (curr->scope < scope) prev_scope = curr;
        }
        curr = curr->next;
    }
    if (!prev_scope) fprintf(stderr, "Error: %s has not been declared\n", name);
    return prev_scope;
}

// Insert value directly into a symbol
int insert_value_to_symbol(const symbol *s, const char *val) {
    if (s) {
        strcpy(s->val, val);
        return 0;
    }
    return 1;
}

// Determine the type of a value
int get_type(const char *val) {
    if (val[0] == '\'' && val[strlen(val) - 1] == '\'' && strlen(val) < 5) return CHAR;
    if (strchr(val, '.')) {
        char *endptr;
        strtod(val, &endptr);
        return (*endptr == '\0') ? DOUBLE : FLOAT;
    }
    for (int i = 0; val[i] != '\0'; i++) {
        if (val[i] < '0' || val[i] > '9') return -1;
    }
    return INT;
}

// Display the symbol table
void display_symbol_table() {
    printf("-------------------------------------------------------------\n");
    printf("| %-10s | %-4s | %-6s | %-6s | %-5s | %-10s |\n", "Name", "Size", "Type", "Line", "Scope", "Value");
    printf("-------------------------------------------------------------\n");
    
    symbol *curr = t->head;
    while (curr) {
        printf("| %-10s | %-4d | %-6d | %-6d | %-5d | %-10s |\n", 
               curr->name, curr->size, curr->type, curr->line, curr->scope, curr->val);
        curr = curr->next;
    }
    printf("-------------------------------------------------------------\n");
}
