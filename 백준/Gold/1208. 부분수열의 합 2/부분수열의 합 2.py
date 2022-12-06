import bisect

def makeSumList(idx, end, lst, Sum):
    
    global ans
    if idx == end:
        return
    
    Sum += nums[idx]
    if Sum == S:
        ans += 1
    
    lst.append(Sum)
    makeSumList(idx + 1, end, lst, Sum)
    makeSumList(idx + 1, end, lst, Sum - nums[idx])

ans = 0
N, S = map(int, input().split())
nums = [*map(int, input().split())]

A, B = [], []
makeSumList(0, N // 2, A, 0)
makeSumList(N // 2, N, B, 0)

A.sort()
B.sort()

for num in A:
    target = S - num
    ans += bisect.bisect_right(B, target) - bisect.bisect_left(B, target)

print(ans)