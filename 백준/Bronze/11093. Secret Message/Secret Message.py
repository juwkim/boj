for _ in[0]*int(input()):
    L=len(s:=input())
    M=L
    while M**.5!=int(M**.5):M+=1
    K,c=int(M**.5),''
    s+=' '*(M - L)
    for i in range(K):
        for j in range(K-1, -1, -1):c+=s[i+K*j]
    print(c.replace(' ',''))