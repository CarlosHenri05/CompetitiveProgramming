#include <stdlib.h>
#include <stdio.h>

int binarySearch(int *lista, int n, int alvo)
{
  int left = 0;
  int right = n - 1;
  while (left <= right)
  {
    int mid = left + (right - left) / 2;

    if (lista[mid] == alvo)
      return mid;
    else if (lista[mid] > alvo)
      right = mid - 1;
    else
      left = mid + 1;
  }
  return -1;
}

int main()
{
  int lista[5] = {1, 2, 3, 4, 5};
  int n = sizeof(lista) / sizeof(lista[0]);
  int alvo = 5;

  printf("%d", binarySearch(lista, n, alvo));
}
