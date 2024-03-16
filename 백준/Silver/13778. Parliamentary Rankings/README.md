# [Silver III] Parliamentary Rankings - 13778 

[문제 링크](https://www.acmicpc.net/problem/13778) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

구현

### 제출 일자

2024년 3월 17일 06:59:02

### 문제 설명

<p>A group of journalists decided it would be quite fun to rank the performance of MPs in parliament each week, and have asked you to write a program to help them.</p>

<p>The journalists were convinced that most MPs did not do very much at all, but came up with a list of codes that would identify actions taken by MPs which they considered noteworthy. They associated points with each action, some positive and some negative. The current table of actions and points follows. If your program is a success and the scheme catches on, more will be added later. </p>

<table class="table table-bordered" style="width:500px">
	<tbody>
		<tr>
			<td style="text-align:center">Code</td>
			<td>Action </td>
			<td style="text-align:center">Points </td>
		</tr>
		<tr>
			<td style="text-align:center">S</td>
			<td>Made a speech lasting at least 5 minutes</td>
			<td style="text-align:center">+10</td>
		</tr>
		<tr>
			<td style="text-align:center">Q</td>
			<td>Asked a question during Question Time </td>
			<td style="text-align:center">+5</td>
		</tr>
		<tr>
			<td style="text-align:center">A</td>
			<td>Answered a question during Question Time </td>
			<td style="text-align:center">+7</td>
		</tr>
		<tr>
			<td style="text-align:center">L</td>
			<td>Spent less than an hour in the chamber</td>
			<td style="text-align:center">-8</td>
		</tr>
		<tr>
			<td style="text-align:center">F</td>
			<td>Made a funny remark that caused laughter in the chamber</td>
			<td style="text-align:center">+4</td>
		</tr>
		<tr>
			<td style="text-align:center">D</td>
			<td>Made a derisory comment about another party </td>
			<td style="text-align:center">-5</td>
		</tr>
		<tr>
			<td style="text-align:center">E</td>
			<td>Was asked to leave the chamber </td>
			<td>-10</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>Input will contain data for one week. It will start with a line containing a positive integer N (0 < N <= 120), the number of MPs who attended the debating chamber of parliament in the week in question. There then follow N lines, each giving data on 1 MP. Data will be a unique identifying number, I (0 < I <= 120) followed by a space, followed by the name of the MP. The length of name does not exceed 20.</p>

<p>The list of MPs will be followed by a positive integer, A (0 < A <200), the number of action entries that complete the data. Each of the A lines following will contain data on 1 recorded action of an MP. It will consist of the MP’s unique identifying number, followed by a space, followed by one of the letter codes from the table above. The points for each MP have to be added to give their points score for the week.</p>

### 출력 

 <p>Output the points score and name of the best scoring MP, and the points score and name of the worst scoring MP each on a separate line. In the case of equal scores, list on the same line all MPs with those scores in order of their unique identifying number, and separated by a space.</p>

