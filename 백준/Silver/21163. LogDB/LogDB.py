import sys
from collections import defaultdict

def skip_ws(s, i):
    n = len(s)
    while i < n and s[i].isspace():
        i += 1
    return i

def parse_name(s, i):
    i = skip_ws(s, i)
    n = len(s)
    j = i
    while j < n and (s[j].isalnum() or s[j] == '_'):
        j += 1
    return s[i:j], j

def parse(line):
    i = 0
    n = len(line)
    res = []
    while i < n:
        i = skip_ws(line, i)
        name, i = parse_name(line, i)
        i = skip_ws(line, i)
        args = []
        while line[i] != ')':
            i += 1
            arg, i = parse_name(line, i)
            args.append(arg)
            i = skip_ws(line, i)
        i += 1
        res.append((name, args))
    return res

def match_args(args, fargs):
    bindings = {}
    for qa, fa in zip(args, fargs):
        if qa[0] != '_':
            if qa != fa:
                return False
        elif qa == "_":
            continue
        elif qa in bindings:
            if bindings[qa] != fa:
                return False
        else:
            bindings[qa] = fa
    return True

db = defaultdict(list)
for line in map(str.rstrip, sys.stdin):
    if line == "":
        break
    for name, args in parse(line):
        db[(name, len(args))].append(args)

for line in map(str.rstrip, sys.stdin):
    name, args = parse(line)[0]
    print(sum(match_args(args, fargs) for fargs in db[(name, len(args))]))