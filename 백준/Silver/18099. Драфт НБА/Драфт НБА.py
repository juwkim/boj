import sys
input = sys.stdin.readline

for _ in range(int(input())):
    h, w, s, r, p = map(int, [input() for _ in range(5)])
    h1, h2, h3, h4 = h > 220, 205 <= h <= 220, 190 <= h < 205, h < 190
    w1, w2, w3, w4 = w > 250, 225 <= w <= 250, 200 <= w < 225, w < 200
    s1, s2, s3, s4 = s > 20, 15 <= s <= 20, 10 <= s < 15, s < 10
    r1, r2, r3, r4 = r > 6, 4 <= r <= 6, 2 <= r < 4, r < 2
    p1, p2, p3, p4 = p > 7, 5 <= p <= 7, 3 <= p < 5, p < 3
    cnt1 = h1 + w1 + s1 + r1 + p1
    cnt2 = h2 + w2 + s2 + r2 + p2
    cnt4 = h4 + w4 + s4 + r4 + p4
    if cnt1 >= 3 and h1 + w1:
        print(0)
    elif cnt1 == 3 or (cnt1 == 2 and cnt2 >= 1) or (cnt4 == 0 and cnt1 + cnt2 >= 3):
        print(1)
    elif cnt1 == 2 or (cnt1 == 1 and cnt2 >= 1) or cnt2 >= 3:
        print(2)
    else:
        print(3)