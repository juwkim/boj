n, *v = map(int, open(0).read().split())
Min = [1e18] * n
Min[-1] = v[-1], n - 1
for i in range(n - 2, -1, -1):
    if v[i] < Min[i + 1][0]:
        Min[i] = v[i], i
    else:
        Min[i] = Min[i + 1]
for i in range(n):
    if v[i] != Min[i][0]:
        r = Min[i][1] + 1
        v[i:r] = v[i:r][::-1]
        if v == sorted(v):
            print(i + 1, r)
        else:
            print("impossible")
        break
else:
    print(1, 1)