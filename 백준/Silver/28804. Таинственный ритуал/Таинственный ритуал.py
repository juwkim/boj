a = 0, 1, 1, 3, 2, 1, 3, 7, 4, 9
for _ in range(int(input())):
    v = [int(c) for c in input()][::-1]
    i = 0
    while i + 1 < len(v) or v[i] > 9 or a[v[i]] < v[i]:
        if i + 1 == len(v):
            v.append(0)
        v[i + 1] += v[i] // 10
        v[i] %= 10
        v[i + 1] += a[v[i]]
        i += 1
    print(v[-1])