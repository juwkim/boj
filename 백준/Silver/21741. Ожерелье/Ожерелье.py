n, *a = map(int, open(0).read().split())

while True:
    end = True
    for i in range(n):
        j = (i + 1) % n
        if a[j] >= a[i] + 2:
            print(a[i], a[j])
            a[i], a[j] = a[j], a[i]
            end = False
    if end:
        break
print(0)