x = int(input())

def make(n):
    ans = ''

    for l in range(n):
        flip = l%2
        for k in range(2):
            for i in range(n):
                if not i % 2 and not flip:
                    ans += '##'
                elif i%2 and not flip:
                    ans += '..'
                elif not i%2 and flip:
                    ans += '..'
                else:
                    ans += '##'
            ans += '\n'
    return ans[:-1]


for _ in range(x):
    n = int(input())
    print(make(n))