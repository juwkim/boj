n, s = int(input()), input()
for _ in range(n):
    t = ''
    count, now = 1, s[0]
    for i in range(1, len(s)):
        if s[i] == now:
            count += 1
        else:
            t += str(count) + now
            count, now = 1, s[i]
    s = t + str(count) + now
print(s)