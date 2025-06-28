# [Silver I] Bee Maja - 6575 

[문제 링크](https://www.acmicpc.net/problem/6575) 

### 성능 요약

메모리: 110916 KB, 시간: 120 ms

### 분류

구현, 시뮬레이션, 많은 조건 분기

### 제출 일자

2025년 6월 28일 21:31:25

### 문제 설명

<p>Maja is a bee. She lives in a bee hive with thousands of other bees. This bee hive consists of many hexagonal honey combs where the honey is stored in.</p>

<p>But bee Maja has a problem. Willi told her where she can meet him, but because Willi is a male drone and Maja is a female worker they have different coordinate systems.</p>

<table class="table">
	<tbody>
		<tr>
			<td style="text-align: center;"><strong>Maja's Coordinate System</strong></td>
			<td style="text-align: center;"><strong>Willi's Coordinate System</strong></td>
		</tr>
		<tr>
			<td style="text-align:center">Maja who often flies directly to a special honey comb has laid an advanced two dimensional grid over the whole hive.</td>
			<td style="text-align:center">Willi who is more lazy and often walks around just numbered the cells clockwise starting from 1 in the middle of the hive.</td>
		</tr>
		<tr>
			<td style="text-align:center"><img alt="Maja" src="https://www.acmicpc.net/upload/images2/bee2.gif"></td>
			<td style="text-align:center"><img alt="Willi" src="https://www.acmicpc.net/upload/images2/bee1.gif"></td>
		</tr>
	</tbody>
</table>

<p>Help Maja to convert Willi's system to hers. Write a program which for a given honey comb number gives the coordinates in Maja's system.</p>

### 입력 

 <p>The input file contains one or more integers which represent Willi's numbers. Each number stands on its own in a separate line, directly followed by a newline. The honey comb numbers are all less than 100 000.</p>

### 출력 

 <p>You should output the corresponding Maja coordinates to Willi's numbers, each coordinate pair on a separate line.</p>

