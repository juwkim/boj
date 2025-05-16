n = int(input())
s = input()
cnt = 0
i = 0
while i < n:
    j = i
    while j < n and s[j] == s[i]:
        j += 1
    cnt += j - i >> 1
    i = j
print(cnt)