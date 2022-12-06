# [Bronze III] Nice Raises - 25812 

[문제 링크](https://www.acmicpc.net/problem/25812) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Everyone knows that the UCF Programming Team coaches are the best trainers in the world and turn out some of the best problem solvers and programmers. The UCF team members are heavily sought after by different companies. FAAMGInc has arranged a nice raise package to attract the UCF team members. When it comes to giving raises, FAAMGInc gives each team member two options: a fixed raise or double their salary. Each team member can then decide which option they’d like. For example, if the fixed raise offered by FAAMGInc is \$5,000, then a team member earning \$3,000 would choose the fixed raise option (\$5,000) but a team member making \$8,000 would pick the double the salary option since that will be a better raise (\$8,000 raise instead of \$5,000 raise).</p>

<p>Given the fixed raise offered by FAAMGInc and the salary of each team member, determine which option is picked the most.</p>

### 입력 

 <p>The first input line contains two integers: n (1 ≤ n ≤ 30), indicating the number of team members and r (1 ≤ r ≤ 50,000), indicating the fixed raise offered by FAAMGInc. Each of the next n input lines contains an integer (between 1 and 200000, inclusive) indicating the current salary for a team member.</p>

### 출력 

 <p>Output will be a single integer: 1, 2, or 0. Print 1 if the majority of the team members choose the fixed raise option, 2 if the majority pick the double the salary option, and 0 if the two options are selected by the same number of team members.</p>

<p>If a team member will end up with the same raise choosing either option, that team member doesn’t count towards either group. For example, if the fixed raise is \$2000 and a team member’s current salary is \$2000, the fixed raise and double the salary end up with the same raise for this team member so the team member doesn’t count towards either group.</p>

