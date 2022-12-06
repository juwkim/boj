A, B = map(int, input().split())
A += 1
flag = 0
while A < 63:
    if str(pow(2, A))[0] == str(B):
        flag = 1
        break
    A += 1
print(A if flag else 0)