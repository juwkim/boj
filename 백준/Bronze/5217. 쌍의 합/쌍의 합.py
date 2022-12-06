for _ in range(int(input())):
    n = int(input())
    print(f'Pairs for {n}: {", ".join([f"{i} {n-i}" for i in range(1, -(-n//2))])}')