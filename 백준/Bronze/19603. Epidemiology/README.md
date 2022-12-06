# [Bronze I] Epidemiology - 19603 

[문제 링크](https://www.acmicpc.net/problem/19603) 

### 성능 요약

메모리: 32952 KB, 시간: 72 ms

### 분류

구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p>People who study epidemiology use models to analyze the spread of disease. In this problem, we use a simple model.</p>

<p>When a person has a disease, they infect exactly R other people but only on the very next day. No person is infected more than once. We want to determine when a total of more than P people have had the disease.</p>

<p><em>This problem was designed before the current coronavirus outbreak, and we acknowledge the distress currently being experienced by many people worldwide because of this and other diseases. We hope that including this problem at this time highlights the important roles that computer science and mathematics play in solving real-world problems.</em></p>

### 입력 

 <p>There are three lines of input. Each line contains one positive integer. The first line contains the value of P. The second line contains N, the number of people who have the disease on Day 0. The third line contains the value of R. Assume that P ≤ 10<sup>7</sup> and N ≤ P and R ≤ 10.</p>

### 출력 

 <p>Output the number of the first day on which the total number of people who have had the disease is greater than P.</p>

