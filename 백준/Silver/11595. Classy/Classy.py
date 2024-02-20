import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

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
buf = [(name, val[::-1] + [1] * (k - len(val))) for name, val in buf]
buf.sort(key=lambda x: (x[1], x[0]))
for name, _ in buf:
    print(name)