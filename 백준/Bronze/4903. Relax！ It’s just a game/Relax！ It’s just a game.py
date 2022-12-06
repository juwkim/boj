while(s:=input())[0]!='-':  
    A,B=map(int,s.split())
    print(f"{A}+{B}{'!'*(1 not in[A,B])+'='}{A+B}")