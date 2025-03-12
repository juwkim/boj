l = input().split()
n, *c = map(int, l[::2])
name = l[1::2]
m = int(input())
nums = []
for num in c[::-1]:
    m, r = divmod(m, num)
    nums.append(r)
nums.append(m)
nums = nums[::-1]
def is_round_up(i):
    if i + 1 == n:
        return False
    if nums[i + 1] * 2 >= c[i]:
        return True
    if nums[i + 1] * 2 + 1 == c[i]:
        return is_round_up(i + 1)
    return False

print(f"{nums[0] + is_round_up(0)} {name[0]}")
p, q = nums[0], nums[1] + is_round_up(1)
if q == c[0]:
    p, q = p + 1, 0
print(f"{p} {name[0]} {q} {name[1]}")