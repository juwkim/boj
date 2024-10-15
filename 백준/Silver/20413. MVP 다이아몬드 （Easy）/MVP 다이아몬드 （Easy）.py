N = int(input())
money = {k: v - 1 for k, v in zip("BSGP", map(int, input().split()))}
ans, prev = 0, 0
for grade in input():
    if grade == 'D':
        ans += money['P'] + 1
    else:
        ans += (prev := money[grade] - prev)
print(ans)