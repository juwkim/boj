ans = -1
P1, P2, P3, X1, X2, X3 = map(int, input().split())
for i in range(X1, P1 * P2 * P3 + 1, P1):
    if i % P2 == X2 and i % P3 == X3:
        ans = i
        break
print(ans)