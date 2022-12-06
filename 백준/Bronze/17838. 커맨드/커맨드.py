for _ in[0]*int(input()):
    s=input()
    print(int(len(s)==7 and len({*s})==2 and s[0]==s[1]==s[4]and s[2]==s[3]==s[5]==s[6]))