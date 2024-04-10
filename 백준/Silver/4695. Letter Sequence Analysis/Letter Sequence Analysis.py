from collections import Counter

words = open(0).read().upper().split()
for l in range(1, 6):
    cnt = Counter()
    for word in words:
        for i in range(len(word) - l + 1):
            p = word[i:i + l]
            if not p.isalpha():
                continue
            cnt[p] += 1
    print(f"Analysis for Letter Sequences of Length {l}")
    print("-----------------------------------------")
    fre, sec, i = 0, [], 5
    for p, c in cnt.most_common():
        if c != fre:
            if sec:
                print(f"Frequency = {fre}, Sequence(s) = ({','.join(sorted(sec))})")
                i -= 1
            fre, sec = c, [p]
            if i == 0:
                break
        elif c == fre:
            sec.append(p)
    if i and sec:
        print(f"Frequency = {fre}, Sequence(s) = ({','.join(sorted(sec))})")
    print()