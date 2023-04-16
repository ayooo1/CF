import collections


class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        mod = 10**9+7

        cnt = collections.defaultdict(int)

        for w in words:
            for i,c in enumerate(w):
                cnt[(i,c)] += 1
        
        dp = {} # -> (i,k) => num ways

        # i = index of the target k = index of words[j][k]
        def dfs(i,k):
            if i == len(target):
                return 1
            
            if k == len(words[0]):
                return 0
            
            if (i,k) in dp:
                return dp[(i,k)]
            
            c = target[i]

            dp[(i,k)] = dfs(i,k+1)
            dp[(i,k)] += cnt[(k,c)] * dfs(i+1,k+1)
            return dp[(i,k)]

        
        return dfs(0,0) % mod