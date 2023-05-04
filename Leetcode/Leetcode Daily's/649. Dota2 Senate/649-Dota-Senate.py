from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        n = len(senate)
        for i,x in enumerate(senate):
            if x == 'R':
                r.append(i)
            else:
                d.append(i)
        
        while r and d:
            rx = r.popleft()
            dx = d.popleft()
            if rx < dx:
                r.append(rx+n)
            else:
                d.append(dx+n)

        return 'Radiant' if r else 'Dire'