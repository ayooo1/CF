'''
Solved after contest
'''
from collections import Counter
class PrefixHash:
    def __init__(self, arr):
        self.mod = mod = 344555666677777
        self.base = base = 37
        self.inv = inv = pow(base, mod-2, mod)
        self.pref = pref = [0]
        self.invpref = invpref = [1]
        pwr, invpwr = 1, 1
        hsh = 0
        for x in arr:
            hsh = (hsh+x*pwr)%mod
            pwr = (pwr*base)%mod
            invpwr = (invpwr*inv)%mod
            pref.append(hsh)
            invpref.append(invpwr)
    def query(self, l, r):
        return (self.pref[r+1]-self.pref[l])*self.invpref[l]%self.mod

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c = Counter()

        ans = 0
        for i in range(len(words)):
            pre = PrefixHash([(ord(x)-96) for x in words[i]])
            m = len(words[i])
            hsh = pre.query(0,m-1)
            for j in range(m):
                l,r = j,m-1-j
                prefix = pre.query(0,l)
                suffix = pre.query(r,m-1)
                if prefix != suffix: continue
                ans += c[prefix]
            c[hsh] += 1
        
        return ans