import re

n, name = input().split()
if n == '2':
    snake = name
    pascal = ''.join(map(lambda s: s.capitalize(), name.split('_')))
    camel = pascal[0].lower() + pascal[1:]
else:
    if n == '1':
        camel = name
        pascal = name[0].upper() + name[1:]
    else:    
        pascal = name
        camel = name[0].lower() + name[1:]
    
    name = name[0].lower() + name[1:]
    snake = [i for i in name.lower()]
    
    for i in [m.start(0) for m in re.finditer('[A-Z]', name)][::-1]:
        snake.insert(i, '_')
    snake = ''.join(snake)
print(camel, snake, pascal)