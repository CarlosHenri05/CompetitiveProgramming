class Solution(object):
    def firstPalindrome(self, words):
        count = 0

        for word in words:
            if word == word[::-1]:
                count+=1
            
            if count == 1:
                return word
        
        return ""
