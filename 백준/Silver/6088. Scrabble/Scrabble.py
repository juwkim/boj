from itertools import product

val = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
    'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
    'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4,
    'Z': 10
}

def get_score(word, score):
    for c in word:
        score += val[c]
    return score

def find(add):
    global ans, max_score
    if add:
        start = sum(val[x] for x in add)
    else:
        start = 0
    s = "".join(sorted(alpha + list(add)))
    if s in dic:
        word = dic[s]
        score = get_score(dic[s], -start)
        if score > max_score or (score == max_score and word < ans):
            ans, max_score = word, score

T = int(input())
alpha = []
vacant = 0
for _ in range(T):
    c = input()
    if c == '#':
        vacant += 1
    else:
        alpha.append(c)
dic = {}
with open("dict.txt", "r") as f:
    for word in map(str.rstrip, f.readlines()):
        p = "".join(sorted(word))
        if p in dic:
            continue
        dic[p] = word
ans, max_score = "", 0
for add in product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=vacant):
    find(add)
print(ans)