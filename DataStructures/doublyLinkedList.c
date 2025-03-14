#include <stdio.h>
#include <stdlib.h>

// Essa estrutura de dados segue a mesma lógica de uma linked list normal, só que com ela conseguimos "navegar" para os dois lados da lista e também operar desses dois lados.
typedef struct node
{
  int val;
  struct node *next;
  struct node *prev;

} node;

void traverse_forwards(node *head)
{
  node *current = head;
  while (current != NULL)
  {
    printf("%d\n", current->val);
    current = current->next;
  }
}

void traverse_backwards(node *tail)
{
  node *current = tail;
  while (current != NULL)
  {
    printf("%d\n", current->val);
    current = current->prev;
  }
}

// Adicionar elemento no final da lista
void append(node *head, int val)
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
// Remover elemento do final da lista
void pop(node *head)
{
  if (head == NULL)
    exit(0);
  if (head->next = NULL)
    free(head);

  node *current = head;
  while (current->next->next != NULL)
  {
    current = current->next;
  }
  free(current->next);
}

void removeFirstNode(node **head)
{
  if ((*head) == NULL)
    exit(0);
  if ((*head)->next == NULL)
    free(*head);

  node *temp = *head;
  *head = (*head)->next;
  (*head)->prev = NULL;

  free(temp);
}

// Adicionar no começo
void push(node **head, int val)
{
  node *new_node = (node *)malloc(sizeof(node));

  new_node->val = val;

  new_node->next = (*head);

  new_node->prev = NULL;

  if ((*head) != NULL)
  {
    (*head)->prev = new_node;
  }
  (*head) = new_node;
}

int main()
{

  node *head;
  node *one = (node *)malloc(sizeof(node));
  node *two = (node *)malloc(sizeof(node));
  node *three = (node *)malloc(sizeof(node));

  one->val = 10;
  one->next = two;
  one->prev = NULL;

  two->val = 20;
  two->next = three;
  two->prev = one;

  three->val = 30;
  three->next = NULL;
  three->prev = two;

  head = one; // sempre considerado o primeiro elemento, a "cabeça" da lista.

  push(&head, 5);

  append(head, 40);

  traverse_forwards(head);
}
