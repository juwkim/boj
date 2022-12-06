nums = [*map(int, input().split())]
dic = {nums[i]: str(i + 1) for i in range(9)}
text, ans = input(), "#"

for character in text:
    if character < 's':
        q, r = divmod(ord(character) - 91, 3)
    elif 's' < character < 'z':
        q, r = divmod(ord(character) - 92, 3)
    else:
        q, r = 7 + 2 * (character == 'z'), 3
    ans += "#" * (ans[-1] == dic[q]) + dic[q] * (r + 1)
print(ans[1:])