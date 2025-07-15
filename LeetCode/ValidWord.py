class Solution(object):
    def isValid(self, word):
        if len(word)<3:
            return False

        vowel_count = 0
        consonant_count = 0

        vogais = ['a','e','i','o','u']

        for c in word:

            if not c.isalnum():
                return False
            
            c_lower = c.lower()

            if c_lower in string.ascii_lowercase and c_lower not in vogais:
                consonant_count+=1

            
            if c_lower in vogais:
                vowel_count+=1
            
        return vowel_count >= 1 and consonant_count >=1
            

        