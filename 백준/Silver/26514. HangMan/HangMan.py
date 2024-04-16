p = "  O", "\n+", "=", "|", "=", "+", "\n  |", "\n /", " \\"
for _ in range(int(input())):
    S, N, *C = input().split()
    l = sum(c not in S for c in C)
    print(S)
    if l:
        print(*p[:l], sep="")
    else:
        print("SAFE")
    print()