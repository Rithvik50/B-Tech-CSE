#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "abstract_syntax_tree.h"

expression_node* init_exp_node(char* val, expression_node* left, expression_node* middle, expression_node* right)
{
	// function to allocate memory for an AST node and set the left and right children of the nodes
	expression_node* node = (expression_node*)malloc(sizeof(expression_node));
	node->left = left;
	node->middle = middle;
	node->right = right;
	node->val = val;
	return node;
}

void helper(expression_node* exp_node, int first)
{
	if(exp_node != NULL) {
		if(first) {
			printf("%s",exp_node->val);
			first = 0;
		}
		else {
			printf(",%s", exp_node->val);
		}
		helper(exp_node->left, first);
		helper(exp_node->middle, first);
		helper(exp_node->right, first);
	}
}

void display_exp_tree(expression_node* exp_node)
{
	// traversing the AST in preorder and displaying the nodes
	int first = 1;
	helper(exp_node, first);
}