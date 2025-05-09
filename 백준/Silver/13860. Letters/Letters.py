index = int(input())
length = 1
while True:
    count = 26**length * length
    if index < count:
        break
    index -= count
    length += 1
word_index, char_index = divmod(index, length)
s = []
for _ in range(length):
    s.append(chr(ord('A') + word_index % 26))
    word_index //= 26
print(s[-1-char_index])