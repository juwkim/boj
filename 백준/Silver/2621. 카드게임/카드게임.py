colors = set()
nums = []
for _ in range(5):
    color, num = input().split()
    colors.add(color)
    nums.append(int(num))
nums.sort()
a, b, c, d, e = nums

if len(colors) == 1 and all(t - s == 1 for s, t in zip(nums, nums[1:])):
    print(900 + e)
else:   
    if a == b == c == d or b == c == d == e:
        print(800 + c)
    elif a == b == c and d == e:
        print(a * 10 + d + 700)
    elif a == b and c == d == e:
        print(c * 10 + a + 700)
    elif len(colors) == 1:
        print(e + 600)
    elif all(t - s == 1 for s, t in zip(nums, nums[1:])):
        print(e + 500)
    elif a == b == c or b == c == d or c == d == e:
        print(c + 400)
    elif (a == b and (c == d or d == e)) or (b == c and d == e):
        print(d * 10 + b + 300)
    elif a == b or b == c:
        print(b + 200)
    elif c == d or d == e:
        print(d + 200)
    else:
        print(e + 100)