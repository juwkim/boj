for _ in[0]*int(input()):
    s=input()
    a=len(s)//2
    print('Do-it'+'-Not'*(s[a]!=s[a-1]))