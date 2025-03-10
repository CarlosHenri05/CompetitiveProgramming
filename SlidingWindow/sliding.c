#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int maxSomaSubArray(int *lista, int n, int k)
{
  int left = 0, right = 0;
  int window_sum = 0;
  int max_sum = INT_MAX;

  for (int i = 0; i < k; i++)
  {
    window_sum += lista[i];
  }
  max_sum = window_sum;

  for (int i = k; i < n; i++)
  {
    window_sum += lista[i];
    window_sum -= lista[i - k];
  }
  if (window_sum > max_sum)
    max_sum = window_sum;

  return max_sum;
}

int smallestSubarrayWithSum(int arr[], int n, int k)
{
  int left = 0, right = 0;
  int window_sum = 0;
  int min_len = INT_MAX; // Inicializa o comprimento mínimo com infinito

  while (right < n)
  {
    // Expande a janela
    window_sum += arr[right];
    right++;

    // Quando a soma da janela é >= k, tenta reduzir a janela
    while (window_sum >= k)
    {
      // Atualiza o comprimento mínimo
      min_len = (right - left) < min_len ? (right - left) : min_len;
      // Reduz a janela
      window_sum -= arr[left];
      left++;
    }
  }
}

int maxSubArraySize(int *lista, int n, int k)
{
  int left = 0, right = 0;
  int window_sum = 0;
  int max_size = 0;

  while (right < n)
  {
    window_sum += lista[right];
    right++;
    while (window_sum >= k)
    {
      if (right - left > max_size)
      {
        max_size = right - left;
      }
      window_sum -= lista[left];
      left++;
    }
  }
  return max_size;
}

int exactSubArraysAsK(int *lista, int n, int k)
{
  int left = 0, right = 0;
  int window_sum = 0;
  int count = 0;

  while (right < n)
  {
    window_sum += lista[right];
    right++;
    while (window_sum >= k)
    {
      if (window_sum == k)
        count++;
      window_sum -= lista[left];
      left++;
    }
  }
  return count;
}

int main()
{
  int arr[] = {1, 2, 2, 1, 5};
  int n = sizeof(arr) / sizeof(arr[0]);
  int k = 3;

  printf("%d", maxSomaSubArray(arr, n, k));
  printf("\n%d", smallestSubarrayWithSum(arr, n, k));
  printf("\n%d", exactSubArraysAsK(arr, n, k));
  printf("\n%d", maxSubArraySize(arr, n, k));
}
