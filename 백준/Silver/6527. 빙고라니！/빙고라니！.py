from math import gcd

words_cnt = 0
game = 0
words = set()
word = []
for c in open(0).read() + " ":
    if c.isalpha():
        word.append(c.upper())
    elif word:
        word = "".join(word)
        if word == "BULLSHIT":
            game += 1
            words_cnt += len(words)
            words = set()
        else:
            words.add(word)
        word = []
GCD = gcd(words_cnt, game)
print(f"{words_cnt // GCD} / {game // GCD}")