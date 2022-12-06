import sys
input = sys.stdin.readline

words = [input().rstrip() for _ in range(int(input()))]
s_words = {word[0] for word in words}
if any(len(set(word) - s_words) == 0 for word in words):
    print('Y')
else:
    print('N')