for _ in range(int(input())):
    A,B,C=map(int,input().split())
    print(("No","Yes")[(A>=C)*(A&1==C&1)*(C!=0 or ~B&1 or A>1)])