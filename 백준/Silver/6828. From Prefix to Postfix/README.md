# [Silver I] From Prefix to Postfix - 6828 

[문제 링크](https://www.acmicpc.net/problem/6828) 

### 성능 요약

메모리: 108384 KB, 시간: 112 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 6월 19일 03:24:15

### 문제 설명

<p>Prefix notation is a non-conventional notation for writing arithmetic expressions. The standard way of writing arithmetic expressions, also known as infix notation, positions a binary operator between the operands, e.g., 3 + 4, while in prefix notation the operator is positioned before the operands, e.g., + 3 4. Similarly, the prefix notation for 5 − 2 is − 5 2. A nice property of prefix expressions with binary operators is that parentheses are not required since there is no ambiguity about the order of operations. For example, the prefix representation of 5 − (4 − 2) is − 5 − 4 2, while the prefix representation of (5 − 4) − 2 is − − 5 4 2. The prefix notation is also known as Polish notation, due to Jan Łukasiewicz, a Polish logician, who invented it around 1920.</p>

<p>Similarly, in postfix notation, orreverse Polish notation, the operator is positioned after the operands. For example, postfix representation of the infix expression (5 − 4) − 2 is 5 4 − 2 −.</p>

<p>Your task is to write a program that translates a prefix arithmetic expression into a postfix arithmetic expression.</p>

### 입력 

 <p>Each line contains an arithmetic prefix expression. The operators are + and -, and numbers are all single-digit decimal numbers. The operators and numbers are separated by exactly one space with no leading spaces on the line. The end of input is marked by 0 on a single line. You can assume that each input line contains a valid prefix expression with less than 20 operators.</p>

### 출력 

 <p>Translate each expression into postfix notation and produce it on a separate line. The numbers and operators are separated by at least one space. The final 0 is not translated.</p>

