for _ in range(int(input())):
    s = input()
    ans = 0
    for i in range(7):
        if len(set(s[:i])) != i:
            continue
        if all(len(set(s[j:j+7])) == len(s[j:j+7]) for j in range(i, len(s), 7)):
            ans = 1
            break
    print(ans)