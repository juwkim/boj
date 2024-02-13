import sys
input = sys.stdin.readline

for _ in range(int(input())):
    r, *a = map(int, input().split())
    w, l = 1, a[-1]
    for num in reversed(a[:-1]):
        w += l * num
        w, l = sorted([w, l])
    print(l)