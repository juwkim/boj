# [Silver I] Don’t Complicate It! - 25817 

[문제 링크](https://www.acmicpc.net/problem/25817) 

### 성능 요약

메모리: 108384 KB, 시간: 96 ms

### 분류

자료 구조, 문자열, 스택

### 제출 일자

2025년 5월 17일 03:59:43

### 문제 설명

<p>The number of parentheses and the level of nesting are usually a good indication of how complicated an expression is.</p>

<p>Given a string containing only “(”, “)” and blanks (spaces), compute its complexity. The complexity is defined as follows:</p>

<ul>
	<li>Each innermost set of parentheses adds 1 to the total complexity.</li>
	<li>Each set of parentheses containing only innermost set of parentheses adds 2 to the total complexity, i.e., one level out will add 2 to the complexity.</li>
	<li>Each set of parentheses at the next level out adds 3 to the complexity, and so on.</li>
</ul>

### 입력 

 <p>There is only one input line; it contains a valid expression. The expression (string) will be 2-60 characters, each character being either “(”, “)” or blank (space). Note that the blanks can be anywhere but the string will not exceed 60 characters (including the blanks). Assume that there will be at least one set of parentheses in the input, i.e., the input will not be all blanks.</p>

<p>Note that a valid expression satisfies the following:</p>

<ol>
	<li>All the parentheses are matched, i.e., every opening parenthesis has a corresponding closing parenthesis.</li>
	<li>The matched parentheses are in the correct order, i.e., an opening parenthesis comes before its corresponding closing parenthesis.</li>
</ol>

<p>Note again that the input is a valid expression, i.e., you do not need to check for errors.</p>

### 출력 

 <p>Print the complexity of the expression.</p>

