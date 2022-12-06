# [Bronze II] Fegla and the Bed Bugs - 9349 

[문제 링크](https://www.acmicpc.net/problem/9349) 

### 성능 요약

메모리: 28776 KB, 시간: 72 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>Fegla, also known as mmaw, is coaching a lot of teams. All these teams train together in one place, unfortunately this place doesn’t have any good ventilation and is quite small relative to the number of teams. All these circumstances resulted in a strange creature appearing! That creature is called The Bed Bug!</p>

<p>These are parasitic bugs; they feed on human blood by biting them. What was strange and confused Fegla, is that some of the team members did not get bitten at all! However, he was more interested in eliminating these bugs. After observing the bugs’ behavior for some time, he concluded that he needed to stop them from reproducing to eliminate them. They reproduce by getting very close to each other.</p>

<p>And so, Fegla needs your help. Given a straight line of empty cells N and the number of bugs K, tell Fegla the best assignment for the bugs to maximize the minimum number of empty cells between each two consecutive bugs on that line.</p>

<p>For example, given N=4 and K=2, the answer would be 2, according to the best assignment:</p>

<table class="table table-bordered" style="width:500px">
	<tbody>
		<tr>
			<td>Bed Bug</td>
			<td>Empty</td>
			<td>Empty</td>
			<td>Bed Bug</td>
		</tr>
	</tbody>
</table>

<p> </p>

### 입력 

 <p>Input will start with an integer T representing the number of test cases. Followed by T lines each line contains two integers N, K.</p>

<p>You can assume that</p>

<ul>
	<li>2 ≤ N ≤ 200 </li>
	<li>2 ≤ K ≤ N</li>
</ul>

### 출력 

 <p>For each test case in a separate line, output the minimum distance between EACH two consecutive bugs in the best assignment.</p>

