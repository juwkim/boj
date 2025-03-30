def gen4(n, k):
    ans = []
    now = [10, 8, 7, 6]
    for i in range(k - 4):
        now.append(3 if i % 2 == 0 else 2)
    ans.append(now)
    
    now = [0, 9, 8, 7]
    for i in range(k - 4):
        now.append(0 if i % 2 == 0 else 3)
    ans.append(now)
    
    now = [1, 0, 9, 8]
    for i in range(k - 4):
        now.append(1 if i % 2 == 0 else 0)
    ans.append(now)
    
    now = [2, 1, 0, 9]
    for i in range(k - 4):
        now.append(0 if i % 2 == 0 else 1)
    ans.append(now)
    
    for it in range(n - 4):
        if it % 4 == 0:
            now = [3, 2, 1, 0]
        elif it % 4 == 1:
            now = [0, 3, 2, 1]
        elif it % 4 == 2:
            now = [1, 0, 3, 2]
        else:
            now = [2, 1, 0, 3]
        
        for i in range(k - 4):
            now.append((it + 1) % 2 if i % 2 == 0 else it % 2)
        ans.append(now)
    
    return ans

def gen3(n, k):
    ans = []
    now = [10, 8, 7]
    for i in range(k - 3):
        now.append(3 if i % 2 == 0 else 2)
    ans.append(now)
    
    now = [0, 9, 8]
    for i in range(k - 3):
        now.append(0 if i % 2 == 0 else 3)
    ans.append(now)
    
    now = [1, 0, 9]
    for i in range(k - 3):
        now.append(1 if i % 2 == 0 else 0)
    ans.append(now)
    
    for it in range(n - 3):
        if it % 3 == 0:
            now = [2, 1, 0]
        elif it % 3 == 1:
            now = [0, 2, 1]
        else:
            now = [1, 0, 2]
        
        for i in range(k - 3):
            now.append(it % 2 if i % 2 == 0 else (it + 1) % 2)
        ans.append(now)
    
    return ans

n, k = map(int, input().split())
if k % 2 == 1:
    ans = gen3(n, k)
else:
    ans = gen4(n, k)

for row in ans:
    print(*row)
