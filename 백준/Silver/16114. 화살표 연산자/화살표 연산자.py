X, N = map(int, input().split())
if N & 1:
    if N > 1:
        print("ERROR")
    elif X < 0:
        print("INFINITE")
    else:
        print(0)
elif N:
    print(max(0, (X - 1) // (N // 2)))
elif X > 0:
    print("INFINITE")
else:
    print(0)