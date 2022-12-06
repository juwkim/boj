N, M, A = map(int, input().split())
mid = M//2 + 1
while (S:=int(input())) != mid:
    A = 1 + (A+S-mid-1)%N
    print(A)
print(0)