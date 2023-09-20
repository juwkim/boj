import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
dish = input()
friend = input() * 2
ans = "EI SAA"
for i in range(N):
    if all(a == 'P' for a, b in zip(dish, friend[i:i+N]) if b == 'S'):
        ans = i + 1
        break
print(ans)