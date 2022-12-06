g = lambda: [*map(int, input().split())]


step = 1
while sum(l:= g()):
    n, m, c = l
    cost = [0] + [int(input()) for _ in range(n)]
    state, ans = set(), 0
    for _ in range(m):
        num = int(input())
        if num in state:
            state.remove(num)
        else:
            state.add(num)
            ans = max(ans, sum(cost[num] for num in state))
    
    print(f'Sequence {step}')
    if ans > c:
        print("Fuse was blown.")
    else:
        print("Fuse was not blown.")
        print(f"Maximal power consumption was {ans} amperes.")
    print()
    step += 1