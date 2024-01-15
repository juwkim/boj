import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

A, B, C = g()
general, special = {}, {}
for _ in range(A):
    name, cost = input().split()
    general[name] = int(cost)
for _ in range(B):
    name, cost = input().split()
    special[name] = int(cost)
service = {input() for _ in range(C)}
general_cost, special_cost = 0, 0
service_menu = []
for _ in range(int(input())):
    menu = input()
    if menu in general:
        general_cost += general[menu]
    elif menu in special:
        special_cost += special[menu]
    else:
        service_menu.append(menu)
if general_cost < 20000:
    if special_cost or service_menu:
        print('No')
    else:
        print('Okay')
elif general_cost + special_cost < 50000:
    if service_menu:
        print('No')
    else:
        print('Okay')
elif len(service_menu) > 1:
    print('No')
else:
    print('Okay')