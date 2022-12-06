N = int(input())
if N < 3:
    print(1, N)
else:
    l, r, pivot = 1, 1, 1
    b, c, *s = input().split()
    for idx, num in enumerate(s, 2):
        a, b, c = b, c, num
        if a == b == c:
            if idx - pivot > r - l:
                l, r = pivot, idx
            pivot = idx
    if N - pivot > r - l:
        l, r = pivot, N
    print(l, r)