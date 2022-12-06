for cnt in range(1, 1 + int(input())):
    S = input()
    i, j = map(int, input().split())
    if len(S) == 1:
        ans = (j - i + 1) * (S == 'B')
    else:
        ans = 0
        while i % len(S) != 1 and i <= j:
            ans += (S[(i - 1) % len(S)] == 'B')
            i += 1
        ans += (j - i + 1) // len(S) * S.count('B')
        i += (j - i + 1) // len(S) * len(S)
        ans += S[(i-1)%len(S):j%len(S)].count('B')
    print(f'Case #{cnt}: {ans}')