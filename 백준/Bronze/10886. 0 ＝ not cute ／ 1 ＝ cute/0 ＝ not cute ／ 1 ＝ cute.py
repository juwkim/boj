import sys
survey = [int(i) for i in sys.stdin.read().split() if i != '0']
print("Junhee is " + ["not ", ""][len(survey) > survey[0] // 2 + 1] + "cute!")