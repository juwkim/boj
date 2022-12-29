cnt = [0] * 1001
N = int(input())
ans = 'Yes'
buf = []
for num in map(int, input().split()):
    if num < 0:
        if cnt[-num]:
            cnt[-num] -= 1
        elif cnt[0]:
            cnt[0] -= 1
            buf.append(-num)
        else:
            ans = 'No'
            break
    else:
        cnt[num] += 1
print(ans)
if ans == 'Yes':
    buf.extend([1] * cnt[0])
    print(*buf)