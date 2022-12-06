N = int(input())
exps = input()
nums = [int(input()) for _ in range(N)]

stack = []
for exp in exps:
    if exp.isalpha():
        stack.append(nums[ord(exp) - 65])
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(eval(f'{a}{exp}{b}'))
print('%.2f' % stack[0])