from collections import Counter
correct = ''.join([input() for _ in range(3)])
guess = ''.join([input() for _ in range(3)])
green = sum(a == b for a, b in zip(correct, guess))
cnt_correct, cnt_guess = Counter(correct), Counter(guess)
yellow = sum(min(cnt_correct[a], cnt_guess[a]) for a in map(chr, range(65, 97))) - green
print(green, yellow)