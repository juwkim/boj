# [Silver III] ASLRDR - 18387 

[문제 링크](https://www.acmicpc.net/problem/18387) 

### 성능 요약

메모리: 113812 KB, 시간: 156 ms

### 분류

그리디 알고리즘, 문자열

### 제출 일자

2024년 6월 23일 18:04:51

### 문제 설명

<p>Suppose an assembly line in a factory with N stations. In each station, workers do an activity on the product that might be the same as previous or next stations’ activity. The order of these stations is not important but they should be ordered such that the product insert to line from one side (Left or Right) and exit from other side (Right or Left) without reverse movement in line. Your job is writing a program to reorder an existing assembly line so that it passed the mentioned rule. You may reorder the assembly line in several “station swapping” but you only allow swap two adjacent stations.</p>

### 입력 

 <p>The first line of input gives n, the number of assembly lines (Test Cases).</p>

<p>For each test case, one line of input follows, containing a string of up to 100 letters or digits that are the name of stations.</p>

### 출력 

 <p>Output consists of one line per test case. This line will contain the least possible number of swaps, or "Impossible" if it is not possible to reorder the stations for passing the rule.</p>

<p>For example, assume we have 3 actions that are named 2,a and D which currently are ordered in an assembly line as "2a2aD". To pass the mentioned rule it should reorder to "2aDa2" with 3 swaps as follows:</p>

<ul>
	<li>swap "aD" to yield "2a2Da"</li>
	<li>swap "2D" to yield "2aD2a"</li>
	<li>swap "2a" to yield "2aDa2"</li>
</ul>

