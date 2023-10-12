#include "lists.h"
#include <stdio.h>

/**
 * Description: print_dlistint - prints all the elements of a dlistint_t list
 *
 * Parameters:
 * -----------
 * @h: pointer points to the first node of the doubly linked list
 *
 * Return:
 * --------
 * the number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	int size = 0;

	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		size++;
	}
	return (size);
}
