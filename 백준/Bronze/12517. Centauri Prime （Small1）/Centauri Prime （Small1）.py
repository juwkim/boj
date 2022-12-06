for i in range(int(input())):
    if (s:=input())[-1] == 'y':
        state = 'nobody'
    elif s[-1] in 'aeiou':
        state = 'a queen'
    else:
        state = 'a king'
    print(f'Case #{i+1}: {s} is ruled by {state}.')