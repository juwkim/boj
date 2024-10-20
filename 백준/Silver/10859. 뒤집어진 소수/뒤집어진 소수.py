def is_prime(num):
    if num == 1:
        return False
    if num % 2 == 0:
        return num == 2
    if num % 3 == 0:
        return num == 3
    i = 5
    while i * i <= num:
        if num % i == 0:
            return False
        if num % (i + 2) == 0:
            return False
        i += 6
    return True

S = input()
if any(c in S for c in "347") or not is_prime(int(S)):
    print("no")
else:
    P = []
    for c in S[::-1]:
        if c == "6":
            P.append("9")
        elif c == "9":
            P.append("6")
        else:
            P.append(c)
    num = int("".join(P))
    print("yes" if is_prime(num) else "no")