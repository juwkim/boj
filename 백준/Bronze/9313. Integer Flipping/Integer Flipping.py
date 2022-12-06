while(n:=int(input()))!=-1:
    print(int(bin(n)[2:].zfill(32)[::-1],2))