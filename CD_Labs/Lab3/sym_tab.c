#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sym_tab.h"

table* init_table()	
{
	/*
        allocate space for table pointer structure eg (t_name)* t
        initialise head variable eg t->head
        return structure
    */
    table* t = (table*)malloc(sizeof(table));
    t -> head = NULL;
    return t;
}

symbol* init_symbol(char* name, int size, int type, int lineno, int scope) //allocates space for items in the list
{
	/*
        allocate space for entry pointer structure eg (s_name)* s
        initialise all struct variables(name, value, type, scope, length, line number)
        return structure
    */
    symbol* s = (symbol*)malloc(sizeof(symbol));
    s -> name = (char*)malloc(sizeof(char)*(strlen(name)+1));
    strcpy(s->name, name);
    s -> size = size;
    s -> type = type;
    s -> line = lineno;
    s -> scope = scope;
    s -> val = (char*)malloc(sizeof(char)*10);
    strcpy(s->val, "~");
    return s;
}

insert_into_table(char* name, int size, int type, int lineno, int scope)
/* 
    arguments can be the structure s_name already allocated before this function call
    or the variables to be sent to allocate_space_for_table_entry for initialisation        
*/
{
    /*
        check if table is empty or not using the struct table pointer
        else traverse to the end of the table and insert the entry
    */
    symbol* s = init_symbol(name, size, type, lineno, scope);
    if (t->head == NULL) {
        t -> head = s;
        return;
    }
    symbol* curr = t -> head;
    while (curr->next != NULL) {
        curr = curr -> next;
    }
    curr -> next = s;
}

check_symbol_table(name) //return a value like integer for checking
{
    /*
        check if table is empty and return a value like 0
        else traverse the table
        if entry is found return a value like 1
        if not return a value like 0
    */
    if (t->head == NULL) {
        return 0;
    }
    symbol* curr = t -> head;
}

insert_value_to_name(name,value)
{
    /*
        if value is default value return back
        check if table is empty
        else traverse the table and find the name
        insert value into the entry structure
    */
    if (strcmp(value, "~") == 0) {
        return;
    }
    if (t->head == NULL) {
        return;
    }
    symbol* curr = t -> head;
    while (curr != NULL) {
        if (strcmp(curr->name, name) == 0) {
            strcpy(curr->val, value);
            return;
        }
        curr = curr -> next;
    }
}

display_symbol_table()
{
    /*
        traverse through table and print every entry
        with its struct variables
    */
    symbol* curr = t -> head;
    if (curr == NULL) {
        return;
    }
    print("Name\tsize\ttype\tlineno\tscope\tvalue\n");
    while (curr != NULL) {
        printf("%s\t%d\t%d\t%d\t%d\t%s\n", curr->name, curr->size, curr->type, curr->line, curr->scope, curr->val);
        curr = curr -> next;
    }
}
