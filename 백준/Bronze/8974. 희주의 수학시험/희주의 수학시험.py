ans = []
for i in range(1, 46):
    ans += [i for _ in range(i)]
A, B = map(int, input().split())
print(sum(ans[A-1:B]))