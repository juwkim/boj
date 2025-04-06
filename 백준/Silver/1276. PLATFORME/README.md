# [Silver I] PLATFORME - 1276 

[문제 링크](https://www.acmicpc.net/problem/1276) 

### 성능 요약

메모리: 123720 KB, 시간: 244 ms

### 분류

구현, 정렬

### 제출 일자

2025년 4월 7일 07:57:08

### 문제 설명

<p>A level is being designed for a new platform game. The locations of the platforms have been chosen. Contrary to popular opinion, platforms can't float in the air, but need pillars for support. More precisely, each of the two ends of the platform needs to be supported by a pillar standing on the floor or on a different platform. </p>

<p>You will be given the locations of the platforms in a coordinate system as in the left image below. Each platform's location is determined by its altitude (vertical distance from the ground) and the start and end coordinates in the horizontal direction. Each support pillar is placed half a unit from the end of a platform, as in the right image. </p>

<p>Determine the total length of pillars needed to support all the platforms. </p>

<table class="table table-bordered td-center">
	<tbody>
		<tr>
			<td style="width:50%;"><img alt="" src="https://upload.acmicpc.net/914de249-cbd7-426c-9864-cb9e15bac82b/-/preview/" style="width: 290px; height: 176px;"></td>
			<td style="width:50%;"><img alt="" src="https://upload.acmicpc.net/6298c0a1-72b7-46ce-a5ea-80585dde87e6/-/preview/" style="width: 291px; height: 176px;"></td>
		</tr>
		<tr>
			<td style="width:50%;">Example level with three platforms. The lowest platform is at altitude 1, the second lowest at altitude 3 and the third at altitude 5.</td>
			<td style="width:50%;">The total length of pillars needed to support all platforms is 14.</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>The first line contains the integer N, 1 ≤ N ≤ 100, the number of platforms. </p>

<p>Each of the following N lines contains the position of one platform, three coordinates Y, X<sub>1</sub> and X<sub>2</sub>. <span style="line-height:1.6em">The first number is the altitude, the other two the horizontal coordinates. All coordinates will be positive integers less than 10000 satisfying X<sub>2</sub> > X<sub>1</sub>+1 (i.e. the length of each platform will be at least 2). </span></p>

<p>The input will be such that no two platforms overlap. </p>

### 출력 

 <p>Output the total length of pillars needed to support all the platforms. </p>

