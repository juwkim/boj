d1, d2, d3 = map(int, input().split())
a, b, c = round((d1 + d2 - d3) / 2, 1), round((d1 - d2 + d3) / 2, 1), round((- d1 + d2 + d3) / 2, 1)
if all(map(lambda x: x > 0, [a, b, c])):
    print(1)
    print(a, b, c)
else:
    print(-1)