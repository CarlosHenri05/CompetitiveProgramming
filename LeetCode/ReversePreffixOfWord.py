class Solution(object):
    def reversePrefix(self, word, ch):
        # Ache a primeira ocorrência da letra na palavra
        j = word.find(ch)

        if j!=-1:
            #Retorne a string até a letra j ao contrário + resto normal
            return word[:j+1][::-1] + word[j+1:]
        
        # Retorna a palavra normal se não tiver a "ch" na palavra
        return word
