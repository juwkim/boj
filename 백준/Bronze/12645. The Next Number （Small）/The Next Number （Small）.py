for cnt in range(1, 1 + int(input())):  
    s = input()
    num, num_len = [*s], len(s)
    flag = False
    for i in range(num_len - 1, -1, -1):
        tmp = num[i]
        candidate = [(num[j], j) for j in range(i+1, num_len) if tmp < num[j]]
        if candidate:
            swap_idx = min(candidate)[1]
            num[i], num[swap_idx] = num[swap_idx], num[i]
            flag = True
            break
    if flag:
        num[i+1:] = sorted(num[i+1:])
    else:
        a = min([i for i in num if i != '0'])
        num.remove(a)
        num = [a, '0'] + sorted(num)
    print(f'Case #{cnt}:', ''.join(num))