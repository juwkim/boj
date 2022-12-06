# [Bronze III] 영리한 아리의 포탈 타기 - 25165 

[문제 링크](https://www.acmicpc.net/problem/25165) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>아리가 보스 몬스터를 잡으러 가려면 광야에 위치한 포탈을 타야만 한다. 하지만 광야에는 아리가 포탈을 타러 가는 것을 방해하려는 보스 몬스터의 오른팔인 부하 몬스터 한 마리도 함께 위치해 있다. 광야는 세로의 길이가 <em>N</em>, 가로의 길이가 <em>M</em> 인 <em>N</em> x <em>M</em> 격자판으로 이루어져 있고 격자판의 왼쪽 윗 칸은 (1, 1)이며 오른쪽 아래 칸은 (<em>N</em>, <em>M</em>)이다. 아리가 처음 위치한 칸은 (1, <em>A<sub>c</sub></em>)이고, 부하 몬스터가 위치한 칸은 (<em>S<sub>r</sub></em>, <em>S<sub>c</sub></em>)이며, 포탈은 (<em>N</em>, <em>M</em>)에 위치해있다. 부하 몬스터의 위치가 (<em>N</em>, <em>M</em>)인 경우는 존재하지 않는다.</p>

<p>부하 몬스터는 처음 위치한 칸에서 움직일 수 없어 아리가 포탈을 타려는 것을 직접적으로 막을 수는 없지만 간접적으로 막기 위해 아리의 움직임에 마법을 걸어두었다. 부하 몬스터가 아리에게 걸어둔 마법은 다음과 같다.</p>

<ul>
	<li>아리의 진행 방향은 왼쪽이나 오른쪽 두 방향 중 하나이다.</li>
	<li>아리의 진행 방향이 왼쪽이었다면 반드시 행의 왼쪽 끝, 오른쪽이었다면 행의 오른쪽 끝까지 이동해야 한다. 한 행의 끝에 도달했다면 아리는 아래 행으로 한 칸 이동한다.</li>
	<li>아리가 아래 행으로 이동하면 아리의 진행 방향은 윗 행에서의 진행 방향의 반대가 된다.</li>
</ul>

<p>예를 들어, 광야의 세로 길이가 5, 가로 길이가 6이고 아리가 처음 위치한 칸이 (1, 3) 일 때, 진행 방향에 따른 아리의 이동 경로는 아래 그림과 같다.</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 900px;">
	<tbody>
		<tr>
			<td style="text-align: center;">아리의 진행 방향이 왼쪽일 때</td>
			<td style="text-align: center;">아리의 진행 방향이 오른쪽일 때</td>
		</tr>
		<tr>
			<td style="text-align: center;"><img alt="" src="" style="width: 298px; height: 250px;"></td>
			<td style="text-align: center;"><img alt="" src="" style="width: 300px; height: 250px;"></td>
		</tr>
	</tbody>
</table>

<p>아리의 움직임이 위와 같이 제한되어 있을 때, 아리는 부하 몬스터를 만날 수도, 만나지 않고 포탈로 바로 갈 수도 있다. 아리가 광야로 출발하기 전, 아리를 도와 부하 몬스터를 만나는지, 만나지 않는지 미리 확인해주도록 하자.</p>

### 입력 

 <p>첫 번째 줄에 광야의 크기를 나타내는 두 정수 <em>N</em>과 <em>M</em>이 주어진다. (2 ≤ <em>N</em>, <em>M</em> ≤ 100)</p>

<p>두 번째 줄에 아리가 처음 위치한 칸의 열의 값을 나타내는 정수 <em>A<sub>c </sub></em>(1 ≤ <em>A<sub>c</sub></em> ≤ <em>M</em>)와 아리의 진행 방향 <em>D</em>가 주어진다. <em>D</em>는 0이나 1로 주어지고, 0이라면 진행 방향이 왼쪽임을, 1이라면 진행 방향이 오른쪽임을 의미한다.</p>

<p>세 번째 줄에 부하 몬스터의 위치를 나타내는 두 정수 <em>S<sub>r</sub></em> (2 ≤ <em>S<sub>r</sub></em> ≤ <em>N</em>), <em>S<sub>c</sub></em> (1 ≤ <em>S<sub>c</sub></em> ≤ <em>M</em>)가 주어진다.</p>

### 출력 

 <p>아리가 부하 몬스터를 만나지 않고 포탈로 바로 갈 수 있다면 첫 번째 줄에 "<code>YES!</code>"를 출력하고 부하 몬스터를 만난다면 "<code>NO...</code>"를 출력한다.</p>

