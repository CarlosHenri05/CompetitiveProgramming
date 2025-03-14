// Essa soma é para a soma de um subarray que seja maior ou igual a K (valor de input)

#include <stdio.h>
#include <stdlib.h>

int menor_subarray_com_soma_k(int *lista, int n, int k)
{
  int left = 0, right = 0;
  int soma = 0;
  int min_len = __INT_MAX__;

  while (right < n)
  {
    soma += lista[right];
    right++;
    while (soma >= k)
    {
      min_len = (right - left) < min_len ? (right - left) : min_len;
      soma -= lista[left];
      left++;
    }
  }
  return min_len == __INT_MAX__ ? 0 : min_len;
}

int main()
{
  int arr[] = {2, 3, 1, 2, 4, 3};
  int n = sizeof(arr) / sizeof(arr[0]);
  int k = 7;

  printf("%d", menor_subarray_com_soma_k(arr, n, k));
}
