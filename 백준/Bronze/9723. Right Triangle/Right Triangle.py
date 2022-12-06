for i in range(1, 1+int(input())):
    a,b,c=sorted(map(int,input().split()))
    print(f"Case #{i}: {['NO', 'YES'][a**2 + b**2 == c**2]}")