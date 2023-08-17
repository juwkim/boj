s = input()
if len(s) > 2 and s.startswith("io") and all(c.isnumeric() for c in s[2:]):
    print("Correct")
else:
    print("Incorrect")