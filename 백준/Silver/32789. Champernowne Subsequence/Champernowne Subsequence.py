n = int(input())
s = input()
k, i = 1, 0
while i < n:
    for c in str(k):
        if c == s[i]:
            i += 1
            if i == n:
                print(k)
                break
    k += 1