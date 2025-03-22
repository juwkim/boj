W = input()
input()
ans = 0
for word in input().split():
    for i in range(len(word) - len(W) + 1):
        if word[i:i + len(W)] == W:
            ans += 1
print(ans)