word = ''
K = int(input())
for i, s in enumerate(input()):
    word += chr(65 + (ord(s) - (3*i + 3 + K) - 65) % 26)
print(word)