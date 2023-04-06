x = int(input())

def func(nums,new,le):
    for i in range(le):
        if int(nums[i]) < int(d):
            return nums[:i]+new+nums[i:]
    return nums+new

for _ in range(x):
    n,d = input().split()
    num = input()
    i = 0
    print(func(num,d,int(n)))