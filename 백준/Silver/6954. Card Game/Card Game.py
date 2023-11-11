import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

dic = {"jack": 1, "queen": 2, "king": 3, "ace": 4}

score = [0, 0]
deck = [input() for _ in range(52)]
for i in range(52):
    card = deck[i]
    if card not in dic:
        continue
    if 51 - i < dic[card]:
        continue
    if all(nextCard not in dic for nextCard in deck[i + 1:i + 1 + dic[card]]):
        score[i&1] += dic[card]
        print(f"Player {'AB'[i&1]} scores {dic[card]} point(s).")
print(f"Player A: {score[0]} point(s).")
print(f"Player B: {score[1]} point(s).")