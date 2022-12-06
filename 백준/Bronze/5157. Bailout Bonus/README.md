# [Bronze III] Bailout Bonus - 5157 

[문제 링크](https://www.acmicpc.net/problem/5157) 

### 성능 요약

메모리: 30840 KB, 시간: 976 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>In order to prevent many financial companies from collapsing, the US Government (and several other governments) “bailed them out”, in the sense that they provided multi-billion dollar emergency loans. After this happened, several of the companies went ahead and paid their executives massive performance bonuses. After a large public outcry, one approach that was taken to recoup these bonuses for the government was to impose a massive 95% tax on bonuses for employees of companies that received bailout money<sup>1</sup>. Here, you are to compute how much money the government will recover.</p>

<p>You will be given a list of the companies that received bailout money, and the proposed taxation rate r (such as 95%), written as an integer (in this case, 95). You will also be given a list of executives with their company affiliation and proposed bonus. Each executive working for a bailed out company will have to pay an r fraction of his bonus back (rounded down to the nearest integer). For simplicity, we assume that executives working for companies that weren’t bailed out have to return none of their bonus.</p>

<p><sup>1</sup>It remains to be seen whether this will be judged constitutional.</p>

### 입력 

 <p>The first line contains the number K of data sets. This is followed by K data sets, each of the following form:</p>

<p>The first line contains four integers C, B, n, r. 1 ≤ C ≤ 500 is the total number of companies. 0 ≤ B ≤ C is the number of these companies that were bailed out. 1 ≤ n ≤ 10000 is the total number of executives, and 0 ≤ r ≤ 100 is the taxation rate in percent.</p>

<p>This is followed by a line containing B integers, the indices (between 1 and C) of the bailed out companies. Finally, there are n lines, each describing one executive. Each such line consists of two integers c<sub>i</sub>, p<sub>i</sub>. 1 ≤ c<sub>i</sub> ≤ C is the company that executive i is working for, and p<sub>i</sub> is the bonus payment that executive i received.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output, on a line by itself, the total amount of money recovered by the government via taxes. Each data set should be followed by a blank line.</p>

