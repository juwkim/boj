ans = 0
for i in range(int(input())):
    check = [0, 0]
    game = input().split('/')
    val = 0
    for score in game:
        a, b = map(int, score.split(':'))
        check[0] += a
        check[1] += b
        val += 1
    if val == 3:
        if check[i&1] > check[1 - (i&1)]:
            ans += 3
    elif val == 4:
        if check[i&1] > check[1 - (i&1)]:
            ans += 2
        else:
            ans += 1
    else:
        if check[i&1] > check[1 - (i&1)]:
            ans += 1
print(ans)