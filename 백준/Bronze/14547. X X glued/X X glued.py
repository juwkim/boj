while (s:=input()) != '#':
    n, i = s.split()[1], 0
    nums = []
    while i < len(n)-1:
        if n[i] == n[i+1] and n[i] not in nums:
            nums += n[i]
            i += 2
        else:
            i += 1
    if nums:
        print(' and '.join([f'{k} {k} glued' for k in nums]))