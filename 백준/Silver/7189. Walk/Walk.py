import sys
input = lambda: sys.stdin.readline().rstrip()

def f(s):
    i = s.find('m')
    if i == -1:
        return int(s[:-1])
    return int(s[:i]) * 60 + int(s[i + 1:-1])

dist, time = 0, 0
for _ in range(int(input())):
    a, _, b = input().split()
    t1 = f(a)
    t2 = f(b.split('/')[0])
    dist += t1 / t2
    time += t1
print(f"{dist * 1000:.0f}m")
print(f"{dist * 3600 / time:.3f}km/h")