for _ in range(int(input())):
    if len(s:=input())%2:
        s += s
    one = ''.join(s[i] for i in range(len(s)) if not i%2)    
    two = ''.join(s[i] for i in range(len(s)) if i%2)
    print(one, two, sep='\n')