g = lambda: map(int, input().split())

n = int(input())
eggplant = input().split()
m, k = g()

ans = 'P'
for _ in range(m):
    if all(eggplant[num - 1] == 'W' for num in g()):
        ans = 'W'
        break
print(ans)