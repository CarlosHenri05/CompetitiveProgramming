class Solution(object):
    def findWordsContaining(self, words, x):
        arr = []
        for i in range(len(words)):
            if x in words[i]:
                arr.append(i)

        return arr