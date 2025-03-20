# [Silver II] Magical, Marvelous Tour (Small) - 12226 

[문제 링크](https://www.acmicpc.net/problem/12226) 

### 성능 요약

메모리: 110916 KB, 시간: 224 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2025년 3월 20일 20:11:00

### 문제 설명

<p>The mysterious owner of an electronics factory has decided to do something very intriguing. She has hidden <em>golden transistors</em> inside seven electronic devices, and the people who buy those devices will be invited to a magical, marvelous tour of the factory.</p>

<p>Arnar and Solveig have received a tip that there is a golden transistor hidden inside one device in their local electronics store. First they pooled their money together and bought all the devices, then placed them in a straight line, numbering the devices 0 to <strong>N</strong>-1. Each device has some number of transistors in it. Then they agreed on a strategy to decide who gets the golden transistor:</p>

<p>First, Arnar will select a range [a, b] (inclusive) of the devices, where 0 ≤ a ≤ b < N. Next, Solveig will choose which one set of devices she wants to take:</p>

<ul>
	<li>If a > 0, she may take all the devices in the range [0, a-1].</li>
	<li>If b < <strong>N</strong>-1, she may take all the devices in the range [b+1, N-1].</li>
	<li>She may always choose to take all the devices in the range [a, b].</li>
</ul>

<p>Once Solveig has chosen one of the sets of devices, Arnar takes all the devices she did not take.</p>

<p>For example, if there are 3 devices and Arnar selects the range [1, 1], Solveig may choose to take the range [0, 0], the range [1, 1] or the range [2, 2]. On the other hand, if Arnar selects the range [1, 2], then Solveig may choose to take the range [0, 0] or the range [1, 2].</p>

<p>Given how many transistors are in each device, and that Arnar and Solveig will each try to maximize their probability of getting the golden transistor (which is maximized by taking electronics with the maximum number of transistors), what is Arnar's probability of getting the golden transistor and thus winning the magical, marvelous tour?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> lines follow. Each line contains five numbers: <strong>N</strong>, <strong>p</strong>, <strong>q</strong>, <strong>r</strong> and <strong>s</strong>. This indicates that there are <strong>N</strong> devices, and the i<sup>th</sup> device contains ((i * <strong>p</strong> + <strong>q</strong>) MOD <strong>r</strong> + <strong>s</strong>) transistors. Remember that the devices are numbered from 0 to <strong>N</strong>-1.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>p</strong> ≤ 10<sup>6</sup>.</li>
	<li>1 ≤ <strong>q</strong> ≤ 10<sup>6</sup>.</li>
	<li>1 ≤ <strong>r</strong> ≤ 10<sup>6</sup>.</li>
	<li>1 ≤ <strong>s</strong> ≤ 10<sup>6</sup>.</li>
	<li>1 ≤ <strong>N</strong> ≤ 1000.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is Arnar's probability of winning the magical, marvelous tour.</p>

<p>y will be considered correct if it is within an absolute or relative error of 10<sup>-9</sup> of the correct answer.</p>

