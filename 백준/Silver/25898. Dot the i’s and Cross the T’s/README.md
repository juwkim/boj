# [Silver III] Dot the i’s and Cross the T’s - 25898 

[문제 링크](https://www.acmicpc.net/problem/25898) 

### 성능 요약

메모리: 110920 KB, 시간: 1204 ms

### 분류

브루트포스 알고리즘, 기하학

### 제출 일자

2024년 6월 14일 20:28:58

### 문제 설명

<p>Mr. T, known for his hair cut and the phrase “you fool” in the old TV series “The A Team”, has decided to try out for the UCF Programming Team. Considering the many talented students at UCF, Mr. T’s best chance is to become great at geometry. So, he sought help from Euclid, one of the Fathers of Geometry. Considering the teacher and the student, the obvious place to start is with the letter T!</p>

<p><img alt="" src="https://upload.acmicpc.net/c326328e-26b1-4adf-b3c4-e8e184af0643/-/preview/" style="width: 148px; height: 140px; float: right;">Consider the picture of the letter T to the right. We define four points A, M, B, and C form a T if three conditions holds:</p>

<ol>
	<li>M is the midpoint of AB</li>
	<li>CM = AB, i.e., CM is the same length as AB</li>
	<li>The angles AMC and BMC are 90 degrees.</li>
</ol>

<p>Given a set of points, you are to determine how many groups of four points form a T based on the above definition.</p>

### 입력 

 <p>The first input line contains an integer, n (1 ≤ n ≤ 100), indicating the number of test cases to process. Each test case starts with an integer, p (4 ≤ p ≤ 50), indicating the number of points. Each of the following p input lines provides two real numbers (each between -1000 and 1000, inclusive), indicating (respectively) the x and y coordinates for a point. Assume all points are distinct. Assume that the x and y coordinates in the input will have at most three digits after the decimal point.</p>

### 출력 

 <p>For each set of points, print “Set #n: m”, where n indicates the set number starting with 1 and m indicates how many groups of four points form a T. Two groups of four points are considered different if they differ in at least one point. Leave a blank line after the output for each set.</p>

<p>Note/Hint: This problem deals with floating-point numbers and one must be careful about checking for equality of two values. Assume two values are equal if they differ by 10<sup>-6</sup> or less.</p>

