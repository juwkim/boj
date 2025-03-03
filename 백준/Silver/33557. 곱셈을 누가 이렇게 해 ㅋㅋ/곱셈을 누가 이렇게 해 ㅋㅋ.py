for _ in range(int(input())):
    A, B = sorted(input().split(), key=len)
    d = len(B) - len(A)
    l = [B[:d]]
    for i in range(len(A)):
        l.append(str(int(A[i]) * int(B[i + d])))
    print(+(int(A) * int(B) == int("".join(l))))