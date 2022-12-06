# [Bronze II] Iterated Difference - 4807 

[문제 링크](https://www.acmicpc.net/problem/4807) 

### 성능 요약

메모리: 30840 KB, 시간: 1964 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>You are given a list of N non-negative integers a(1), a(2), ... , a(N). You replace the given list by a new list: the k-th entry of the new list is the absolute value of a(k) - a(k+1), wrapping around at the end of the list (the k-th entry of the new list is the absolute value of a(N) - a(1)). How many iterations of this replacement are needed to arrive at a list in which every entry is the same integer?</p>

<p>For example, let N = 4 and start with the list (0 2 5 11). The successive iterations are:</p>

<pre>2 3 6 11
1 3 5 9
2 2 4 8
0 2 4 6
2 2 2 6
0 0 4 4
0 4 0 4
4 4 4 4</pre>

<p>Thus, 8 iterations are needed in this example.</p>

### 입력 

 <p>The input will contain data for a number of test cases. For each case, there will be two lines of input. The first line will contain the integer N (2 <= N <= 20), the number of entries in the list. The second line will contain the list of integers, separated by one blank space. End of input will be indicated by N = 0.</p>

### 출력 

 <p>For each case, there will be one line of output, specifying the case number and the number of iterations, in the format shown in the sample output. If the list does not attain the desired form after 1000 iterations, print 'not attained'.</p>

