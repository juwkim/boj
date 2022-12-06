g = lambda: [*map(int, input().split())]

N, C = g()
w = g()

max_cnt = 0
for i in range(N):
    j, cnt, cur = i, 0, 0
    while j < N:
        tmp = cur + w[j]
        if tmp < C:
            cur = tmp
            cnt += 1
            j += 1
        elif tmp == C:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
            break
        else:
            j += 1
    max_cnt = max(max_cnt, cnt)
                    
print(max_cnt)