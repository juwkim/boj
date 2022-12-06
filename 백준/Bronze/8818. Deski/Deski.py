for _ in[0]*int(input()):
    s = len(str(int(bin(int(input()))[2:][::-1])))
    print(0 if s == 1 else s)