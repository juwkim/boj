import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

weight, value = 0, 0
for _ in range(int(input())):
    T, *l = input().split()
    W, H, L = map(int, l)
    if T == 'A':
        num = (W // 12) * (H // 12) * (L // 12)
        weight += 1000 + 500 * num
        value += 4000 * num
    else:
        weight += 6000
print(weight, value)