jar = int(input())
cnt = [int(input()) for _ in range(3)]
l = [(35, 30), (100, 60), (10, 9)]
ans, idx = 0, 0
while jar:
    cnt[idx] += 1
    if cnt[idx] == l[idx][0]:
        cnt[idx] = 0
        jar += l[idx][1]    
    ans += 1
    idx = (idx + 1) % 3
    jar -= 1
print(f'Martha plays {ans} times before going broke.')