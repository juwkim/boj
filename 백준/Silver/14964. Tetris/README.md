# [Silver I] Tetris - 14964 

[문제 링크](https://www.acmicpc.net/problem/14964) 

### 성능 요약

메모리: 108384 KB, 시간: 96 ms

### 분류

구현

### 제출 일자

2025년 4월 21일 11:18:28

### 문제 설명

<p>Ivica is a passionate computer scientist. He recently started working on his first computer game: a clone of the popular Tetris. Although he’s far from being finished, his program supports placing five different Tetris figures shown in the image below in a matrix. Before placing it in the Tetris matrix, the figure can be rotated by 90 degrees an arbitrary number of times and coloured. Additionally, the current version of the game doesn’t support placing the figure if that would mean it goes out of the matrix boundaries or overlaps with another existing figure in the matrix.</p>

<table class="table" style="width:100%">
	<tbody>
		<tr>
			<td style="text-align:center; vertical-align:bottom; width:20%"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14964/1.png" style="height:57px; width:55px"></td>
			<td style="text-align:center; vertical-align:bottom; width:20%"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14964/2.png" style="height:36px; width:93px"></td>
			<td style="text-align:center; vertical-align:bottom; width:20%"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14964/3.png" style="height:64px; width:76px"></td>
			<td style="text-align:center; vertical-align:bottom; width:20%"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14964/4.png" style="height:56px; width:72px"></td>
			<td style="text-align:center; vertical-align:bottom; width:20%"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14964/5.png" style="height:61px; width:79px"></td>
		</tr>
		<tr>
			<td style="text-align:center; width:20%">Figure 1</td>
			<td style="text-align:center; width:20%">Figure 2</td>
			<td style="text-align:center; width:20%">Figure 3</td>
			<td style="text-align:center; width:20%">Figure 4</td>
			<td style="text-align:center; width:20%">Figure 5</td>
		</tr>
	</tbody>
</table>

<p>While Ivica was in school, his sister Marica started the game and randomly rotated, coloured and placed the figures in a way that the adjacent figures are coloured differently. Two figures are adjacent if they share a common side or touch in the tip.</p>

<p>When Ivica came back to his computer, he found the game running with the figures his sister placed. He wants to know how many of which figures there are in the Tetris matrix and he is asking you to help him solve this problem while he’s busy with improving the game.</p>

### 입력 

 <p>The first line of input contains positive integers N and M (1 ≤ N, M ≤ 10) that represent the number of rows and columns of the Tetris matrix. Each of the following N lines contains M characters that represent the matrix.</p>

<p>Each character can be ‘.’ (dot) that represents a blank space or a lowercase letter of the English alphabet that represents a part of the figure. Different letters represent different colours, and the parts of the same figure are coloured the same.</p>

### 출력 

 <p>You must output exactly five rows. The i th line must contain the number of appearances of the i th figure in the game of Tetris.</p>

