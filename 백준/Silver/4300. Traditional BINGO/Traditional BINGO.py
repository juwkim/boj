input = __import__('sys').stdin.readline

def g(): return [*map(int, input().split())]

for _ in range(int(input())):
    nums = [g() for _ in range(5)]
    nums[2] = nums[2][:2] + [0] + nums[2][2:]
    buf = [set(line) for line in nums]
    buf.extend([set(line) for line in zip(*nums)])
    buf.append(set(nums[i][i] for i in range(5)))
    buf.append(set(nums[i][4 - i] for i in range(5)))
    
    for Set in buf:
        Set -= {0}
    
    def solve():

        cards = []
        while len(cards) != 75:
            cards.extend(g())

        for cnt, num in enumerate(cards, 1):
            for Set in buf:
                if num in Set:
                    Set.remove(num)
                    if not Set:
                        return cnt
    
    cnt = solve()
    print(f'BINGO after {cnt} numbers announced')