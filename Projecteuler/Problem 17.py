import inflect
from collections import Counter
p = inflect.engine()
ans = 0
for i in range(1,1001):
    x = p.number_to_words(i)
    for j in x:
        if j!=' ' and j!='-':
            ans += 1

print(ans)