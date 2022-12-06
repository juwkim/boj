I = lambda: int(input())
s = [ord(i) for i in input()]
words = [input() for _ in range(I())]
for i in range(1, 27):
    ans = ''.join([chr((c + i - 97) % 26 + 97) for c in s])
    if any(word in ans for word in words):
        print(ans)
        break