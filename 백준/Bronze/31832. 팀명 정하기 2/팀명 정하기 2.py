for _ in range(int(input())):
    s = input()
    if len(s) <= 10 and any(not c.isdigit() for c in s) and sum(c.isupper() for c in s) <= sum(c.islower() for c in s):
        print(s)
        break