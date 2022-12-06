a = ["No", "Yes"]
p = [1, 3, 5, 7, 8, 10, 12]
for _ in range(int(input())):
    x, y = map(int, input().split())
    d = 29 + (x != 2) + (x in p)
    s = 1 <= x <= 12
    t = 1 <= y <= d
    print(a[x // 24 + y // 60 == 0], a[(s + t) // 2])