#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
  int data;
  struct Node *left;
  struct Node *right;

} Node;

Node *createNode(int val)
{
  Node *newNode = (Node *)malloc(sizeof(Node));

  newNode->data = val;
  newNode->left = NULL;
  newNode->right = NULL;

  return newNode;
}

Node *pushNode()
{
}

int main()
{
}
