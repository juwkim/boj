while n:=int(input()):
    print(*[int(input()) for _ in range(n)][::-1], sep='\n')
    print(0)