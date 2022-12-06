while (N := int(input())):
    time = [0 for _ in range(1440)]
    
    for _ in range(N):
        start, end = input().split('-')
        
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        
        a = start_h * 60 + start_m
        b = end_h * 60 + end_m
        
        for i in range(a, b):
            time[i] += 1
    
    print('no ' * (2 not in time) + 'conflict')