for _ in range(int(input())):
    a = [*map(int, input().split())]
    print('YES' if all(a[i] == a[i-1] + a[i-2] for i in range(3, a[0]+1)) else 'NO')