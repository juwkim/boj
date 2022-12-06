g = lambda: [*map(int, input().split())]

N, S, M = g()
least = None
for month in range(1, 13):
    ans = 0
    N1 = month + 10
    N2 = S
    for N3 in range(10, N+1):
        if not (11 <= N3 <= 22):
            num = N1 * 1000 + N2 * 100 + N3 % 100
            if num % (N1 + N2) == 0 or num % (N1 + N3) == 0 or num % (N2 + N3) == 0:
                ans += 1
                if month == M and least == None:
                    least = N3
    print(ans)
    
if least:
    print(M + 10, S, least)
else:
    print(0, 0, 0)