while True:
    try:
        dance = input().split()
        error = set()
        for i in range(len(dance)):
            if dance[i] != 'dip':
                continue
            if not ((i >= 1 and dance[i-1] == 'jiggle') or (i >= 2 and dance[i-2] == 'jiggle') or (i < len(dance) - 1 and dance[i+1] == 'twirl')):
                error.add(1)
                dance[i] = 'DIP'
        if dance[-3:] != ['clap', 'stomp', 'clap']:
            error.add(2)
        if 'twirl' in dance and 'hop' not in dance:
            error.add(3)
        if dance[0] == 'jiggle':
            error.add(4)
        if 'dip' not in dance and 1 not in error:
            error.add(5)
        if not error:
            print("form ok:", end=' ')
        elif len(error) == 1:
            print(f"form error {error.pop()}:", end=' ')
        else:
            *l, e = sorted(error)
            print('form errors ' + ', '.join(map(str, l)) + f' and {e}:', end=' ')
        print(*dance)
    except:
        break