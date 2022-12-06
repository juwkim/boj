for _ in range(int(input())):
    m, n = map(int, input().split())

    blocks = [*zip(*[input().split() for _ in range(m)])]
    
    
    total = 0
    for block in blocks:
        zeros = block.count('0')
        
        after = (m * (m + 1) - zeros * (zeros + 1)) // 2
        before = sum(i + 1 for i in range(m) if block[i] == '1')
        
        diff = after - before
        total += diff
        
    print(total)