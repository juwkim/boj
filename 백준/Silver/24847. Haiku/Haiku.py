buf = []
N = int(input())
for _ in range(N):
    word = 'q' + input()
    cnt = sum((a not in 'aeiou') and (b in 'aeiou') for a, b in zip(word, word[1:]))
    buf.append(cnt)


ans = 0
for i in range(N):
    a, b, c = 0, 0, 0
    p = i
    while p < N - 2 and a < 5:
        a += buf[p]
        p += 1
    if a > 5:
        continue

    while p < N - 1 and b < 7:
        b += buf[p]
        p += 1
    if b > 7:
        continue

    while p < N and c < 5:
        c += buf[p]
        p += 1

    ans += c == 5
print(ans)