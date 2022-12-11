N, K = map(int, input().split())
buf = [input().split() for _ in range(N)]
buf.sort(key=lambda x: (-int(x[2]), int(x[3])))
check = set()
for uni, team, solved, penalty in buf:
    if uni not in check:
        check.add(uni)
        print(team)
        K -= 1
        if K == 0:
            break