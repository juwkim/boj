def g(): return [*map(int, input().split())]

for t in range(1, int(input()) + 1):

    shakes = int(input()) * [0]
    customers = []
    for _ in range(int(input())):
        customer = []
        k, *nums = g()
        for i in range(0, k * 2, 2):
            customer.append((nums[i] - 1, nums[i + 1]))
        customers.append(customer)

    impossible = False
    solved = False
    while not impossible and not solved:
        redo = False
        for customer in customers:
            unsatisfied = []
            for flavor, malt in customer:
                if shakes[flavor] == malt:
                    unsatisfied = []
                    break
                else:
                    unsatisfied.append((flavor, malt))

            for flavor, malt in unsatisfied:
                if malt == 1 and shakes[flavor] == 0:
                    shakes[flavor] = 1
                    redo = True
                    break

            if redo:
                break

            if len(unsatisfied):
                impossible = True
                break

        if not redo:
            solved = True
            
    if impossible:
        ans = "IMPOSSIBLE"
    else:
        ans = " ".join(map(str, shakes))
    print(f"Case #{t}: {ans}")