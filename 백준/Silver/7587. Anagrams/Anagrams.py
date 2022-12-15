while n:= int(input()):
    buf = []
    nums = [0] * n
    for i in range(n):
        word = input()
        for j in range(len(buf)):
            if sorted(word) == sorted(buf[j]):
                nums[i] += 1
                nums[j] += 1
        buf.append(word)
    idx = max(range(n), key=lambda x: (nums[x], -x))
    print(buf[idx], nums[idx])