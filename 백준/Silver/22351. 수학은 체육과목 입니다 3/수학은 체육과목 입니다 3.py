S = input()
A = 1
while True:
    cur = 0
    num = A
    while cur < len(S):
        if num != int(S[cur:cur+len(str(num))]):
            break
        cur += len(str(num))
        num += 1
    if cur == len(S):
        print(A, num - 1)
        break
    A += 1