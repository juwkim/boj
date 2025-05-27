from itertools import product
from collections import Counter

def eval_ops(num, nums, ops):
    ret = num
    for num, op in zip(nums, ops):
        match op:
            case '+': ret += num
            case '-': ret = abs(ret - num)
            case '*': ret *= num
            case '/':
                if num == 0:
                    return 0
                ret //= num
    return ret

for line in [*open(0)][:-1]:
    num, *nums = list(map(int, line.split()))
    cnt = Counter()
    for ops in product('+-*/', repeat=len(nums)):
        val = eval_ops(num, nums, ops)
        if '3' in str(val):
            cnt[val] += 1
    if cnt:
        Max = max(cnt.values())
        print(max(k for k, v in cnt.items() if v == Max))
    else:
        print("No result")