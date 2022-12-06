g = lambda: [*map(int, input().split())]
N, M = g()
nums = [int(input()) for _ in range(N)]
s, e = max(nums), max(nums) * N


def check(num):
    cur = num
    ret = 0
    for val in nums:
        if val <= cur:
            cur -= val
        else:
            ret += 1
            cur = num - val
    if cur != num:
        ret += 1
    
    return ret

while e > s + 1:
    m = (s + e) // 2
    cnt = check(m)
    if cnt > M:
        s = m
    else:
        e = m

if check(s) > M:  
    print(e)
else:
    print(s)