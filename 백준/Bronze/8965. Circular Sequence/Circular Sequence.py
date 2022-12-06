for _ in [0]*int(input()):
    s=input()
    print(sorted(s[i:]+s[:i]for i in range(len(s)))[0])