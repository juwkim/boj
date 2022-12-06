for cnt in range(1, 1 + int(input())):
    N = int(input())
    S = input()
    buf = [1]
    cur = 1
    for i in range(1, N):
        if S[i] > S[i-1]:
            cur += 1
        else:
            cur = 1
        buf.append(cur)
    print(f'Case #{cnt}:', *buf)