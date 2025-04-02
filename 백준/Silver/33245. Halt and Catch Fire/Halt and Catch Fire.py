n = int(input())
program = [input().split() for _ in range(n)]
reg = {"pc": 0, "acc": 0, "cmp": 0, "out": 0}
value = lambda arg: reg[arg[1:]] if arg[0] == '$' else int(arg)
while 0 <= reg["pc"] < n:
    cmd, arg1, arg2 = program[reg["pc"]]
    match cmd:
        case "mov":
            reg[arg2[1:]] = value(arg1)
            reg["pc"] += 1
        case "add":
            reg["acc"] = value(arg1) + value(arg2)
            reg["pc"] += 1
        case "sub":
            reg["acc"] = value(arg1) - value(arg2)
            reg["pc"] += 1
        case "jeq":
            if reg["cmp"] == value(arg1):
                reg["pc"] = value(arg2)
            else:
                reg["pc"] += 1
        case "hcf":
            print(cmd, arg1, arg2)
            print(reg["acc"])
            print(reg["cmp"])
            print(reg["out"])
            break
else:
    print(reg["out"])