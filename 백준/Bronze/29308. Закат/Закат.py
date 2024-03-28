cost, ans = 0, None
for _ in range(int(input())):
    money, name, nationality = input().split()
    money = int(money)
    if nationality == "Russia" and money > cost:
        cost, ans = money, name
print(ans)