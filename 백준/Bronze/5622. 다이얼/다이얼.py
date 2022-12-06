word = input()
total = 0
for alphabet in word:
    if ord(alphabet) < ord("S"):
        total += (ord(alphabet) - 56) // 3
    elif alphabet == "S":
        total += 8
    elif alphabet == "Z":
        total += 10
    else:
        total += (ord(alphabet) - 57) // 3
print(total)