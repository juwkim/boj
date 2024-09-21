from math import atan, degrees, sqrt

d, h, w, k = map(int, input().split())
if w * 2 <= h and sqrt(d ** 2 + w ** 2) * 2 <= k:
    print(degrees(atan(w / d)))
elif k >= 2 * d and sqrt(k ** 2 - 4 * d ** 2) / 2 >= w:
    print(degrees(atan(sqrt(k ** 2 - 4 * d ** 2) / 2 / d)))
else:
    print(-1)