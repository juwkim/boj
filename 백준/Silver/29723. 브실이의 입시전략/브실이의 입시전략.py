import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M, K = g()
dic = {}
for _ in range(N):
    s, p = input().split()
    dic[s] = int(p)
score = 0
for _ in range(K):
    t = input()
    score += dic[t]
    del dic[t]

nums = sorted(dic.values())
Min = score + sum(nums[:M-K])
if K == M:
    Max = score
else:
    Max = score + sum(nums[K-M:])
print(Min, Max)