g = lambda: [*map(int, input().split())]
for i in range(int(input())):
    N = int(input())
    num, *l = sorted(g())
    tot = 0
    for x in l:
        tot ^= x
    if tot == num:    
        ans = sum(l)
    else:
        ans = 'NO'
    print(f'Case #{i+1}: {ans}')