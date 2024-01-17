import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def solve():
    words = input().split()
    space = int(input())
    if space < len(words) - 1:
        return -1
    title = "".join(word[0].upper() for word in words)
    words.append(title)
    cnt = g()
    for word in words:
        prev = ''
        for c in word:
            if c == prev:
                continue
            if c.islower():
                cnt[ord(c) - ord('a')] -= 1
            else:
                cnt[ord(c) - ord('A')] -= 1
            prev = c
    if any(x < 0 for x in cnt):
        return -1
    return title

print(solve())