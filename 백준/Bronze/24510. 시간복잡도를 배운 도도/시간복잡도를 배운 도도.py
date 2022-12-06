a = 0
for _ in range(int(input())):
    s = input()
    a = max(a, s.count('while') + s.count('for'))
print(a)