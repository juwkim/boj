g = lambda: [*map(int, input().split())]

N, M, T, X, Y = g()
nums = [int(input()) for _ in range(M)]
score = [0] * N
check = [[[0, 0] for _ in range(M)] for _ in range(N)]
for _ in range(Y):
    *l, state = input().split()
    t, who, problem = map(int, l)
    who -= 1
    problem -= 1
    
    if state == 'open':
        check[who][problem][0] = t
    elif state == 'incorrect':
        check[who][problem][1] += 1
    else:
        a, b = check[who][problem]
        score[who] += max(X, nums[problem] - (t - a) - 120 * b)
print(*score)