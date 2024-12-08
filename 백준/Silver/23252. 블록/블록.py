for _ in range(int(input())):
    A,B,C=map(int,input().split())
    print(("No","Yes")[C and A>=C and(A-C)%2==0 or C==0 and A%2==0 and(B%2==0 or A>1)])