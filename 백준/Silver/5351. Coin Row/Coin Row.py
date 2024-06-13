for _ in range(int(input())):
    a, b = 0, 0
    for d in input().split(): a, b = max(a, b), a + int(d)
    print(max(a, b))