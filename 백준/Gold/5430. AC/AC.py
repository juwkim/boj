for _ in range(int(input())):
    p = input()
    s, e, rev = 0, int(input()), 0
    arr = input()
    
    for cmd in p:
        if cmd == "R": rev ^= 1
        elif rev: e -= 1
        else: s += 1

    if s > e: print("error")
    else:
        arr = arr[1:-1].split(",")[s:e]
        if rev: arr = arr[::-1]
        print(f"[{','.join(arr)}]")