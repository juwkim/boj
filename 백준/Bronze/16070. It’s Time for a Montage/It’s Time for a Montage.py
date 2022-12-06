g = lambda: [*map(int,input().split())]
n = int(input())
diff = [villain - hero for hero, villain in zip(g(), g())]
ans = diff[0]
diff = [i - ans for i in diff]
for i in diff:
    if i != 0:
        ans += (i > 0)
        break
print(max(0, ans))