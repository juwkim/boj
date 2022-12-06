# [Bronze III] POT - 11772 

[문제 링크](https://www.acmicpc.net/problem/11772) 

### 성능 요약

메모리: 121220 KB, 시간: 104 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>The teacher has sent an e-mail to her students with the following task:</p>

<p>"Write a programme that will determine and output the value of \(X\) if given the statement:</p>

<p>\[X = number_1^{pot_1} + number_2^{pot_2} + \dots + number_N^{pot_N}\]</p>

<p>and it holds that \(number_1\), \(number_2\) to \(number_N\) are integers, and \(pot_1\), \(pot_2\) to \(pot_N\) one-digit integers." Unfortunately, when the teacher downloaded the task to her computer, the text formatting was lost so the task transformed into a sum of \(N\) integers:</p>

<p>\[X = P_1 + P_2 + ... + P_N\]</p>

<p>For example, without text formatting, the original task in the form of \(X = 21^2 + 125^3\) became a task in the form of \(X = 212 + 1253\). Help the teacher by writing a programme that will, for given \(N\) integers from \(P_1\) to \(P_N\) determine and output the value of \(X\) from the original task.</p>

<p>Please note: We know that it holds a \(N = a \cdot a \cdot \dots \cdot a\) (\(N\) times).</p>

### 입력 

 <p>The first line of input contains the integer \(N\) (1 ≤ \(N\) ≤ 10), the number of the addends from the task. Each of the following \(N\) lines contains the integer \(P_i\) (10 ≤ \(P_i\) ≤ 9999, \(i\) = 1 ... \(N\)) from the task.</p>

### 출력 

 <p>The first and only line of output must contain the value of \(X\) (\(X\) ≤ 1 000 000 000) from the original task.</p>

