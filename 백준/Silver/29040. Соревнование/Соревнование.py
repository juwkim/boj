def gen4():
    ans = []
    now = [10, 8, 7, 6]
    for i in range(k - 4): now.append((3, 2)[i & 1])
    ans.append(now)
    
    now = [0, 9, 8, 7]
    for i in range(k - 4): now.append((0, 3)[i & 1])
    ans.append(now)
    
    now = [1, 0, 9, 8]
    for i in range(k - 4): now.append((1, 0)[i & 1])
    ans.append(now)
    
    now = [2, 1, 0, 9]
    for i in range(k - 4): now.append((0, 1)[i & 1])
    ans.append(now)
    
    for it in range(n - 4):
        match it % 4:
            case 0: now = [3, 2, 1, 0]
            case 1: now = [0, 3, 2, 1]
            case 2: now = [1, 0, 3, 2]
            case 3: now = [2, 1, 0, 3]
        for i in range(k - 4): now.append((it + 1 & 1, it & 1)[i & 1])
        ans.append(now)
    return ans

def gen3():
    ans = []
    now = [10, 8, 7]
    for i in range(k - 3): now.append((3, 2)[i & 1])
    ans.append(now)
    
    now = [0, 9, 8]
    for i in range(k - 3): now.append((0, 3)[i & 1])
    ans.append(now)
    
    now = [1, 0, 9]
    for i in range(k - 3): now.append((1, 0)[i & 1])
    ans.append(now)
    
    for it in range(n - 3):
        match it % 3:
            case 0: now = [2, 1, 0]
            case 1: now = [0, 2, 1]
            case 2: now = [1, 0, 2]        
        for i in range(k - 3): now.append((it & 1, it + 1 & 1)[i & 1])
        ans.append(now)
    return ans

n, k = map(int, input().split())
if k & 1:
    ans = gen3()
else:
    ans = gen4()
for row in ans:
    print(*row)