# [Bronze I] Baza - 12115 

[문제 링크](https://www.acmicpc.net/problem/12115) 

### 성능 요약

메모리: 148044 KB, 시간: 668 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Mirko got a summer internship in a big IT company. This company builds a large database consisting of N rows and M columns.</p>

<p>On his first day, Mirko received a total of Q queries. Each query consists of M numbers. However, some numbers got lost during transition, so they are denoted with -1. Mirko wants to know how many rows of the database correspond to the query, i.e., how many rows of t he database have identical numbers as the query, excluding -1.</p>

<p>For example, if the query is in the form of -1 3 2 ​, then we need to count the rows of the database that have any number ​in the first column, have the number 3 in the second column, and have the number 2​ in the third​ column.</p>

<p>Since he just started with his internship, Mirko needs your help. Help him and answer the queries!</p>

### 입력 

 <p>The first line of input contains N (1 ≤ N ≤ 10<sup>3</sup>) and M (1 ≤ M ≤ 10<sup>3</sup>), the size of the database.<br>
Each of the following N lines contains M numbers A<sub>ij</sub> (1 ≤ A<sub>ij</sub> ≤ 10<sup>6</sup>), the content of the database.<br>
The following line contains Q (1 ≤ Q ≤ 50), the number of queries.<br>
Each of the following Q lines contains M numbers B<sub>ij</sub> (B<sub>ij</sub> = -1 or 1 ≤ B<sub>ij</sub> ≤ 10<sup>6</sup>), the description of the i th query.</p>

### 출력 

 <p>The output must contain Q lines, each line containing X, the answer to the i th query from the task.</p>

