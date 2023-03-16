g = lambda: [*map(int, input().split())]

C, N = g()
check = bytearray(C + 1)
for num in g():
    check[num] = True

error, correct = [], []
for i in range(1, C + 1):
    if check[i] == True:
        error.append(i)
    else:
        correct.append(i)

def solve(arr, st):
    A = []
    l, r = 0, 1
    while r < len(arr):
        while r < len(arr) and arr[r] == arr[r - 1] + 1:
            r += 1
        if arr[l] == arr[r - 1]:
            A.append(arr[l])
        else:
            A.append(f'{arr[l]}-{arr[r - 1]}')
        l = r
        r = r + 1
    if r == len(arr):
        A.append(arr[l])
    
    print(f'{st}: {A[0]}', end='')
    for i in range(1, len(A) - 1):
        print(f", {A[i]}", end='')
    print(f" and {A[-1]}")

solve(error, 'Errors')
solve(correct, 'Correct')