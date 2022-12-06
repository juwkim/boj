count = [0] * 26
s = [input().split() for _ in [0]*int(input())]
for word1, word2 in s:
    check1, check2 = [0] *26, [0] * 26
    for alpha in word1:
        check1[ord(alpha)-97] += 1
    for alpha in word2:
        check2[ord(alpha)-97] += 1    
    for i in range(26):
        count[i] += max(check1[i], check2[i])

print(*count)