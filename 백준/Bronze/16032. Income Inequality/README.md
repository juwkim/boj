# [Bronze II] Income Inequality - 16032 

[문제 링크](https://www.acmicpc.net/problem/16032) 

### 성능 요약

메모리: 47016 KB, 시간: 248 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>We often compute the average as the first step in processing statistical data. Yes, the average is a good tendency measure of data, but it is not always the best. In some cases, the average may hinder the understanding of the data.</p>

<p>For example, consider the national income of a country. As the term <i>income inequality</i> suggests, a small number of people earn a good portion of the gross national income in many countries. In such cases, the average income computes much higher than the income of the vast majority. It is not appropriate to regard the average as the income of typical people.</p>

<p>Let us observe the above-mentioned phenomenon in some concrete data. Incomes of <i>n</i> people, <i>a</i><sub>1</sub>, … , <i>a<sub>n</sub></i>, are given. You are asked to write a program that reports the number of people whose incomes are less than or equal to the average (<i>a</i><sub>1</sub> + … + <i>a<sub>n</sub></i>) / <i>n</i>.</p>

### 입력 

 <p>The input consists of multiple datasets, each in the following format.</p>

<pre><i>n</i>
<i>a</i><sub>1</sub> <i>a</i><sub>2</sub> … <i>a<sub>n</sub></i></pre>

<p>A dataset consists of two lines. In the first line, the number of people <i>n</i> is given. <i>n</i> is an integer satisfying 2 ≤ <i>n</i> ≤ 10 000. In the second line, incomes of <i>n</i> people are given. <i>a<sub>i</sub></i> (1 ≤ <i>i</i> ≤ <i>n</i>) is the income of the <i>i</i>-th person. This value is an integer greater than or equal to 1 and less than or equal to 100 000.</p>

<p>The end of the input is indicated by a line containing a zero. The sum of <i>n</i>'s of all the datasets does not exceed 50 000.</p>

### 출력 

 <p>For each dataset, output the number of people whose incomes are less than or equal to the average.</p>

