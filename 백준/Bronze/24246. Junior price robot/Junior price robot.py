n = int(input())
t, *p = map(int, input().split())
cnt = 0
flag = False
for num in p:
    cnt += 1
    if num <= t:
        flag = True
        break
print(cnt if flag else 'infinity')