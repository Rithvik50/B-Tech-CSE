#ifndef SYM_TAB_H
#define SYM_TAB_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Symbol table entry structure
struct symbol {
    char* name;
    int size;
    int type;
    int lineno;
    int scope;
    char* value;
};

// Make symtab accessible to other files
extern struct symbol symtab[100];
extern int symtab_index;

// Function declarations
void init_table();
int find_symbol(char* name, int scope);
void insert_symbol(char* name, int size, int type, int lineno, int scope, char* value);
void update_symbol_value(int index, char* value);
void display_symbol_table();
int get_size(int type);

#endif