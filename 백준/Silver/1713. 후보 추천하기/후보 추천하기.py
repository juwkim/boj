g = lambda: [*map(int, input().split())]

N = int(input())
M = int(input())
nums = g()
when, cnt = {}, {}
for i in range(M):
    num = nums[i]
    if num in cnt:
        cnt[num] += 1
    elif len(cnt) < N:
        when[num] = i
        cnt[num] = 1
    else:
        Min = min(cnt.values())
        vals = [t for t in cnt if cnt[t] == Min]
        if len(vals) == 1:
            t = vals[0]
        else:
            t = min(vals, key=lambda x: when[x])
        del (when[t], cnt[t])
        
        when[num] = i
        cnt[num] = 1
print(*sorted(cnt))