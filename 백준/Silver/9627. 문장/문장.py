import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def num_to_english(num):
    if num <= 10:
        return ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"][num]
    if num <= 19:
        return ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][num - 11]
    if num <= 99:
        return ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][num // 10 - 2] + (num_to_english(num % 10) if num % 10 else "")
    return num_to_english(num // 100) + "hundred" + (num_to_english(num % 100) if num % 100 else "")

N = int(input())
words = [input() for _ in range(N)]
cnt = sum(map(len, words)) - 1
num = 1
while True:
    eng = num_to_english(num)
    if cnt + len(eng) == num:
        words[words.index("$")] = eng
        break
    num += 1
print(*words)