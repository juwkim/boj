# [Bronze I] Similarity Computation - 15466 

[문제 링크](https://www.acmicpc.net/problem/15466) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation)

### 문제 설명

<p>The Jaccard similarity coefficient is usually used for measuring the similarity of two sets. Give two sets A and B, the Jaccard similarity coefficient, J(A, B), is defined as the size of the intersection divided by the size of the union of the two sets. That is, J(A, B) = |A∩B|/|A∪B|. For example, if A = {1, 3, 7, 8} and B = {1, 7, 9}, then J(A, B) = |{1,7}|/|{1,3,7,8,9}| = 2/5.</p>

<p>Assume the element i in the set is an integer between 0 to 9 (0 ≤ i ≤ 9) and the size of the set is no larger than 10. Please write a program to compute the Jaccard similarity coefficient of two sets A and B. And output 1 if J(A, B) > 0.5 and 0 if J(A, B) ≤ 0.5.</p>

### 입력 

 <p>The first line of the input file contains an integer T (T ≤ 25) indicating the number of test cases to follow.</p>

<p>Each test case will consist of three lines. The first line contains two integers m and n (0 < m, n ≤ 10), indicating the number of elements of sets A and B, respectively. The second line contains m integers (the elements of set A) and the third line contains n integers (the elements of set B).</p>

<p>You may assume:</p>

<ul>
	<li>1 ≤ T ≤ 25</li>
	<li>m ≤ 10 and n ≤ 10</li>
</ul>

### 출력 

 <p>For each test case, output 1 if J(A, B) > 0.5 and 0 if J(A, B) ≤ 0.5.</p>

