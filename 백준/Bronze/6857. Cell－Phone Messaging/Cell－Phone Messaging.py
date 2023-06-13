d = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

dic = {}
for key, val in d.items():
    for cnt, alpha in enumerate(val, 1):
        dic[alpha] = (key, cnt)

while (word:=input()) != "halt":
    ans = dic[word[0]][1]
    for i in range(1, len(word)):
        pre, cur = dic[word[i - 1]], dic[word[i]]
        ans += cur[1] + 2 * (pre[0] == cur[0])
    print(ans)