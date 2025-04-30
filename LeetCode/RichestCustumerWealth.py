class Solution(object):
    def maximumWealth(self, accounts):
        wealth = 0
        biggest_wealth = 0
        for element in accounts:
            wealth = sum(element)
            biggest_wealth = max(biggest_wealth, wealth)
        
        return biggest_wealth
