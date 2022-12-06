ans = ''
T = int(input())
while T:
    ans = str(T % 9) + ans
    T //= 9
print(ans)