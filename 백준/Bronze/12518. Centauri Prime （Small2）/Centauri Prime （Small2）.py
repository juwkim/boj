for i in range(int(input())):
    if (s:=input())[-1] in 'yY':
        state = 'nobody'
    elif s[-1] in 'aeiouAEIOU':
        state = 'a queen'
    else:
        state = 'a king'
    print(f'Case #{i+1}: {s} is ruled by {state}.')