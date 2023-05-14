from collections import defaultdict


class Solution:
    def circularGameLosers(self, n: int, k: int) -> list[int]:
        dic = defaultdict(int)
        i=1
        steps = 1
        dic[1] = 1
        while max(dic.values()) != 2:
            dic[(i+steps*k)%(n)] += 1
            i += steps*k
            steps += 1
            
        ret = []
        for i in range(1,n):
            if not dic[i]:
                ret.append(i)
        if not dic[0]:
            ret.append(n)
        return ret