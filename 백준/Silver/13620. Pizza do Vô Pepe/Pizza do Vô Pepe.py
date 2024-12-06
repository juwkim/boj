C, N, *X = map(int, open(0).read().split())
ans = 'N'
d = C // N
for i in range(d):
    a, b = i + 0.5, i + 0.5 + d
    if X[0] > a:
        for num in X:
            if a < num < b:
                a += d
                b += d
            else:
                break
        else:
            ans = 'S'
            break
    else:
        for num in X[1:]:
            if a < num < b:
                a += d
                b += d
            else:
                break
        else:
            ans = 'S'
            break
print(ans)