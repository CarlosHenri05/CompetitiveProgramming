#include <stdio.h>
#include <stdlib.h>

int twoPointerSum(int *lista, int n, int alvo)
{
  int left = 0;
  int right = n - 1;
  while (left < right)
  {
    if (lista[left] + lista[right] == alvo)
    {
      printf("(%d, %d)", lista[left], lista[right]);
      right--;
      left++;
    }
    else if (lista[left] + lista[right] > alvo)
    {
      right--;
    }
    else if (lista[left] + lista[right] < alvo)
    {
      left++;
    }
  }
}

int main()
{
  int arr[] = {1, 2, 3, 4, 5, 6, 7};
  int n = sizeof(arr) / sizeof(arr[0]);
  int alvo = 9;

  twoPointerSum(arr, n, alvo);
}
