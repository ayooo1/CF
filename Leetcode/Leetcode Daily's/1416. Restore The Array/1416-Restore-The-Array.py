class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = int(1e9+7)
        @cache
        def dfs(l):
            if l == len(s):
                return 1
            if s[l] == "0": return 0
            res = 0
            for r in range(l+1, len(s)+1):
                x = int(s[l:r])
                if x > k: break
                res+=dfs(r)
            return res%mod
        return dfs(0)