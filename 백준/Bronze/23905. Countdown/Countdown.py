g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    N, K = g()
    nums = ' ' + input().replace(' ', '  ') + ' '
    comp = ' ' + '  '.join(map(str, range(K, 0, -1))) + ' '
    ans = nums.count(comp)
    
    print(f'Case #{cnt}: {ans}')