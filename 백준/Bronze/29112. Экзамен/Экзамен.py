l, r = map(int, input().split())
s = lambda x: 0 if x < 0 else int((x // 36000) ** (1/6) + 1e-12) + 1 
print(s(r) - s(l - 1))