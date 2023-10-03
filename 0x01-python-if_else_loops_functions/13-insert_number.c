#include "lists.h"

/**
 * Description: insert_node - inserts a num into a soreted singly linked list
 * Input:
 *	@head: (pointer to a linked list): the head of the linked list
 *	@number: (int): value of the new node
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *curr, *new;
       
	new = malloc(sizeof(listint_t));
	if (!new)
		return NULL;
	
	new->n = number;
	curr = head;
	prev = NULL;

	/* handle empty linked list */
	if (!head)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	
	while (curr)
	{
		if (curr->n > number)
		{
			if (prev == NULL)
			{
				new->next = curr;
				*head = new;
				return (new);
			}
			break;
		}
		prev = curr;
		curr = curr->next;
	}
	prev->next = new;
	new->next = curr;
	return (new);
