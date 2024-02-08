# [Silver III] Matrix Chain Multiplication - 6604 

[문제 링크](https://www.acmicpc.net/problem/6604) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

자료 구조, 스택

### 제출 일자

2024년 2월 9일 00:25:18

### 문제 설명

<p>Suppose you have to evaluate an expression like A*B*C*D*E where A,B,C,D and E are matrices.</p>

<p>Since matrix multiplication is associative, the order in which multiplications are performed is arbitrary. However, the number of elementary multiplications needed strongly depends on the evaluation order you choose.</p>

<p>For example, let A be a 50*10 matrix, B a 10*20 matrix and C a 20*5 matrix.</p>

<p>There are two different strategies to compute A*B*C, namely (A*B)*C and A*(B*C).</p>

<p>The first one takes 15000 elementary multiplications, but the second one only 3500.</p>

<p>Your job is to write a program that determines the number of elementary multiplications needed for a given evaluation strategy.</p>

### 입력 

 <p>Input consists of two parts: a list of matrices and a list of expressions.</p>

<p>The first line of the input file contains one integer <em>n</em> (1 n n lines each contain one capital letter, specifying the name of the matrix, and two integers, specifying the number of rows and columns of the matrix.</p>

<p>The second part of the input file strictly adheres to the following syntax (given in EBNF):</p>

<pre>SecondPart = Line { Line } <EOF>
Line       = Expression <CR>
Expression = Matrix | "(" Expression Expression ")"
Matrix     = "A" | "B" | "C" | ... | "X" | "Y" | "Z"</pre>

### 출력 

 <p>For each expression found in the second part of the input file, print one line containing the word "error" if evaluation of the expression leads to an error due to non-matching matrices. Otherwise print one line containing the number of elementary multiplications needed to evaluate the expression in the way specified by the parentheses.</p>

