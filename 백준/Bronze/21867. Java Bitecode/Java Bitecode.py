input()
s = input()
for i in "JAV":
    s = s.replace(i, "")
print(s if len(s) else "nojava")