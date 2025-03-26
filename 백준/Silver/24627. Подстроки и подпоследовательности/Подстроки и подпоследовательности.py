n = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
l = 1
while n > 26 + 650 * (l - 1):
    n -= 26 + 650 * (l - 1)
    l += 1
buf = []
for a in alpha:
    buf.append(a * l)
    for i in range(1, l):
        for b in alpha:
            if a != b:
                buf.append(a * i + b * (l - i))
print(sorted(buf)[n - 1])