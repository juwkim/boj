g = lambda: [*map(int, input().split())]

while (s:= input()) != '0 0':
    A, B = map(int, s.split())
    
    ans = [A, B]
    A_nums = {A: 1}
    
    idx = 2
    while True:
        A = sum(int(i)**2 for i in str(A))
        if A in A_nums:
            break
        A_nums[A] = idx
        idx += 1
    
    B_nums = {B: 1}

    idx = 2
    while True:
        B = sum(int(i)**2 for i in str(B))
        if B in B_nums:
            break
        B_nums[B] = idx
        idx += 1
    
    cnt = 1e10
    for num in A_nums:
        if num in B_nums:
            cnt = min(cnt, A_nums[num] + B_nums[num])
    if cnt == 1e10:
        cnt = 0
    print(*ans, cnt)