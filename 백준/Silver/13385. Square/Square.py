for _ in range(int(input())):
    _, *a, l = map(int, input().split())
    w = 1
    for n in reversed(a):
        w, l = l, w + l * n
    print(l)