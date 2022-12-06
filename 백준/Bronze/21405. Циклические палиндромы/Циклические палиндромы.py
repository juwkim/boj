word = input()
ans = 'no'
for i in range(len(word)):
    if word == word[::-1]:
        ans = 'yes'
        break
    word = word[-1] + word[:-1]
print(ans)