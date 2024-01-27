from math import gcd

cnt = 0
bullshit = 0
word = []
words = set()
for c in open(0).read() + " ":
    if c.isalpha():
        word.append(c.upper())
    elif word:
        word = "".join(word)
        if word == "BULLSHIT":
            bullshit += 1
            cnt += len(words)
            words = set()
        else:
            words.add(word)
        word = []
GCD = gcd(cnt, bullshit)
print(f"{cnt // GCD} / {bullshit // GCD}")