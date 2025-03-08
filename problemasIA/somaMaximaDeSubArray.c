#include <stdio.h>
#include <stdlib.h>

// n é o tamanho da array lista sei la
int sum(int *lista, int n, int k)
{
  int window_sum = 0;
  int max_sum = 0;
  for (int i = 0; i < k; i++)
  {
    window_sum += lista[i];
    max_sum = window_sum;
  }

  for (int i = k; i < n; i++)
  {
    window_sum += lista[i];
    window_sum -= lista[i - k];

    if (window_sum > max_sum)
      max_sum = window_sum;
  }

  return max_sum;
}

int main()
{
  int arr[] = {1, 4, 2, 10, 2, 3, 1, 0, 20};
  int n = sizeof(arr) / sizeof(arr[0]);
  int k = 4;
  printf("%d", sum(arr, n, k));
}
