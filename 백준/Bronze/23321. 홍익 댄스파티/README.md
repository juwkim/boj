# [Bronze I] 홍익 댄스파티 - 23321 

[문제 링크](https://www.acmicpc.net/problem/23321) 

### 성능 요약

메모리: 117436 KB, 시간: 136 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>10년 전, 홍익대학교 학생을 위한 댄스파티가 개최되었다.</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 350px;">
	<thead>
		<tr>
			<th scope="col" style="width:50px;text-align: center;"> </th>
			<th scope="col" style="width:100px;text-align: center;">도약 준비</th>
			<th scope="col" style="width:100px;text-align: center;">도약 중</th>
			<th scope="col" style="width:100px;text-align: center;">착석</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">.</td>
			<td style="text-align: center;">o</td>
			<td style="text-align: center;">.</td>
		</tr>
		<tr>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">o</td>
			<td style="text-align: center;">w</td>
			<td style="text-align: center;">.</td>
		</tr>
		<tr>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">m</td>
			<td style="text-align: center;">l</td>
			<td style="text-align: center;">o</td>
		</tr>
		<tr>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">l</td>
			<td style="text-align: center;">n</td>
			<td style="text-align: center;">L</td>
		</tr>
		<tr>
			<td style="text-align: center;">5</td>
			<td style="text-align: center;">n</td>
			<td style="text-align: center;">.</td>
			<td style="text-align: center;">n</td>
		</tr>
	</tbody>
</table>

<p>댄스파티에는 위와 같이 세 종류의 학생이 있다.</p>

<p>학생들은 빈자리 없이 좌우로 딱 붙어 한 줄로 서서, 다음 차례가 되면 <code>도약 준비</code> 학생은 <code>도약 중</code>으로, <code>도약 중</code> 학생은 <code>도약 준비</code>로 바뀐다. <code>착석</code> 학생은 바뀌지 않는다.</p>

<p>당신은 댄스파티의 모습을 한 장의 사진에 담았다.</p>

<p>그리고 10년이 흐른 지금, 대학을 졸업하고 사회인이 된 당신은 짐을 정리하던 도중 댄스파티의 사진을 발견하였다. 그 낡은 단 한 장의 사진은 하루가 바쁘게 일상에 치이며 살아가는 당신을 추억에 잠기게 하기에 충분하였다.</p>

<p>그 시절을 회상하기 위해 주어진 사진을 토대로 다음 차례의 모습을 유추하라.</p>

### 입력 

 <p>댄스파티의 사진이 $5$줄의 문자열로 주어진다.</p>

<p>각 줄의 최대 길이는 $10\,000$자이며 모든 줄의 길이는 동일하다.</p>

<p>각 열은 <code>도약 준비</code>, <code>도약 중</code>, <code>착석</code> 중 하나이다.</p>

### 출력 

 <p>입력으로 주어진 댄스파티 사진의 다음 차례의 모습을 $5$줄의 문자열로 출력한다.</p>

