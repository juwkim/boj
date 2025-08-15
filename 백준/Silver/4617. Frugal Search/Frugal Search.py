import sys
input = lambda: sys.stdin.readline().rstrip()

def bit(c):
    return 1 << ord(c) - 97

def parse_term(t):
    i = 0
    U, P, N = 0, 0, 0
    while i < len(t) and t[i].isalpha():
        U |= bit(t[i])
        i += 1
    while i < len(t):
        sign = t[i]
        if sign == '+':
            P |= bit(t[i+1])
        else:
            N |= bit(t[i+1])
        i += 2
    return U, P, N

while (word:=input()) != "#":
    words = [word]
    while (word:=input()) != "*":
        words.append(word)
    while (q:=input()) != "**":
        ans = "NONE"
        for w in sorted(words):
            mask = 0
            for ch in w:
                mask |= bit(ch)
            for t in q.split("|"):
                U, P, N = parse_term(t)
                if mask & U and (mask & P) == P and (mask & N) == 0:
                    ans = w
                    break
            else:
                continue
            break
        print(ans)
    print("$")