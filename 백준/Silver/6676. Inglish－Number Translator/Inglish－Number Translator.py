word_to_number = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
}

def parse_number(words):
    total = 0
    for word, value in ("million", 1_000_000), ("thousand", 1_000), ("hundred", 100):
        if word in words:
            idx = words.index(word)
            total += parse_number(words[:idx]) * value
            words = words[idx + 1:]

    for word in words:
        if word in word_to_number:
            total += word_to_number[word]

    return total

for l in open(0):
    words = l.split()
    if not words:
        continue
    negative = False
    if words[0] == "negative":
        negative = True
        words = words[1:]
    total = parse_number(words)
    if negative:
        total = -total
    print(total)