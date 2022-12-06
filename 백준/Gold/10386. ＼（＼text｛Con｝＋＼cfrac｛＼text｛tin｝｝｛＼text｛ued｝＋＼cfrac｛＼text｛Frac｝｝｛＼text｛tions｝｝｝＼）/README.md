# [Gold II] \(\text{Con}+\cfrac{\text{tin}}{\text{ued}+\cfrac{\text{Frac}}{\text{tions}}}\) - 10386 

[문제 링크](https://www.acmicpc.net/problem/10386) 

### 성능 요약

메모리: 116836 KB, 시간: 248 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>The (simple) continued fraction representation of a real number r is an expression obtained by an iterative process of representing r as a sum of its integer part and the reciprocal of another number, then writing this other number as the sum of its integer part and another reciprocal, and so on. In other words, a continued fraction representation of r is of the form</p>

<p>\[r = a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \frac{1}{a_3 + \cdots}}}\]</p>

<p>where a<sub>0</sub>, a<sub>1</sub>, a<sub>2</sub>, . . . are integers and a<sub>1</sub>, a<sub>2</sub>, . . . > 0. We call the a<sub>i</sub>-values partial quotients. For example, in the continued fraction representation of 5.4 the partial quotients are a<sub>0</sub> = 5, a<sub>1</sub> = 2, and a<sub>2</sub> = 2. This representation of a real number has several applications in theory and practice.</p>

<p>While irrational numbers like √2 require an infinite set of partial quotients, any rational number can be written as a continued fraction with a unique, finite set of partial quotients (where the last partial quotient is never 1 in order to preserve uniqueness). Given two rational numbers in continued fraction representation, your task is to perform the four elementary arithmetic operations on these numbers and display the result in continued fraction representation.</p>

### 입력 

 <p>Each test case consists of three lines. The first line contains two integers n<sub>1</sub> and n<sub>2</sub>, 1 ≤ n<sub>i</sub> ≤ 9 specifying the number of partial quotients of two rational numbers r<sub>1</sub> and r<sub>2</sub>. The second line contains the partial quotients of r<sub>1</sub> and the third line contains the partial quotients of r<sub>2</sub>. The partial quotients satisfy |a<sub>0</sub>| ≤ 10 and 0 < a<sub>i</sub> ≤ 10, the last partial quotient will never be 1, and r<sub>2</sub> is non-zero. A line containing two 0’s will terminate input.</p>

### 출력 

 <p>For each test case, display the case number followed by the continued fraction representation of r<sub>1</sub>+r<sub>2</sub>, r<sub>1</sub>−r<sub>2</sub>, r<sub>1</sub>×r<sub>2</sub>, and r<sub>1</sub>/r<sub>2</sub> in order, each on a separate line. Use 64-bit integers for all of your calculations (long long in C++ and long in Java).</p>

