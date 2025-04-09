# [Silver III] The mysterious X network - 7449 

[문제 링크](https://www.acmicpc.net/problem/7449) 

### 성능 요약

메모리: 127640 KB, 시간: 272 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 9일 10:37:11

### 문제 설명

<p>One of the reasons for which École polytechnique (nicknamed “X” for reasons to be explained during the debriefing talk) is so deeply rooted in French society is its famous network of camarades — former students of the same school. When one camarade wants something (money, job, etc.), he can ask this network for help and support. In practice, this means that when he/she wants to reach some other camarade, not always of the same year, then surely he can find intermediate camarades to get to her/him. Note that the “camarade” relationship is symmetric. Due to the magic of the X network, there is always a means to reach anybody.</p>

<p>The program you have to write is supposed to help to minimize the number of these intermediate camarades.</p>

### 입력 

 <p>The input begins with a single positive integer on a line by itself indicating the number of the cases following, each of them as described below. This line is followed by a blank line, and there is also a blank line between two consecutive inputs.</p>

<p>The huge file of all living camarades is simplified so as to obey the following format. The first line in the file is the number of camarades, say N, an integer 1 ≤ N ≤ 10<sup>5</sup>. Camarades are labeled from 0 to N − 1. Follow N lines. Each line starts with the camarade label c, followed by the number of other camarades he/she knows, say nc, followed by the labels of those nc camarades. All these integers are separated by a single blank. It is assumed that nc is always less than 100. The last line in the file is the label of the camarade seeking help (say c<sub>1</sub>) followed by the label of the camarade he wants help from, say c<sub>2</sub> (c<sub>2</sub> ≠ c<sub>1</sub>).</p>

### 출력 

 <p>For each test case, your program should output three integers separated by a blank: c<sub>1</sub>, c<sub>2</sub> and the minimal number of intermediate camarades to reach c<sub>2</sub>.</p>

<p>The outputs of two consecutive cases will be separated by a blank line.</p>

