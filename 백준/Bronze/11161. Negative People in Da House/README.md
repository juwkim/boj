# [Bronze III] Negative People in Da House - 11161 

[문제 링크](https://www.acmicpc.net/problem/11161) 

### 성능 요약

메모리: 123908 KB, 시간: 156 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>The following math joke is presented for your amusement: Two mathematicians sit in a car outside a house. Two people enter the house. Then, three people are observed going out of the house. One of the mathematicians exclaim: If one person is to enter now, the house will be empty!</p>

<p>Since you have very little sense of humor, you are to write a program that will calculate the minimum number of people there must have been there to begin with. In other words, given a sequence of groups of people leaving and entering the house, output the minimum number of people there must have been before you started stalking. After writing this program, your mathematician friend will leave you, as well as their math department, to start a company specializing in joke-telling and stalking.</p>

### 입력 

 <p>The first line of the input consists of a single integer T, the number of test cases. Each of the following T cases has two parts: First, a line containing a single integer M. Then follows M lines with two integers P1 and P2 separated by a space, where the first one contains the number of people entering the house, then the number of people leaving the house. Note that these are two events: First, P1 people enter the house, then P2 people leave the house.</p>

<ul>
	<li>0 < T ≤ 50</li>
	<li>0 < M ≤ 100</li>
	<li>0 ≤ P1, P2 ≤ 1000</li>
</ul>

### 출력 

 <p>Output the minimum number of people that would have to have been inside the house at the beginning.</p>

