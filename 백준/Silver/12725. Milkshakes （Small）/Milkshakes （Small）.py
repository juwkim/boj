def g(): return [*map(int, input().split())]

def check():

    while True:
        for customer in customers:
            satisfied = False
            change_flavor = None
            for flavor, malt in customer:
                if shakes[flavor] == malt:
                    satisfied = True
                    break
                elif malt == 1 and shakes[flavor] == 0:
                    change_flavor = flavor

            if satisfied:
                continue

            if change_flavor == None:
                return False
            
            shakes[change_flavor] = 1
            break

        else:
            return True
            
for t in range(1, int(input()) + 1):

    shakes = int(input()) * [0]
    customers = []

    for _ in range(int(input())):
        customer = []
        k, *nums = g()
        for i in range(0, k * 2, 2):
            customer.append((nums[i] - 1, nums[i + 1]))
        customers.append(customer)
            
    solved = check()
    if solved:
        ans = " ".join(map(str, shakes))
    else:
        ans = "IMPOSSIBLE"
    print(f"Case #{t}: {ans}")