for i in range(1, 1+int(input())):
    n, m = map(int, input().split())
    vote = {input(): 0 for _ in range(n)}
    
    for _ in range(m):
        X, R, C = input().split()
        vote[X] += int(R)
    a = max(vote.values())
    
    if [*vote.values()].count(a) == 1:
        b = dict(map(reversed, vote.items()))[a]
        print(f'VOTE {i}: THE WINNER IS {b} {a}')
    else:
        print(f'VOTE {i}: THERE IS A DILEMMA')