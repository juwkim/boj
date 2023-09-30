# [Bronze III] Finding Your Roots - 30260 

[문제 링크](https://www.acmicpc.net/problem/30260) 

### 성능 요약

메모리: 116672 KB, 시간: 148 ms

### 분류

구현

### 문제 설명

<p>P-22’s father was P-1, the first mountain lion tagged in the Santa Monica Mountains. P-22’s mother is unknown. Unfortunately, we do not know anything about P-1’s parents, so we can only trace back P-22’s ancestry two generations (himself and his father). In some other cases, one can trace back ancestry quite a bit further, and you are supposed to find out just how far.</p>

<p>To keep things simple (and avoid exponential growth), we will assume that for each individual mountain lion, you are given only one parent (or none, when no information is available). You are to return the total number of generations in the ancestry of a specific mountain lion that can be traced back.</p>

### 입력 

 <p>The first line contains a number 1 ≤ K ≤ 100, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of a data set contains two integers 1 ≤ L ≤ n ≤ 10000. n is the total number of mountain lions in the database, and L is the mountain lion whose ancestry you are interested in.</p>

<p>This is followed by a single line with n integers p<sub>i</sub>, where 0 ≤ p<sub>i</sub> ≤ n is the parent of mountain lion i. A ’0’ denotes that the parent of lion i is unknown. Because these are parent relationships, there will never be cycles in the input.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the number of generations of the ancestry of L that are in the database (including L himself/herself).</p>

<p>Each data set should be followed by a blank line.</p>

