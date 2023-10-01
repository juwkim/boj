import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
odd, even = [], []
while N:
    for num in g():
        N -= 1
        if num&1:
            odd.append(num)
        else:
            even.append(num)
ans = sum(odd) + sum(even)
if ans&1:
    ans -= min(odd)
print(ans // 2)