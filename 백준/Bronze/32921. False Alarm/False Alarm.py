import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    h, m = map(int, input().split(':'))
    l.append(h * 60 + m)
if any(l[i + 2] - l[i] <= 10 for i in range(n - 2)):
    print(0)
elif any(l[i + 1] - l[i] <= 10 for i in range(n - 1)):
    print(1)
else:
    print(2)