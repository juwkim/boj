line = input()
nums, ops = [], []
pos = 0
for i in range(len(line)):
    if line[i] in "+-":
        nums.append(int(line[pos:i]))
        ops.append(line[i])
        pos = i + 1
nums.append(int(line[pos:i+1]))

total = nums[0]
for i in range(len(ops)):
    if ops[i] == "-":
        total -= sum(nums[i+1:])
        break
    else:
        total += nums[i+1]
print(total)