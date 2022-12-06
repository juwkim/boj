N = int(input())
P = int(input())

if N < 5:
    ans = P
elif N < 10:
    ans = P - 500
elif N < 15:
    ans = min(P - 500, P * 9 // 10)
elif N < 20:
    ans = min(P - 2000, P * 9 // 10)
else:
    ans = min(P - 2000, P * 3 // 4)
print(max(0, ans))