for i in range(1, 1+int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    s = sum(a[i-1] < a[i] > a[i+1] for i in range(1, n-1))
    print(f'Case #{i}: {s}')