x = int(input())


def clock(s):
    isPm = 0
    ans = 0

    if int(s[:2]) > 12:
        isPm = 1
        ans = str(int(s[:2]) - 12)
    elif int(s[:2]) == 12:
        isPm = 1
        ans = s[:2]
    elif s[:2] == '00':
        ans = '12'
    else:
        ans = s[:2]
    
    if len(ans) == 1:
        ans = '0'+ans
    if isPm:
        return f'{ans}:{s[3:]} PM'
    else:
        return f'{ans}:{s[3:]} AM'



for _ in range(x):
    n = input()
    print(clock(n))