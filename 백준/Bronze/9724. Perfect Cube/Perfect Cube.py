for i in range(1, int(input())+1):
    A, B = map(lambda x: int(x)**(1/3), input().split())
    print(f'Case #{i}:', int(B) - int(A) + (A == int(A)))