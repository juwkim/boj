from bisect import bisect_left

buf = []
order = []
N = int(input())
for _ in range(N):
    name, *nums = input().split()
    score = -sum(int(num) for num in nums)
    buf.append((score, name))
    order.append((score, name))
buf.sort()

for score, name in order:
    a = bisect_left(buf, (score - 500, name))
    b = bisect_left(buf, (score + 500, name))
    print(a + 1, b)