w, h, d = map(int, input().split())
w -= 2 * d
h -= 2 * d
if w > 0 and h > 0:
    print(w * h)
else:
    print(0)