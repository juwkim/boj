for _ in range(int(input())):
    N = int(input())
    robots = [input() for _ in range(N)]
    winner = [*range(N)]
    for l in zip(*robots):
        cur = {"R": [], "S": [], "P": []}
        for robot in winner:
            cur[l[robot]].append(robot)
        if sum(val == [] for val in cur.values()) != 1:
            continue
        if not cur["R"]:
            winner = cur["S"]
        elif not cur["S"]:
            winner = cur["P"]
        else:
            winner = cur["R"]
        if len(winner) == 1:
            break
    if len(winner) == 1:
        print(winner[0] + 1)
    else:
        print(0)