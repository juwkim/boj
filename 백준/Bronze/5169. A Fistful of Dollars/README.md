# [Bronze I] A Fistful of Dollars - 5169 

[문제 링크](https://www.acmicpc.net/problem/5169) 

### 성능 요약

메모리: 30840 KB, 시간: 440 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Frequently, when people kill each other, money is a primary reason<sup>1</sup>. As a result, one can often identify suspects by sudden extravagant spending. That’s why the police like to have access to financial transaction records.</p>

<p>In this problem, you are to analyze a sequence of financial transactions, and find out if one suspect stands out as spending extravagantly. You will be given the recent purchases by a number of people. Someone is a suspect if his recent purchases add up to more than twice those of any other person in that period. You are to output which suspect, if any, stands out.</p>

<p><sup>1</sup>Recall the final lines from “Fargo”: So that was Mrs. Lundegaard on the floor in there. And I guess that was your accomplice in the wood chipper. And those three people in Brainerd. And for what? For a little bit of money. There’s more to life than a little money, you know. Don’t you know that? And here ya are, and it’s a beautiful day. Well, I just don’t understand it.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line contains two integers s,t, the number of suspects 2 ≤ s ≤ 50 and financial transactions 1 ≤ t ≤ 1000.</p>

<p>This is followed by t lines, each containing two positive integers si, pi. si is the number of the person who made transaction i (1 ≤ si ≤ s) and pi the amount of money the transaction was for.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. On the next line, output the number of the suspect who spent more than twice as much as every other suspect in the data set. If there is no such suspect, output “No suspect.” instead. Each data set should be followed by a blank line.</p>

