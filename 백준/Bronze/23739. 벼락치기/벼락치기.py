cnt = 0
left = 30
for _ in range(int(input())):
    time = int(input())
    cnt += (time <= left * 2)
    left = left - time if left > time else 30    
print(cnt)