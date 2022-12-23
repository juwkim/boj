nums = (5, 7, 5, 7, 7) 
while n:= int(input()):
    words = [len(input()) for _ in range(n)]
    i = 0
    while True:
        j, k, num = 0, 0, 0
        flag = False
        while True:
            num += words[i + j]
            if num > nums[k]:
                break
            if num == nums[k]:
                k += 1
                if k == 5:
                    flag = True
                    break
                num = 0
            j += 1
        if flag:
            break
        i += 1
    print(i + 1)