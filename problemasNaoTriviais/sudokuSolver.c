#include <stdlib.h>
#include <stdio.h>

#define n 10

void print_matrix(int arr[n][n])
{
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      printf("%d\n", arr[i][j]);
    }
  }
}

void isSafe(int grid[n][n], int row, int col, int num)
{
  for (int i = 0; i < n; i++)
  {
    if (grid[row][i] == num)
      return 0; // Retornará falso caso encontrarmos o mesmo número na mesma linha
  }
  for (int i = 0; i < n; i++)
  {
    if (grid[i][col] == num)
    {
      return 0; // Retornará falso caso encontremos o mesmo número na mesma linha
    }
  }

  int start_row = row - row % 3, start_col = col - col % 3;

  for (int i = 0; i < 3; i++)
  {
    for (int j = 0; j < 3; j++)
    {
      if (grid[i + start_row][j + start_col] == num)
        return 0;
    }
  }
  return 1;
}

int main()
{
}
