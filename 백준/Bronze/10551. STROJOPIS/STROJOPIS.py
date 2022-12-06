from collections import Counter
a = Counter(input())
s = "1QAZ2WSX3EDC4RFV5TGB6YHN7UJM8IK,9OL.0P;/-['=]"
t = [0, 4, 8, 12, 20, 28, 32, 36, 45]
for x, y in zip(t, t[1:]):
    print(sum(a[k] for k in s[x:y]))