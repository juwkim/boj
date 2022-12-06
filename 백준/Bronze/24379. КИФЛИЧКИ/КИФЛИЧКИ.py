g = lambda: [*map(int, input().split())]

a = sorted(zip(g(), g()))
money = int(input())
cnt = 0
for cost, amount in a:
    if cost > money:
        break
    if cost:
        amount = min(money // cost, amount)
    cnt += amount
    money -= amount * cost
print(cnt)