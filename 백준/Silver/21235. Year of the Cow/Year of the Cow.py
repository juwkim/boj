import sys
input = lambda: sys.stdin.readline().rstrip()

zodiacs = {c: i for i, c in enumerate(("Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"))}
years = {"Bessie": 0}
for _ in range(int(input())):
    cow1, _, _, direction, zodiac, _, _, cow2 = input().split()
    target, cur = zodiacs[zodiac], years[cow2]
    if direction == "next":
        diff = (target - cur - 1) % 12 + 1
        years[cow1] = cur + diff
    else:
        diff = (cur - target - 1) % 12 + 1
        years[cow1] = cur - diff
print(abs(years["Elsie"]))