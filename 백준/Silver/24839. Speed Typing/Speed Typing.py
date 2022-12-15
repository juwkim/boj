for step in range(1, 1 + int(input())):
    s = input()
    ans, idx = 0, 0
    for c in input():
        if idx == len(s) or c != s[idx]:
            ans += 1
        else:
            idx += 1
    if idx != len(s):
        ans = 'IMPOSSIBLE'
    print(f'Case #{step}: {ans}')