score = {"A+": 4.5, "A": 4.0, "B+": 3.5, "B": 3.0, "C+": 2.5, "C": 2.0, "D+": 1.5, "D": 1.0, "F": 0.0}

n, Sum = 0, 0
s, i = input(), 0
while i < len(s):
    n += 1
    if i != len(s) - 1 and s[i+1] == '+':
        Sum += score[s[i:i+2]]
        i += 2
    else:
        Sum += score[s[i]]
        i += 1

print(Sum / n)