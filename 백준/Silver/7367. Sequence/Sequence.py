while n:= int(input()):
    s = input()
    p = max(s)
    nums = s.split()
    
    p = int(p) + 1
    flag = False
    while p <= 10:
        buf = [int(num, p) for num in nums]
        if len(set(a - b for a, b in zip(buf, buf[1:]))) == 1:
            flag = True
            break
        p += 1
    if flag:
        print(f'Minimum base = {p}.')
    else:
        print('No base <= 10 can be found.')