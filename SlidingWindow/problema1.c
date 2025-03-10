#include <stdio.h>
#include <stdlib.h>

int maiorProduto(int *lista, int n, int k)
{
  int produto = 1;

  int maior_produto = INT_MIN;

  for (int i = 0; i < k; i++)
  {
    produto *= lista[i];
  }
  maior_produto = produto;

  for (int i = k; i < n; i++)
  {
    produto /= lista[i - k];
    produto *= lista[i];

    if (produto > maior_produto)
      maior_produto = produto;
  }

  return maior_produto;
}

int main()
{

  int arr[] = {1, 5, 9, 2, 3, 7, 4, 6, 8};
  int k = 3;
  int n = sizeof(arr) / sizeof(arr[0]);

  printf("%d", maiorProduto(arr, n, k));
}
