from fractions import Fraction

buf = ["SAME", "TAOYUAN", "JAKARTA"]
R1, R2, S1, S2 = input().split()
R1, R2 = int(R1), int(R2)
S1, S2 = Fraction(S1), Fraction(S2)

if R1 == 1 and R2 == 1:
    ans = buf[(S1 > S2) - (S1 < S2)]
elif R1 == 1:
    ans = buf[1]
elif R2 == 1:
    ans = buf[2]
else:
    a, b = (R2 - 1) * S1, (R1 - 1) * S2
    ans = buf[(a > b) - (a < b)]
print(ans)