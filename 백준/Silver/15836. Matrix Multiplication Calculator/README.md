# [Silver V] Matrix Multiplication Calculator - 15836 

[문제 링크](https://www.acmicpc.net/problem/15836) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 선형대수학(linear_algebra), 수학(math)

### 문제 설명

<p>Matrix multiplication is a basic tool of linear algebra, and has numerous applications in many areas of mathematics, as well as in applied mathematics, computer graphics, physics, and engineering.</p>

<p>We can only multiply two matrices if their dimensions are compatible, which means the number of columns in the first matrix is the same as the number of rows in the second matrix.</p>

<p>If A = [a<sub>ij</sub>] is an m×n matrix and B = [b<sub>ij</sub>] is an n×q matrix, the product AB is an m×q matrix. The product AB is defined to be the m×q matrix C = [c<sub>ij</sub>] such that</p>

<p>\[c_{ij} = \sum_{k=1}^{n}{a_{ik}b_{kj}\]</p>

<p>Your task is to design a matrix multiplication calculator to multiply two matrices and display the output. If the matrices cannot be multiplied, display "undefined"</p>

### 입력 

 <p>The input consists of a few test cases. For each test case, the first line of input is 4 positive integers, M, N, P and Q (1 ≤ M, N, P, Q ≤ 20). M and N represent the dimension of matrix A, while P and Q represent the dimension of matrix B. The following M lines consist of the data for matrix A followed by P lines that contains the data for matrix B as shown in the sample input. The test data ends when M, N, P and Q are 0.</p>

### 출력 

 <p>For each test case, the output contains a line in the format "Case #x:", where x is the case number (starting from 1). The following line(s) is the output of the matrix multiplication.</p>

