import sys
input = sys.stdin.readline

buf = []
k = 0
for _ in range(int(input())):
    name, l = input().split(':')
    val = []
    for c in l.split()[:-1]:
        match c[0]:
            case 'u': val.append(0)
            case 'm': val.append(1)
            case 'l': val.append(2)
    k = max(k, len(val))
    buf.append((name, val))
for _, name in sorted((val[::-1] + [1] * (k - len(val)), name) for name, val in buf):
    print(name)