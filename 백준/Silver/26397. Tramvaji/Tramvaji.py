import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n + 1)
s = [0] * (n + 1)
for i in range(1, n):
    p = input()
    if p[0] == 'P':
        num = int(p.split()[1])
        d[i + 1] = num - d[i]
        s[i + 1] = num
    else:
        _, y, num = p.split()
        y, num = int(y), int(num)
        dist = s[y] + num
        d[i + 1] = dist - s[i]
        s[i + 1] = dist
x2 = min(range(2, n + 1), key=lambda x: (d[x], x))
print(d[x2], x2 - 1, x2)