class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        # Basta iterar sobre as linhas e limitar as colunas 
        for i in range(rows):
            left = 0
            right = cols-1 # limite 

            # Busca binária normal 
            while left<=right:
                mid = (left+right)//2

                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid]>target:
                    right = mid-1
                else:
                    left = mid + 1
        
        return False
        

        
