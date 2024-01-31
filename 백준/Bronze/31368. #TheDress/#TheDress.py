import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
a, b, c = 0, 0, 0
for _ in range(N):
    s = input()
    if "blue" in s and "black" in s:
        a += 100
    elif "white" in s and "gold" in s:
        b += 100
    else:
        c += 100
print(a / N, b / N, c / N)