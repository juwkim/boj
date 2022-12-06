for _ in range(int(input())):
    m = int(input())
    dna_list = [input() for _ in range(m)]
    ans = 'no significant commonalities'
    find = 'Z'
    for l in range(60, 2, -1):
        for i in range(61-l):
            target = dna_list[0][i:i+l]
            if all(target in dna_list[j] for j in range(1, m)):
                find = min(find, target)
        if find != 'Z':
            break
    if find == 'Z':
        print(ans)
    else:
        print(find)