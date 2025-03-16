#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

int binarySearch(int *lista, int n, int alvo, int left, int right)
{
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

int exponentialSearch(int *lista, int n, int alvo)
{
  if(lista[0]== alvo)
    return 0;
  
  int i = 1;
  while(i<n && lista[i]<=alvo)
    i*=2;
  
  return binarySearch(lista,n,alvo,i/2,MIN(i, n-1));
}

int main()
{
  int lista[5] = {1, 2, 3, 4, 5};
  int n = sizeof(lista) / sizeof(lista[0]);
  int alvo = 3;

  printf("%d", exponentialSearch(lista, n, alvo));
}
