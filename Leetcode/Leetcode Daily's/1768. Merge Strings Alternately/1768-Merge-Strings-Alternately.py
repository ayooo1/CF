class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        i=0
        if len(word1) > len(word2):
            m = len(word2)
            x = 2
        elif len(word1) < len(word2):
            m = len(word1)
            x = 1
        else:
            m = len(word1)
            x = 0

        while m:
            s += word1[i]
            s += word2[i]
            i+=1
            m-=1
        
        if x == 2:
            s += word1[i:]
        elif x == 1:
            s += word2[i:]
        
        return s
        