# [Bronze II] Jean and Joe’s Clothes - 5100 

[문제 링크](https://www.acmicpc.net/problem/5100) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Jean and Joe are a rather untidy couple with a similar bogun taste in clothes. Their 2 children, Jane and James are also clothed in the style.</p>

<p>Jean’s mother came to stay and was horrified at the untidy state of the house. She formed a pile of clothes for each of the 4 people in the house, but could only do so by looking at the size of each item. Unfortunately sometimes the size had been cut off or wasn’t readable, so these clothes she put in a separate pile.</p>

<ul>
	<li>If the size is ‘M’ or ‘L’, then it is Joe’s.</li>
	<li>If the size is ‘S’ then it is James’.</li>
	<li>If it is 12 or greater then it is Jean’s.</li>
	<li>If it is smaller than 12 it is Jane’s.</li>
</ul>

<p>Jean’s mother makes frequent visits and has to go through this process every visit. Your task in this problem is to write a program that will assist her.</p>

### 입력 

 <p>Input consists of data for a number of visits by Jean's mother. The first line of each visit will consist of a whole number, N (0 < N <= 50), which is the total number of clothes found strewn round the house. Then follows N lines each representing the size of an item of clothing, or an ‘X’ if it is missing or unreadable. The sizes will either be a 1 or 2 digit number or a letter ‘S’, ‘M’ or ‘L’.</p>

<p>Input is finished when the number of clothes strewn, N, is 0. Do not process this line.</p>

### 출력 

 <p>Output consists of one line for each visit. The line will contain five numbers, each separated by a space. The numbers represent the number of clothes belonging to Joe, Jean, Jane and James respectively in the current visit. The final number is the number of clothes unable to be assigned to anyone. If there are no clothes in a pile, the number 0 must be shown.</p>

