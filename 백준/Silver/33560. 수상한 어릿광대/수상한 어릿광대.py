N = int(input())
ans = [0, 0, 0, 0]
time, score = 0, 0
dtime, dscore = 4, 1
def solve():
    global time, score, dtime, dscore
    if score < 35:
        pass
    elif score < 65:
        ans[0] += 1
    elif score < 95:
        ans[1] += 1
    elif score < 125:
        ans[2] += 1
    else:
        ans[3] += 1
    time, score = 0, 0
    dtime, dscore = 4, 1

for d in map(int, input().split()):
    if time > 240:
        solve()
    match d:
        case 1:
            solve()
            continue
        case 2:
            if dscore > 1:
                dscore >>= 1
            elif dscore == 1:
                dtime += 2
        case 4:
            time += 56
        case 5:
            if dtime > 1:
                dtime -= 1
        case 6:
            if dscore < 32:
                dscore <<= 1
    score += dscore
    time += dtime
print(*ans, sep='\n')