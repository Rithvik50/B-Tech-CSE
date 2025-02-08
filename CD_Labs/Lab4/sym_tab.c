#include "sym_tab.h"

// Define the global symbol table
struct symbol symtab[100];
int symtab_index = 0;

// Initialize symbol table
void init_table() {
    symtab_index = 0;
}

// Find a symbol in the table
int find_symbol(char* name, int scope) {
    for(int i = 0; i < symtab_index; i++) {
        if(strcmp(symtab[i].name, name) == 0 && symtab[i].scope == scope) {
            return i;
        }
    }
    return -1;
}

// Insert a symbol into the table
void insert_symbol(char* name, int size, int type, int lineno, int scope, char* value) {
    symtab[symtab_index].name = strdup(name);
    symtab[symtab_index].size = size;
    symtab[symtab_index].type = type;
    symtab[symtab_index].lineno = lineno;
    symtab[symtab_index].scope = scope;
    symtab[symtab_index].value = value ? strdup(value) : NULL;
    symtab_index++;
}

// Update symbol value
void update_symbol_value(int index, char* value) {
    if(symtab[index].value) {
        free(symtab[index].value);
    }
    symtab[index].value = strdup(value);
}

// Display symbol table
void display_symbol_table() {
    printf("Name\tsize\ttype\tlineno\tscope\tvalue\n");
    for(int i = 0; i < symtab_index; i++) {
        printf("%s\t%d\t%d\t%d\t%d\t%s\n", 
            symtab[i].name, 
            symtab[i].size, 
            symtab[i].type, 
            symtab[i].lineno,
            symtab[i].scope,
            symtab[i].value ? symtab[i].value : "");
    }
}

// Get type size
int get_size(int type) {
    switch(type) {
        case 1: return 1;  // char
        case 2: return 2;  // int
        case 3: return 4;  // float
        case 4: return 8;  // double
        default: return 0;
    }
}
