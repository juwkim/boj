# [Bronze I] Selection of Participants of an Experiment - 13280 

[문제 링크](https://www.acmicpc.net/problem/13280) 

### 성능 요약

메모리: 30840 KB, 시간: 104 ms

### 분류

브루트포스 알고리즘(bruteforcing), 정렬(sorting)

### 문제 설명

<p>Dr. Tsukuba has devised a new method of programming training. In order to evaluate the effectiveness of this method, he plans to carry out a control experiment. Having two students as the participants of the experiment, one of them will be trained under the conventional method and the other under his new method. Comparing the final scores of these two, he will be able to judge the effectiveness of his method.</p>

<p>It is important to select two students having the closest possible scores, for making the comparison fair. He has a list of the scores of all students who can participate in the experiment. You are asked to write a program which selects two of them having the smallest difference in their scores.</p>

### 입력 

 <p>The input consists of multiple datasets, each in the following format.</p>

<pre>n
a<sub>1</sub> a<sub>2</sub> … a<sub>n</sub></pre>

<p>A dataset consists of two lines. The number of students n is given in the first line. n is an integer satisfying 2 ≤ n ≤ 1000. The second line gives scores of n students. a<sub>i</sub> (1 ≤ i ≤ n) is the score of the i-th student, which is a non-negative integer not greater than 1,000,000.</p>

<p>The end of the input is indicated by a line containing a zero. The sum of n's of all the datasets does not exceed 50,000.</p>

### 출력 

 <p>For each dataset, select two students with the smallest difference in their scores, and output in a line (the absolute value of) the difference.</p>

