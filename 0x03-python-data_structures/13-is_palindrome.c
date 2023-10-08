#include "lists.h"


listint_t *list_tail(listint_t *);


/**
 * Description: is_palindrome - checks if a singly linked list is a palindrome
 *
 * Args:
 *	@head: (pointer): head of the linked list
 *
 * Return: 0 if it's not a palindrome, 1 if it's a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *start = *head, *end = list_tail(start);

	if (!start || start == end)
		return (1);

	while (start)
	{
		if (start->n == end->n)
		{
			start = start->next;
			if (start == end || start->next == end)
				return (1);
			temp = start->next;
			while (temp)
			{
				if (temp->next == end)
				{
					end = temp;
					break;
				}
				temp = temp->next;
			}
		}
		else
			break;
	}
	return (0);
}


/**
 * Description: list_tail - returns a pointer to last node in a linked list
 *
 * Args:
 *	@head: (pointer): head of the linked list
 *
 * Return: pointer to last node
 */
listint_t *list_tail(listint_t *head)
{
	listint_t *end = NULL;

	while (head)
	{
		if (head->next == NULL)
			end = head;
		head = head->next;
	}
	return (end);
}

