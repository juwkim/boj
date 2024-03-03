s = input()
if s[0] == s[-1] == '"' and len(s) > 2:
    print(s[1:-1])
else:
    print("CE")