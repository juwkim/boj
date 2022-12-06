# [Bronze II] Alarmist - 5121 

[문제 링크](https://www.acmicpc.net/problem/5121) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>aAs an end-of-the-world alarmist, you’re always looking for new data to support your end-of-the-world theories. A common form of data is a series of scalar samples over time, for instance the outdoor temperature taken at one second intervals for an entire day, or the height of the tide measured every minute for a month. Given such a sampling, you’d like to check if the difference between the maximum sample and minimum sample is large, that way you can yell and scream that the world has undergone serious change and thus is about to end.</p>

<p>The problem is, such data sets often contain some erroneous samples whose scalar values are too large or too small, due to transient errors in monitoring equipment. In order to make your claims more believable, you want to smooth out these erroneous values by calculating what’s called a moving average. Given a series of n samples s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>n</sub> and a window size w where w ≤ n, a moving average consists of n − w + 1 elements. The first element of the moving average is the average of the first w samples s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>w</sub>. The second element of the moving average is the average of the same window, except shifted one element forward, i.e. the average of samples s<sub>2</sub>, s<sub>3</sub>, ..., s<sub>w+1</sub>. And so on. For simplicity, round each element of the moving average down to the nearest equal or lesser integer.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line of each data set contains the integers n and w, the number of samples and the window size, respectively, where 1 ≤ n ≤ 100 and 1 ≤ w ≤ n. The next line contains n non-negative integers representing the samples. Each sample is at most 1000.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. On the next line, output the absolute difference between the maximum and minimum element of the moving average. Each data set should be followed by a blank line.</p>

