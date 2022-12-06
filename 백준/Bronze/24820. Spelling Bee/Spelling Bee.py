import sys
input = sys.stdin.readline
s = input()
p = {*s}
for _ in range(int(input())):
    word = input().rstrip()
    if len(word) >= 4 and (s[0] in word) and (not ({*word} - p)):
        print(word)