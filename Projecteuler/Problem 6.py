def Sum_square_difference():
    sq = 0
    for i in range(101):
        sq += i**2

    return int((100*101/2)**2 - sq)

print(Sum_square_difference())