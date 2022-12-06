min_l, max_l = 100, 0
buf = [0] * 101
for _ in range(3):
    a, b = map(int, input().split())
    min_l = min(min_l, b - a)
    max_l = max(max_l, b - a)
    buf[a:b] = [1] * (b - a)
print(''.join(map(str, buf)).count('01'))
print(min_l, max_l)