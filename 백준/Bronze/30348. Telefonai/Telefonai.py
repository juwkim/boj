nums = []
for _ in range(int(input())):
    s = input()
    if all(a < b for a, b in zip(s, s[1:])) or all(a == b for a, b in zip(s, s[1:])):
        nums.append(int(s))
if nums:
    print(min(nums))
else:
    print("NERASTA")