# [Bronze III] Presidential Election - 25829 

[문제 링크](https://www.acmicpc.net/problem/25829) 

### 성능 요약

메모리: 113248 KB, 시간: 104 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Presidential election is coming up (November). In 2016, Clinton won the “majority” votes but Trump ended up with more “electoral” votes and won the race. (As a reminder, if a candidate receives more votes in a state, that candidate wins all the electoral votes for that state, i.e., electoral votes for a state are not divided proportionally based on the votes received by each candidate in that state.)</p>

<p>Election is in less than two months so let’s predict the outcome! Given the voting data for each state, determine who wins the majority votes and who wins the electoral votes.</p>

### 입력 

 <p>The first input line contains an integer, n (1 ≤ n ≤ 50), indicating the number of states. Each of the next n input lines contains three integers, providing voting data for a state: e (1 ≤ e ≤ 100), indicating electoral votes for the state, v1 (0 ≤ v1 ≤ 1000), indicating votes for the first candidate, and v2 (0 ≤ v2 ≤ 1000; v2 ≠ v1), indicating votes for the second candidate.</p>

### 출력 

 <p>Print 1 (one) if the first candidate wins both the majority votes and the electoral votes. Print 2 (two) if the second candidate wins both the majority votes and the electoral votes. Print 0 (zero) for all the other cases. Assume that if the total majority votes for the two candidates tie, neither one wins the majority. Similarly, if the total electoral votes for the two candidates tie, neither one wins the electoral.</p>

