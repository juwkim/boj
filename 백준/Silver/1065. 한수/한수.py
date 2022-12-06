N = int(input())

def check(num):
    digits = list(map(int, list(str(num))))
    if len(digits) <= 2:
        return True
    else:
        diff = set([])
        for i in range(len(digits) - 1):
            diff.add(digits[i] - digits[i + 1])
        if len(diff) == 1:
            return True
        else:
            return False

count = 0
for num in range(1, N + 1):
    if check(num):
        count += 1

print(count)