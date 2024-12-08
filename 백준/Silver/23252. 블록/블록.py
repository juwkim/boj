for _ in range(int(input())):
    A,B,C=map(int,input().split())
    print(("No","Yes")[A>=C and(A-C)%2==0 and(C != 0 or B%2==0 or A>1)])