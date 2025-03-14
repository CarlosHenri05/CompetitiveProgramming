#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
  int val;
  struct node *next;
} node;

// lista[0]

void print_list(node *head)
{
  node *current = head;
  while (current != NULL)
  {
    printf("Current: %d ", current->val);
    current = current->next;
  }
}

void push(node *head, int val)
{
  node *current = head;
  while (current->next != NULL)
  {
    current = current->next;
  }
  current->next = (node *)malloc(sizeof(node));
  current->next->val = val;
  current->next->next = NULL;
}

void pop(node *head)
{
  if (head == NULL)
  {
    printf("Error");
    exit(0);
  }

  node *current = head;

  if (current->next == NULL)
  {
    free(current);
  }

  while (current->next->next != NULL)
  {
    current = current->next;
  }
  free(current->next);
}

int main()
{
  node *head = (node *)malloc(sizeof(node));

  head->val = 10;
  head->next = NULL;

  push(head, 20);

  pop(&head);

  print_list(head);
}
