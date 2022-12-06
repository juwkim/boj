from collections import Counter
N = int(input()) - 1
word = input()
for _ in range(N):
    s = input()
    a = Counter(word)
    b = Counter(s)
    if len(word) == len(s):
        if sum(v for k, v in (a&b).items()) < len(word) - 1:
            N -= 1
    elif len(word) == len(s) - 1:
        if sum(v for k, v in (b-a).items()) != 1:
            N -= 1
    elif len(word) == len(s) + 1:
        if sum(v for k, v in (a-b).items()) != 1:
            N -= 1
    else:
        N -= 1
print(N)