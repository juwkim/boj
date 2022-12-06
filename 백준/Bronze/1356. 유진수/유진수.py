def mul_list(nums):
    res = 1
    for num in nums:
        res *= num
    
    return res

def check(res1, res2):
    return res1 == res2

num = [*map(int, input())]
    
if any(check(mul_list(num[:i]), mul_list(num[i:])) for i in range(1, len(num))):
    print('YES')
else:
    print('NO')