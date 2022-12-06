for _ in[0]*int(input()):
    N,C,S=input().split()
    for _ in[0]*int(C):S=S[int(N):]+S
    print(S)