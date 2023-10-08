#include "lists.h"


int list_len(listint_t *);


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
	listint_t *start = *head;
	int len = list_len(start), *arr, i, j;

	if (len == 0  || len == 1)
		return (1);

	arr = malloc(sizeof(int) * (len / 2));

	for (i = 0; i < len / 2; i++)
	{
		arr[i] = start->n;
		start = start->next;
	}

	if (len % 2 != 0)
	{
		start = start->next;
		i++;
	}

	j = 0;
	for (; i < len; i++)
	{
		if (start->n == arr[j])
			start = start->next;
		else
			return (0);
		j++;
	}
	return (1);
}


/**
 * Description: list_len - returns the length of a linked list
 *
 * Args:
 *	@head: (pointer): head of the linked list
 *
 * Return: length of the linked list
 */
int list_len(listint_t *head)
{
	int size = 0;

	while (head)
	{
		head = head->next;
		size++;
	}
	return (size);
}

