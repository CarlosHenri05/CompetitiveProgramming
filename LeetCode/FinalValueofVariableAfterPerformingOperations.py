class Solution(object):
    def finalValueAfterOperations(self, operations):
        X = 0
        for string in operations:
            if string=="++X" or string=="X++":
                X+=1
            elif string=="--X" or string=="X--":
                X-=1

        return X
