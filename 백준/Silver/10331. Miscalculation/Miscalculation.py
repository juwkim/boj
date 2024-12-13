s = input()
num = int(input())
a = eval(s)
b = int(s[0])
for i in range(1, len(s), 2):
    if s[i] == '+':
        b += int(s[i + 1])
    else:
        b *= int(s[i + 1])
if a == num and b == num:
    print("U")
elif a == num:
    print("M")
elif b == num:
    print("L")
else:
    print("I")