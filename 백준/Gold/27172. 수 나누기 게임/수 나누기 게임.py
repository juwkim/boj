import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
ans = [0] * 1000001
nums = g()
for num in nums:
    if num != 1:
        ans[1] += 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            ans[i] += 1
            if i != num // i:
                ans[num // i] += 1
    for i in range(2 * num, 1000001, num):
        ans[i] -= 1
print(*[ans[i] for i in nums])