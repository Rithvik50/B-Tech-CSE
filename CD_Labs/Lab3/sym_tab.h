#define CHAR 1
#define INT 2
#define FLOAT 3
#define DOUBLE 4

typedef struct symbol {
    char* name;   // Identifier name
    int size;     // Storage size of identifier name
    int type;     // Identifier type
    char* val;    // Value of the identifier
    int line;     // Declared line number
    int scope;    // Scope of the variable
    int value; 
    struct symbol* next;
} symbol;

typedef struct table {
    symbol* head;
} table;

table* init_table(); // Allocate space for a new symbol table

symbol* init_symbol(char* name, int size, int type, int lineno, int scope);  // Creates a new symbol entry

void insert_into_table(char* name, int size, int type, int lineno, int scope); // Inserts a new symbol into the table

int check_symbol_table(char* name); // Checks if a variable exists in the symbol table

void insert_value_to_name(char* name, char* value); // Assigns a value to a variable in the symbol table

void display_symbol_table(); // Displays the symbol table
