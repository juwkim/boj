for _ in range(int(input())):
    input()
    k = sum(map(int, input().split()))
    print('Right' if k > 0 else 'Left' if k < 0 else 'Equilibrium')