def solve(tokens):
    token = tokens.pop()
    if token != "(":
        return token
    function_name = tokens.pop()
    args = []
    while tokens[-1] != ")": args.append(solve(tokens))
    tokens.pop()
    return f"{function_name}({', '.join(args)})"

print(solve(input().replace("(", " ( ").replace(")", " ) ").split()[::-1]))