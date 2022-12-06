ans = 1
for i in range(3, int(input()), 2):
    ans = ans * i % 1_000_000_007
print(ans)