def Largest_palindrome_product():
    ret = []

    for x in range(100,1000):
        for y in range(100,1000):
            if str(x*y) == str(x*y)[::-1]:
                ret.append(x*y)
    return max(ret)

print(Largest_palindrome_product())