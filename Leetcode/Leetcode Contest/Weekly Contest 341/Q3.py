class Solution:
    def addMinimum(self, word: str) -> int:
        comp = {'a':{'a':2,'b':0,'c':1},'b':{'a':1,'b':2,'c':0},'c':{'a':0,'b':1,'c':2}}
        res = comp['c'][word[0]]+comp[word[-1]]['a']
        for i in range(len(word)-1):
            res+=comp[word[i]][word[i+1]]
        return res