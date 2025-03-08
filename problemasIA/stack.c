#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct
{
  int arr[MAX_SIZE];
  int top;
} stack;

void initialize(stack *stack)
{
  stack->top = -1; // Indicamos que é uma stack vazia pois o topo é -1
}

bool isEmpty(stack *stack)
{
  return stack->top == -1 ? 1 : 0;
}

bool isFull(stack *stack)
{
  return stack->top == MAX_SIZE - 1;
}

void push(stack *stack, int val)
{
  if (isEmpty(stack))
  {
    stack->arr[stack->top] = val;
    stack->top++;
  }
  if (isFull(stack))
  {
    printf("Cant, the stack is full.");
    return;
  }
  // stack->top+=1;
  stack->arr[++stack->top] = val; // posição acima do top comum (que normalmente não existe) vai ser criada nessa incrementação com o valor val se tornando o novo top
}

int peek(stack *stack)
{
  if (isEmpty(stack))
    return -1;
  return stack->arr[stack->top];
}

int pop(stack *stack)
{
  if (isEmpty(stack))
    return -1;

  int popped = stack->arr[stack->top];

  stack->top--;

  return popped;
}

int main()
{
  stack newStack;

  initialize(&newStack);

  push(&newStack, 10);
  printf("Top element: %d\n", peek(&newStack));

  push(&newStack, 20);
  printf("Top element: %d\n", peek(&newStack));

  push(&newStack, 30);
  printf("Top element: %d\n", peek(&newStack));

  while (!isEmpty(&newStack))
  {
    printf("Top element: %d\n", peek(&newStack));
    printf("Popped element: %d\n", pop(&newStack));
  }
}
