from collections import Counter,deque
from typing import List

prime = [True for i in range(10**7)]
def SieveOfEratosthenes(num):
# boolean array
    p = 2
    while (p * p <= num):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1

SieveOfEratosthenes(10**7-1)

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        
        def is_prime(num):
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    return 0
            return 1
        
        m,n = len(mat),len(mat[0])
        c = Counter()
        moves = [(1,1),(-1,-1),(1,-1),(-1,1),(1,0),(-1,0),(0,1),(0,-1)]
        
        def bfs(i,j):
            hm = Counter()
            q = deque([(i,j,mat[i][j],x) for x in range(len(moves))])
            s = set()

            s.add((i,j))
            
            while q:
                x,y,num,d = q.popleft()
                if num > 10:
                    hm[num] += prime[num]
                
                r = x+moves[d][0]
                c = y+moves[d][1]

                if -1<r<m and -1<c<n and (r,c) not in s:
                    s.add((r,c))
                    q.append((r,c,num*10+mat[r][c],d))

            return hm
            
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                c += bfs(i,j)

        ans = sorted(c.items(), key = lambda x: (x[1],x[0]))
        return ans[-1][0] if ans else -1
        