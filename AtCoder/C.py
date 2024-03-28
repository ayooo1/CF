x = str(input())

ptr = 0
ans = 0
while ptr < len(x)-1:
    if x[ptr:ptr+2] == '00':
        ptr += 2
    else:
        ptr += 1
    ans += 1

print(ans)