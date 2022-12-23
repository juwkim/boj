ans = [0, 0]
for c in input():
    ans[c == 'C'] += 1
print(ans[0] // 2 + ans[1] // 2)