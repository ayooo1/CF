def dfs(x,y):
    ans = 0
    if x<20:
        ans += dfs(x+1,y)
    if y<20:
        ans += dfs(x,y+1)
    if x== 20 and y == 20:
        return 1
    return ans

print(dfs(0,0))