def cmp(a, b):
    return (a > b) - (a < b)

for j in range(1, 1+int(input())):
    seq = input().split()[1:]
    
    blue = [int(seq[i+1]) for i in range(0, len(seq), 2) if seq[i] == 'B']
    orange = [int(seq[i+1]) for i in range(0, len(seq), 2) if seq[i] == 'O']
    order = [k for k in seq if k in 'BO']
    
    b_pos, o_pos = 1, 1
    time = 0
    
    for _ in range(len(order)):
        now = order.pop(0)

        if now == 'O':
            goal = orange.pop(0)
            b_move = blue and blue[0] or 0
                
            while o_pos != goal:
                time += 1
                o_pos += cmp(goal, o_pos)
                b_pos += cmp(b_move, b_pos)

            b_pos += cmp(b_move, b_pos)
            time += 1
            
        else:
            goal = blue.pop(0)
            o_move = orange and orange[0] or 0
                
            while b_pos != goal:
                time += 1
                b_pos += cmp(goal, b_pos)
                o_pos += cmp(o_move, o_pos)

            o_pos += cmp(o_move, o_pos)
            time += 1
    print(f'Case #{j}: {time}')