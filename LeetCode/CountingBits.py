# Dynamic Programming

class Solution(object):
    def countBits(self, n):
        ans = [0] * (n+1)
        sub = 1

        for i in range(1, n + 1):
            if sub * 2 == i:
                sub = i
            
            ans[i] = ans[i - sub] + 1 # bit mais significativo 

        return ans
        
        # sub * 2 == i? 
        # ans[1] = ans[1-sub] + 1 == 1
        # ans[2] = ans[2-2] + 1 ==   1           sub caiu no IF 1 * 2 == i
