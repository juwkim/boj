import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n, *exec_times, quantum = map(int, input().split())
programs = []
for _ in range(n):
    program = []
    while (s:=input()) != "end":
        program.append(s)
    programs.append(program)

variables = {c: 0 for c in map(chr, range(97, 123))}
ready_queue = deque([(i, 0) for i in range(n)])
blocked_queue = deque()
lock_held = False

while ready_queue:
    pid, line_index = ready_queue.popleft()
    program = programs[pid]
    remaining_time = quantum
    
    while line_index < len(program) and remaining_time > 0:
        statement = program[line_index]
        if "=" in statement:
            var, value = statement.split(" = ")
            variables[var] = value
            remaining_time -= exec_times[0]
        elif statement.startswith("print"):
            var = statement.split()[1]
            print(f"{pid + 1}: {variables[var]}")
            remaining_time -= exec_times[1]
        elif statement == "lock":
            if lock_held:
                blocked_queue.append((pid, line_index))
                break
            else:
                lock_held = True
                remaining_time -= exec_times[2]
        elif statement == "unlock":
            lock_held = False
            if blocked_queue:
                ready_queue.appendleft(blocked_queue.popleft())
            remaining_time -= exec_times[3]
        line_index += 1
    else:
        if line_index < len(program):
            ready_queue.append((pid, line_index))