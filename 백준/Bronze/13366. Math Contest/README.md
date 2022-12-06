# [Bronze I] Math Contest - 13366 

[문제 링크](https://www.acmicpc.net/problem/13366) 

### 성능 요약

메모리: 2392 KB, 시간: 252 ms

### 분류

수학(math), 정수론(number_theory)

### 문제 설명

<p>International Mathematical Olympiad (IMO) 2016 was held on 11th – 12th July. There are 3 problems in each day and one of them is as follows.</p>

<p>Problem 2. Find all positive integers n for which each cell of an n × n table can be filled with one of the letters I, M and O in such a way that:</p>

<ul>
	<li>In each row and each column, one third of the entries are I, one third are M and one third are O; and</li>
	<li>In any diagonal, if the number of entries on the diagonal is a multiple of three, then one third of the entries are I, one third are M, and one third are O.</li>
</ul>

<p>Note: The rows and columns of an n × n table are each labelled 1 to n in a natural order. Thus each cell corresponds to a pair of positive integers (i,j) with 1 ≤ i, j ≤ n. For n > 1, the table has 4n-2 diagonals of two types. A diagonal of the first type consists of all cells (i,j) for which i+ j is a constant, and a diagonal of the second type consists of all cells ( i,j) for which i-j is a constant.</p>

<p>The answer of this question is all positive integers which is divisible by 9 ( n = 9k for some positive integer k). However, you are now participating ACM-ICPC contest, not IMO, so the question is changed to “Determine whether the given positive integer x can be used as n in the given problem?”</p>

### 입력 

 <p>The first line contains the number of test cases T (1 ≤ T ≤ 1000)</p>

<p>For each test case, there will be an integer x (1 ≤ x ≤ 10<sup>100 000</sup>)</p>

### 출력 

 <p>For each test case, print ‘YES’ if x can be used as n, and ‘NO’otherwise, both without quote.</p>

