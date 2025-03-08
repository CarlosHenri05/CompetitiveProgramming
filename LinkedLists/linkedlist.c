#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
  int val;
  struct node *next;
} node;

void printList(node *head)
{
  node *current = head;
  while (current != NULL)
  {
    printf("%d\n", current->val);
    current = current->next;
  }
}

void append(node *head, int n)
{
  if (head == NULL)
  {
    head = (node *)malloc(sizeof(node));
    head->val = n;
    head->next = NULL;

    return;
  }
  node *current = head;
  while (current->next != NULL)
  {
    current = current->next;
  }
  current->next = (node *)malloc(sizeof(node));
  current->next->val = n;
  current->next->next = NULL;
}

void pushToFirstIndex(node **head, int n)
{
  node *current = *head;
  node *new_node = (node *)malloc(sizeof(node));

  new_node->val = n;
  new_node->next = current;
  current = new_node;
}

void pop(node **head_ref)
{
  node *head = *head_ref;

  if (head == NULL)
  {
    return;
  }
  if (head->next == NULL)
  {
    free(head);
    *head_ref = NULL;
    return;
  }
  node *current = head;
  while (current->next->next != NULL)
  {
    current = current->next;
  }
  free(current->next);
  current->next = NULL;
}

void insert_at(node **head, int index, int val)
{
  node *new_node = (node *)malloc(sizeof(node));
  new_node->val = val;
  if (index == 0)
  {
    node *temp = *head;
    head = new_node;
    new_node->next = temp;
  }
  node *current = *head;
  int i = 0;
  while (current != NULL & i < index - 1)
  {
    current = current->next;
    i++;
  }
  if (current = NULL)
  {
    free(new_node); // vai liberar o nó caso a posição seja inválida
  }

  new_node->next = current->next;
  current->next = new_node;
}

void delete_by_value(node **head_ref, int val)
{
  node *head = *head_ref;
  if (head == NULL)
  {
    return;
  }
  if (head != NULL && head->val == val)
  {
    free(head);
  }
  node *current = head;
  while (current->next != NULL && current->val != val)
  {
    current = current->next;
  }
  if (current->next != NULL)
  {
    node *temp = current->next;
    current->next = current->next->next;
    free(temp);
  }
}

int main()
{
  // Se eu te mandei, é por que ja testei.
}
