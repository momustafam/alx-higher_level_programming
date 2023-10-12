#ifndef DOUBLY_LLIST
#define DOUBLY_LLIST

#include <stddef.h>


/**
 * Description: dlistint_t - node of a doubly linked list
 * @data: node data
 * @next: pointer points to the next node
 * @prev: pointer points to the previoud node
 */
typedef struct dlistint_t
{
	int n;
	struct dlistint_t *next;
	struct dlistint_t *prev;
} dlistint_t;

size_t print_dlistint(const dlistint_t *h);

#endif
