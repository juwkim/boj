ans, m = 0, 1_000_000_007
for i, c in enumerate(input()):
    if c == 'O':
        ans = (ans + pow(2, i, m)) % m
print(ans)