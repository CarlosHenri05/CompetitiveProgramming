#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
  // Converte os ponteiros genéricos para o tipo específico
  const int *pa = (const int *)a;
  const int *pb = (const int *)b;

  // Retorna negativo se a < b, 0 se a == b, positivo se a > b
  return *pa - *pb;
}

int twoPointer(int *lista, int n, int alvo)
{
  qsort(lista, n, sizeof(int), compare);
  int current_sum;
  int menor_diferenca;
  int resultado;

  for (int i = 0; i < n - 3; i++)
  {
    int left = 0;
    int right = n - 1;
    while (left < right)
    {
      current_sum = lista[i] + lista[left] + lista[right];
      int diferenca = abs(current_sum - alvo);

      if (diferenca < menor_diferenca)
      {
        diferenca = menor_diferenca;
        resultado = current_sum;
      }
      if (current_sum < alvo)
      {
        left++;
      }
      else
      {
        right--;
      }
    }
  }
  return resultado;
}

int main()
{
  int arr[] = {-1, 2, 1, -4};
  int alvo = 1;
  int n = sizeof(arr) / sizeof(arr[0]);

  printf("%d", twoPointer(arr, n, alvo));
}
