S = input()
for i in range(26):
    print(*[chr((ord(c) - i - ord('A')) % 26 + ord('A')) for c in S], sep='')