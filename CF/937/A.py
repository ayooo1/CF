x = int(input())

def check(a,b,c):
    if a < b < c:
        return 'STAIR'
    elif a < b and b > c:
        return 'PEAK'
    else:
        return 'NONE'

for _ in range(x):
    a,b,c = input().split()
    print(check(int(a),int(b),int(c)))