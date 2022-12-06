g = lambda: [*map(int, input().split())]

def solve():
    arr = [0, 0]
    time = 0
    for num in nums:
        if time + num > t:
            break
        arr[0] += 1
        arr[1] += time + num
        time += num
    return arr

for step in range(1, 1 + int(input())):
    t, n = g()

    nums = g()
    bill = solve()

    nums.sort()
    steve = solve()

    nums.reverse()
    linus = solve()
    
    Max = max([bill, linus, steve], key=lambda x: [x[0], -x[1]])
    if Max == steve:
        winner = 'Steve'
    elif Max == linus:
        winner = 'Linus'
    else:
        winner = 'Bill'
    print(f'Scenario #{step}:')
    print(f'{winner} wins with {Max[0]} solved problems and a score of {Max[1]}.')
    print()