import random

def get_num(s):
    nums = [*range(1, 10001)]
    random.shuffle(nums)
    i = 0
    while True:
        print(f"? {s}", nums[i], flush=True)
        if input() == '1':
            break
        i += 1
    return nums[i]

A = get_num('A')
B = get_num('B')
print(f"! {A + B}", flush=True)