cake = [0 for _ in range(int(input()))]

max_idx, max_dis = 0, 0
real_idx, real_dis = 0, 0
for i in range(1, 1 + int(input())):
    s, t = map(int, input().split())
    
    if t - s > max_dis:
        max_idx = i
        max_dis = t - s
    
    temp = sum(cake[k] == 0 for k in range(s-1, t))
    
    if temp > real_dis:
        real_idx = i
        real_dis = temp
    
    for j in range(s-1, t):
        cake[j] = 1

print(max_idx, real_idx)