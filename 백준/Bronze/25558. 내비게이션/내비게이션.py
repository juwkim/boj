N = int(input())
x1, y1, x2, y2 = map(int, input().split())
ans = 1
Min = 1e13
for i in range(1, 1 + N):
    num = 0
    s, t = x1, y1
    for _ in range(int(input())):
        a, b = map(int, input().split())
        num += abs(s - a) + abs(t - b)
        s, t = a, b
    num += abs(s - x2) + abs(t - y2)
    if num < Min:
        Min = num
        ans = i
print(ans)