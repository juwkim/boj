n = int(input())
ans, coffee = 0, 0
for l in input():
    if l == '1':
        ans += 1
        coffee = 2
    elif coffee:
        ans += 1
        coffee -= 1
print(ans)