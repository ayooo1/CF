x = int(input())

def func(i: int):
    base_9 = ""
    m = i
 
    while m > 0:
        m, d = divmod(m, 9)
        if d > 3:
            d += 1
        base_9 = str(d) + base_9
 
    return int(base_9, 10) if base_9 else 0


for _ in range(x):
    print(func(int(input())))