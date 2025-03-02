nums = sorted(l.count('1') for l in open(0))
if nums == [0, 4, 4] or nums == [0, 0, 4]:
    print("No")
else:
    print("Yes")