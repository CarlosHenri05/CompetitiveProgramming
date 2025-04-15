# Mantendo x como integer

class Solution1(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        
        inputNum = x
        newNum = 0

        while x>0:
            newNum = newNum*10 + x%10
            x = x//10

        return newNum == inputNum 


# Transformando x em string
class Solution2(object):
    def isPalindrome(self, x):
        x = str(x)

        return x == x[::-1]

