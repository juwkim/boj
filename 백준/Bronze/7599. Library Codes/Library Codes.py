while (lib:=input()) != '# 0':
    name, f = lib.split()
    print(name, 'Library')
    for i in range(1, 1+int(input())):
        w, text = input().split()
        print('Book', i, 'horizontal' if int(w) >= int(f) * len(text) + 2 else 'vertical')