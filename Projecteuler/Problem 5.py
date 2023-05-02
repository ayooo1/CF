def Smallest_multiple():
    num = 21
    x = 2
    def helper(n):
        x = 2
        while x < 21:
            if n%x == 0:
                x += 1
            else:
                return False
        return True

    while True:
        if helper(num):
            return num
        num += 1
        
print(Smallest_multiple())