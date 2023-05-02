def multiples_of_3_or_5():
    s = set()
    for x in range(1000):
        if x % 3 == 0 and x % 5 == 0:
            s.add(x)
        elif x % 3 == 0:
            s.add(x)
        elif x % 5 == 0:
            s.add(x)
    
    return sum(s)

print(multiples_of_3_or_5())