#include <stdio.h>
#include <stdlib.h>

int comparar(const void *a, const void *b)
{
  // Converte os ponteiros genéricos para o tipo específico
  const int *pa = (const int *)a;
  const int *pb = (const int *)b;

  // Retorna negativo se a < b, 0 se a == b, positivo se a > b
  return *pa - *pb;
}
int elementosUnicos(int *lista, int n)
{
  if (n == 0)
  {
    return 0;
  }

  qsort(lista, n, sizeof(int), comparar);
  int count = 1;

  for (int i = 1; i < n; i++)
  {
    if (lista[i] != lista[i - 1])
    {
      count++;
    }
  }
  return count;
}

int main()
{

  // 1,1,2,2,3,4,4,5
  int lista[] = {1, 2, 3, 1, 2, 4, 5, 4};
  int size = sizeof(lista) / sizeof(lista[0]);
  printf("%d", elementosUnicos(lista, size));
}
