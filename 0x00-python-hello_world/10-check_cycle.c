#include "lists.h"

/**
 * Description: check_cycle - checks if there is a cycle in the linkedlist
 * Input:
 *	@list: (pointer to node): points to the first node of the linked list
 * Return:
 *	- 0 if there is no cycle
 *	- 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
