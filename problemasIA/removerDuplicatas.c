#include <stdio.h>
#include <stdlib.h>

int removeDuplicates(int *lista, int n)
{
  if (n == 1)
    return 1;

  int i = 0; // ponteiro que so vai avançar quando vermos uma condição

  for (int j = 1; j < n; j++)
  {
    if (lista[i] != lista[j])
    {
      i++;
      i = lista[j];
    }
  }
  return lista[i + 1];
}

int main()
{

  int arr[] = {2, 2, 1, 1, 3};
  int size = sizeof(arr) / sizeof(arr[0]);

  printf("%d", removeDuplicates(arr, size));
}
