import re
import sys
input = sys.stdin.readline

pattern = re.compile(r'([+-]?)(?:(\d*)X(?:\^(\d+))?|(\d+))')
for tc in range(1, 1 + int(input())):
    X, poly = int(input()), input()
    ans = 0
    for m in pattern.finditer(poly):
        sign_s, coef_s, exp_s, const_s = m.groups()
        if const_s is None:
            coef = 1 if coef_s in (None, '') else int(coef_s)
            exp = 1 if exp_s is None else int(exp_s)
        else:
            coef, exp = int(const_s), 0
        ans += (1, -1)[sign_s == '-'] * coef * pow(X, exp)
    print(f"Case #{tc}: {ans}")