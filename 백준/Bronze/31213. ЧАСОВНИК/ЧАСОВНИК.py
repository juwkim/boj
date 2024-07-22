h, m = map(int, input().split())
h1, m1 = divmod(m * 12, 60)
print(h1 if h1 else 12, m1)
if m * 12 > (h % 12) * 60 + m:
    print(*divmod(m * 12 - (h % 12) * 60 - m, 60))
else:
    print(*divmod(720 + m * 12 - (h % 12) * 60 - m, 60))