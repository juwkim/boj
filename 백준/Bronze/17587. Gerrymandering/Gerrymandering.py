P, D = map(int, input().split())
vote = [[0, 0] for _ in range(D)]
total = 0
for _ in range(P):
    d, A, B = map(int, input().split())
    vote[d-1][0] += A
    vote[d-1][1] += B
    total += A + B

m = 0
for a,b in vote:
    winner = 'AB'[a < b]
    if winner == 'A':
        s, t = a - (a + b) // 2 - 1, b
    else:
        s, t = a, b - (a + b) // 2 - 1
    m += s - t
    print(winner, s, t)
print(abs(m) / total)