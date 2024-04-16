# [Silver III] Dinoscan - 15065 

[문제 링크](https://www.acmicpc.net/problem/15065) 

### 성능 요약

메모리: 109240 KB, 시간: 112 ms

### 분류

구현

### 제출 일자

2024년 4월 17일 04:32:42

### 문제 설명

<p>Sarah Tops is a paleontologist who specializes in the reconstruction of dinosaur skeletons. One problem which she faces is determining whether two bones mesh together correctly. She has taken scans of all the bones in her collection, so instead of physically trying to put bones together she plans to use the scans to determine the appropriate connections between bones. Below on the left are scans of the ends of two different bones:</p>

<table class="table" style="width:100%">
	<tbody>
		<tr>
			<td style="text-align:center; width:33%"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15065/1.png" style="height:106px; width:126px"></td>
			<td style="text-align:center; width:34%"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15065/2.png" style="height:106px; width:78px"></td>
			<td style="text-align:center; width:33%"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15065/3.png" style="height:105px; width:102px"></td>
		</tr>
		<tr>
			<td style="text-align:center; width:33%">Scan 1</td>
			<td style="text-align:center; width:34%">Scan 2</td>
			<td style="text-align:center; width:33%">Combined</td>
		</tr>
	</tbody>
</table>

<p>In each scan, a 1 indicates bone and a 0 indicates empty space. Two bones mesh together if the two scans can be put together to form a solid rectangle of 1’s with no overlap. Scan 1 above can mesh with Scan 2 (as shown above on the right), but Scan 1 cannot mesh with either scans 3 or 4 shown below:</p>

<table class="table" style="width:100%">
	<tbody>
		<tr>
			<td style="text-align:center; width:50%"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15065/4.png" style="height:105px; width:101px"></td>
			<td style="text-align:center; width:50%"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15065/5.png" style="height:105px; width:78px"></td>
		</tr>
		<tr>
			<td style="text-align:center; width:50%">Scan 3</td>
			<td style="text-align:center; width:50%">Scan 4</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>Input starts with a line containing three positive integers r c<sub>1</sub> c<sub>2</sub>, indicating the number of rows in both scans and the number of columns in the left hand and right hand scans. Following this are r lines each containing c<sub>1</sub> characters – this is the left hand scan. All characters in the scan are either a ‘0’ or a ‘1’. Following this are r lines each with c<sub>2</sub> characters specifying the right hand scan. The maximum value for r, c<sub>1</sub> and c<sub>2</sub> is 20. In all test cases, the first column of the left hand scan and the last column of the right hand scan contain all ‘1’s.</p>

### 출력 

 <p>Display Yes if the two scans can be meshed together, or No otherwise. After the scans are connected, no portion of the left hand scan should extend beyond the right hand scan, and vice-versa.</p>

