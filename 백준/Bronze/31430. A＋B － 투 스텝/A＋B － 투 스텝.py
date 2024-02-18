if input() == '1':
    num = sum(map(int, input().split()))
    ans = ['a'] * 13
    for i in range(12, -1, -1):
        if num == 0:
            break
        num, c = divmod(num, 26)
        ans[i] = chr(c + 97)
    print(*ans, sep='')
else:
    ans = 0
    for c in input():
        ans = ans * 26 + ord(c) - 97
    print(ans)