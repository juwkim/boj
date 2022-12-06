front = ''
order = 1
for _ in range(int(input())):
    now = input()
    order += front != now
    front = now
print(order)