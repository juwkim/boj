N = int(input())
x, y = map(int, input().split())
ans = (x != 1) + (x != N) + (y != 1) + (y != N)
print(ans)