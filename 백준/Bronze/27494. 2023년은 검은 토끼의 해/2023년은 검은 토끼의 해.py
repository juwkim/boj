ans = 0
target = '2023'
for i in range(2023, int(input()) + 1):
    
    idx = 0
    for c in str(i):
        if c == target[idx]:
            idx += 1
            if idx == 4:
                break
    ans += idx == 4
print(ans)