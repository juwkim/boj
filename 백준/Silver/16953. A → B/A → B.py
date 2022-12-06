A, B = map(int, input().split())
count = 1
while B > A:
    count += 1
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    else:
        break
    if A == B:
        break
print(count if A == B else -1)