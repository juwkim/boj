input()
words = []
while True:
    words += [(s:=input())]
    if s[::-1] in words:
        break
print(len(s), s[len(s)//2])