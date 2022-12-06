for _ in range(1, 1 + int(input())):
    print(f'Data Set {_}:')
    buf = [input() for _ in range(int(input()))]
    target = input().lower()
    for name in buf:
        idx = -1
        tmp = name.lower()
        if all((idx:= tmp.find(c, idx+1)) != -1 for c in target):
            print(name)
            
    print()