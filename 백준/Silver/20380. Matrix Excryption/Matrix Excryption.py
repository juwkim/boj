char_to_num = {chr(i + 65): i + 1 for i in range(26)}
char_to_num[' '] = 27
char_to_num[','] = 28
char_to_num['.'] = 29
char_to_num['?'] = 30
num_to_char = {v: k for k, v in char_to_num.items()}

def mod30(x):
    return (x - 1) % 30 + 1

while d:=int(input()):
    matrix = [[*map(int, input().split())] for _ in range(d)]
    nums = [char_to_num[c] for c in input() if c in char_to_num]
    r = len(nums) % d
    if r:
        nums.extend([27] * (d - r))
    result = []
    for idx in range(0, len(nums), d):
        block = nums[idx:idx + d]
        encrypted = []
        for r in range(d):
            s = sum(matrix[r][j] * block[j] for j in range(d))
            encrypted.append(mod30(s))
        result.extend(num_to_char[num] for num in encrypted)
    print("'" + ''.join(result) + "'")