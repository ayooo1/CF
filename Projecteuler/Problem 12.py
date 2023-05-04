import math


def Highly_divisible_triangular_number():
    def helper(x):
        ans = 0
        for i in range(1, int(math.sqrt(x) + 1)):
            if x % i == 0:
                if i * i == x:
                    ans +=  1
                else:
                    ans += 2
        
        return ans
    
    j = 1
    tot = 2
    while True:
        if helper(j) > 500:
            return j
        else:
            j += tot
            tot += 1
    

print(Highly_divisible_triangular_number())