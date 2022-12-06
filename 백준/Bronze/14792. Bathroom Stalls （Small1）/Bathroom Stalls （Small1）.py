from math import log
for i in range(1, 1+int(input())):
    N, K = map(int, input().split())
    d = int(log(K, 2))
    x, y = N%2, 1 - N%2 # 홀수, 짝수의 갯수
    nums = set([N])
    for _ in range(d):
        temp_x, temp_y = 0, 0
        temp = set()
        for _ in range(len(nums)):
            a, b = divmod(nums.pop(), 2)
            if b:
                temp.update([a])
                if a%2:
                    temp_x += 2*x
                else:
                    temp_y += 2*x
            else:
                temp.update([a-1, a])
                temp_x += y 
                temp_y += y
        x = temp_x
        y = temp_y
        nums = temp

    if (max(nums)%2 and K < 2**d + x) or (max(nums)%2 == 0 and K < 2**d + y):
        t = max(nums)
    else:
        t = min(nums)
    print(f'Case #{i}: {t//2} {t//2+t%2-1}')