H, M = map(int, input().split())
N = int(input())
pos_h, pos_m, dir_m = H * 5 % 60, M % 60, 1
visited = {(pos_h, pos_m, dir_m): 0}
check = {}
t = 0
while N:
    t += 1
    N -= 1
    pos_h = (pos_h + 1) % 60
    pos_m = (pos_m + dir_m * 2) % 60
    if pos_h == pos_m:
        dir_m = -dir_m
    state = pos_h, pos_m, dir_m
    if state in visited:
        prev_t = visited[state]
        pos_h, pos_m, dir_m = check[N % (t - prev_t) + prev_t]
        break
    else:
        visited[state] = t
        check[t] = state
print(pos_h // 5, pos_m)