class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        cnt, res = 0, 0
        l = 0
        for r in range(len(s)):
            if s[r] in vowels:
                cnt += 1
            if r - l + 1 > k:
                if s[l] in vowels:
                    cnt -= 1
                l += 1
            res = max(res,cnt)
            if res == k:
                return res

        

        return res
