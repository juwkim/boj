N = int(input())
if N == 2:
    print("NO")
else:
    print("YES")
    if N == 1:
        print(1)
    else:
        print(1, 3, 2, *range(4, N + 1))