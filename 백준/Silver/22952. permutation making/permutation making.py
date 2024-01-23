N = int(input())
l, r = 1, N - 1
while l < r:
    print(l, r, end=" ")
    l += 1
    r -= 1
if l == r:
    print(l, end=" ")
print(N)