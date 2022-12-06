# [Bronze I] Entrance Examination - 11038 

[문제 링크](https://www.acmicpc.net/problem/11038) 

### 성능 요약

메모리: 115556 KB, 시간: 188 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>The International Competitive Programming College (ICPC) is famous for its research on competitive programming. Applicants to the college are required to take its entrance examination.</p>

<p>The successful applicants of the examination are chosen as follows.</p>

<ul>
	<li>The score of any successful applicant is higher than that of any unsuccessful applicant.</li>
	<li>The number of successful applicants n must be between nmin and nmax, inclusive. We choose n within the specified range that maximizes the gap. Here, the gap means the difference between the lowest score of successful applicants and the highest score of unsuccessful applicants.</li>
	<li>When two or more candidates for n make exactly the same gap, use the greatest n among them.</li>
</ul>

<p>Let's see the first couple of examples given in Sample Input below. In the first example, nmin and nmax are two and four, respectively, and there are five applicants whose scores are 100, 90, 82, 70, and 65. For n of two, three and four, the gaps will be 8, 12, and 5, respectively. We must choose three as n, because it maximizes the gap.</p>

<p>In the second example, nmin and nmax are two and four, respectively, and there are five applicants whose scores are 100, 90, 80, 75, and 65. For n of two, three and four, the gap will be 10, 5, and 10, respectively. Both two and four maximize the gap, and we must choose the greatest number, four.</p>

<p>You are requested to write a program that computes the number of successful applicants that satisfies the conditions.</p>

### 입력 

 <p>The input consists of multiple datasets. Each dataset is formatted as follows.</p>

<pre>m n<sub>min</sub> n<sub>max</sub>
P<sub>1</sub>
P<sub>2</sub>
...
P<sub>m</sub></pre>

<p>The first line of a dataset contains three integers separated by single spaces. m represents the number of applicants, nmin represents the minimum number of successful applicants, and nmax represents the maximum number of successful applicants. Each of the following m lines contains an integer P<sub>i</sub>, which represents the score of each applicant. The scores are listed in descending order. These numbers satisfy 0 < n<sub>min</sub> < n<sub>max</sub> < m ≤ 200, 0 ≤ P<sub>i</sub> ≤ 10000 (1 ≤ i ≤ m) and P<sub>n<sub>min</sub></sub> > P<sub>n<sub>max</sub>+1</sub>. These ensure that there always exists an n satisfying the conditions.</p>

<p>The end of the input is represented by a line containing three zeros separated by single spaces.</p>

### 출력 

 <p>For each dataset, output the number of successful applicants in a line.</p>

