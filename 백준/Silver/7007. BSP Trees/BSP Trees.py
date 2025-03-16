n = int(input())
x_coords, z_coords = [0] * n, [0] * n
for i in range(n):
    *_, x, z = map(int, input().split())
    x_coords[i] = x
    z_coords[i] = z

p = int(input())
A, B, C = [0] * p, [0] * p, [0] * p

for i in range(p):
    x1, z1, x2, z2 = map(int, input().split())
    A[i] = z1 - z2
    B[i] = x2 - x1
    C[i] = x1 * z2 - z1 * x2
    if B[i] < 0:
        A[i], B[i], C[i] = -A[i], -B[i], -C[i]

order = list(range(n))
is_dividing = bytearray(n + 1)
is_dividing[0], is_dividing[n] = True, True

for i in range(p):
    current_index = 0
    while current_index < n:
        next_div = current_index + 1
        while not is_dividing[next_div]:
            next_div += 1
        if next_div == current_index + 1:
            current_index = next_div
            continue
        
        front_count, back_count = 0, 0
        temp_back = [0] * n
        
        for j in range(next_div - current_index):
            if A[i] * x_coords[order[current_index + j]] + B[i] * z_coords[order[current_index + j]] + C[i] > 0:
                order[current_index + front_count] = order[current_index + j]
                front_count += 1
            else:
                temp_back[back_count] = order[current_index + j]
                back_count += 1
        is_dividing[current_index + front_count] = True
        for j in range(back_count):
            order[current_index + front_count + j] = temp_back[j]        
        current_index = next_div

print("".join(chr(order[i] + ord('A')) for i in range(n)))