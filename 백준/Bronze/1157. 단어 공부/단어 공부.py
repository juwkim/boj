word = input().upper()
set_word = set(word)

Max = 0
Top_alphabet = []
for alphabet in set_word:
    num = word.count(alphabet)
    if num > Max:
        Max = num
        Top_alphabet.clear()
        Top_alphabet.append(alphabet)
    elif num == Max:
        Top_alphabet.append(alphabet)

if len(Top_alphabet) == 1:
    print(Top_alphabet[0])
else:
    print('?')