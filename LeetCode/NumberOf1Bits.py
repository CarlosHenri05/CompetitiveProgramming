class Solution(object):
    def hammingWeight(self, n):
        count = 0

        while n>0:
            resto = n % 2
            n = n //2

            if resto == 1:
                count+=1
        
        return count

            
        