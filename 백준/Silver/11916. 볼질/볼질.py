g = lambda: [*map(int, input().split())]

N = int(input())
ans = 0
ball_cnt = 0
state = [0, 0, 0]
for num in g():
    fogto = False
    if num == 1:
        ball_cnt += 1
    elif num == 2:
        ball_cnt = 4
    else:
        ball_cnt += 1
        fogto = True


    if ball_cnt == 4 and fogto:
        ball_cnt = 0
        ans += state[2]
        state = [1] + state[:2]
            
    elif ball_cnt == 4:
        ball_cnt = 0
        if state[0]:
            if state[1]:
                ans += state[2]
                state[2] = 1
            else:
                state[1] = 1
        else:
            state[0] = 1
    elif fogto:
        ans += state[2]
        state = [0] + state[:2]
print(ans)