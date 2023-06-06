#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a
 * cycle in it.
 * list: pointer variable to of type listint_t
 * Return: 0 upon success
 */

int check_cycle(listint_t *list)
{
	listint_t *iter1;
	listint_t *iter2;

	iter1 = list;
	iter2 = list;
	if (list == NULL)
	{
		return (0);
	}
	iter2 = iter2->next;
	while (iter2 != NULL && iter2->next != NULL && iter1 != NULL)
	{
		if (iter1 == iter2)
		{
			return (1);
		}
		iter1 = iter1->next;
		iter2 = iter2->next->next;
	}
	return (0);
}
