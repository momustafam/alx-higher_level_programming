#include "lists.h"


listint_t *reverse_list(listint_t *);


/**
 * Description: is_palindrome - checks if a singly linked list is a palindrome
 *
 * Args:
 *	@head: (pointer): head of the linked list being checked
 * Return: 0 if it's not a plaindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *q1 = *head, *q2 = *head, *temp = *head;
	int len = 0, i = 1, q1_end, q2_start;

	/* get the length of the linked list */
	while (temp)
	{
		len++;
		temp = temp->next;
	}
	
	/* handle the linked list if it is empty or with one node */
	if (len == 1 || len == 0)
		return (1);

	/* store the index of end of first half and start of the second one */
	q1_end = len / 2;
	q2_start = (len % 2 == 0) ? (len / 2 + 1) : (len / 2 + 2);

	/* split the linked list to two sublists q1, and q2 */
	while (1)
	{
		if (i = q1_end)
		{
			temp = q2;
			q2 = q2->next;
			temp->next = NULL;
			q2 = (++i == q2_start) ? q2 : q2->next;
			q2 = reverse_list(q2);
			break;
		}
		i++;
		q2 = q2->next;
	}

	/* comapre each element in q1 with the corresponding one in q2 */
	while (q2)
	{
		if (q2->n == q1->n)
		{
			q2 = q2->next;
			q1 = q1->next;
		}
		else
			return (0);
	}
	return (1);
}


/**
 * Description: reverse_list - reverses a linke list
 *
 * Args:
 *	head: (pointer): the head of the linked list
 *
 * Return: a pointer to the new head of the reversed linke list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *temp, *prev = NULL;
	while (head)
	{
		temp = head;
		head = head->next;
		temp->next = prev;
		prev = temp;
	}
	return (temp);
}
