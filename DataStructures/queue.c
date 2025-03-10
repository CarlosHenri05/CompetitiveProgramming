#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
  int val;
  struct node *next;
} node;

void print_queue(node *head)
{
  node *current = head;
  while (current != NULL)
  {
    printf("%d\n", current->val);
    current = current->next;
  }
}

void add(node *head, int n)
{
  node *current = head;

  while (current->next != NULL)
  {
    current = current->next;
  }
  current->next = (node *)malloc(sizeof(node));
  current->next->val = n;
  current->next->next = NULL;
}

void removeFirstNode(node **head)
{
  node *next_node = NULL;

  if (*head == NULL)
  {
    exit(0);
  }

  next_node = (*head)->next;
  free(*head);
  *head = next_node;
}

int peek(node *head)
{
  return head->val;
}

int main()
{
  node *queue = (node *)malloc(sizeof(node));

  queue->val = 10;

  queue->next = NULL;

  print_queue(queue);

  add(queue, 20);

  print_queue(queue);

  removeFirstNode(&queue);

  print_queue(queue);

  printf("%d", peek(queue));
}
