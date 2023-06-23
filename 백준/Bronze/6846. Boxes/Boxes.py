g = lambda: [*map(int, input().split())]

boxes = [sorted(g()) for _ in range(int(input()))]
for _ in range(int(input())):
    l0, w0, h0 = sorted(g())
    ans = 1e12
    for l, w, h in boxes:
        if l0 <= l and w0 <= w and h0 <= h:
            ans = min(ans, l * w * h)
    if ans == 1e12:
        print("Item does not fit.")
    else:
        print(ans)