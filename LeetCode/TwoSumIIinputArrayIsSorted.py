class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left<right:
            soma = numbers[left] + numbers[right]

            if soma == target:
                return [left + 1, right + 1]
            elif soma > target:
                right -= 1
            else:
                left += 1
        

        # Como é 1 indexed, já temos certeza que temos que voltar o índice + 1
        # Basta somarmos o elemento do primeiro índice com o último e vermos se é maior ou não que o alvo,
        # O resto do código é uma lógica básica de two pointers




        