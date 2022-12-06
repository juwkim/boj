m, d = int(input()), int(input())
a = m * 30 + d
print([['Before', 'After'][a > 78],'Special'][a == 78])