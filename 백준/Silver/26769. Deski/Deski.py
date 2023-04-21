N = int(input())
if N < 4:
    print(0)
else:
    *_, a, b, c, d = sorted(map(int, input().split()))
    print(a * a)