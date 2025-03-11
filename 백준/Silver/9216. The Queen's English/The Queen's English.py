ones = "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
tens = "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"

def solve(num, is_last):
    p = "and " if is_last else ""
    if num == 0:
        return ""
    elif num < 20:
        return p + ones[num]
    elif num < 100:
        return p + tens[num // 10] + ("-" + ones[num % 10] if num % 10 else "")
    else:
        return ones[num // 100] + " hundred" + (" and " + solve(num % 100, False) if num % 100 else "")

tc = 1
while n:=int(input()):
    l = []
    a = solve(n // 1000000, False)
    if a:
        l.append(a)
        l.append("million")
    b = solve(n // 1000 % 1000, False)
    if b:
        l.append(b)
        l.append("thousand")
    c = solve(n % 1000, bool(l))
    if c:
        l.append(c)
    ans = " ".join(l)
    print(f"Test {tc}: {ans}")
    tc += 1