# [Bronze I] 우유가 넘어지면? - 17363 

[문제 링크](https://www.acmicpc.net/problem/17363) 

### 성능 요약

메모리: 29200 KB, 시간: 80 ms

### 분류

구현(implementation)

### 문제 설명

<p>유머 감각이 뛰어난 성원이는 매일 재미있는 농담을 준비한다. 오늘 준비한 농담은 바로 이것이다.</p>

<blockquote>
<p>우유가 넘어질 때 뭐라고 하게? 답은 "아야"! 깔깔!</p>
</blockquote>

<p>친구들의 반응이 심드렁하자, 성원이는 해설을 덧붙였다.</p>

<blockquote>
<p>"우유"가 세로로 적혀 있는 상자를 왼쪽으로 툭 넘어뜨리면 "아야"가 되잖아? 이게 마치 우유가 넘어져서 아파하는 것 같다는 점이 웃음 포인트야!</p>
</blockquote>

<p style="margin-bottom: 20px;"><img alt="milk" src="" style="display: block; margin-left: auto; margin-right: auto; width: 100%; max-width: 300px;"></p>

<p>그럼에도 불구하고 친구들이 웃지 않자, 성원이는 친구들이 공간지각력이 부족해 상자를 넘어뜨리는 모습을 상상하지 못한다고 생각했다. 그래서 상자를 넘어뜨리는 프로그램을 만들어 친구들에게 결과를 보여주기로 했다.</p>

<p>성원이는 상자에 "우유"가 아니라 다른 그림이 그려져 있어도 프로그램이 잘 동작하기를 원한다. 성원이는 상자의 면을 격자로 나누고 각 칸에 아래 문자들 중 하나를 그려 넣는 방식으로 그림을 그린다.</p>

<table class="table table-bordered" style="margin-left: auto; margin-right: auto; width: 360px;">
	<tbody>
		<tr>
			<th style="text-align: center; width: 80px;">문자</th>
			<th style="text-align: center; width: 120px;">이름</th>
			<th style="text-align: center; width: 80px;">ASCII</th>
			<th style="text-align: center; width: 80px;">돌린 뒤</th>
		</tr>
		<tr>
			<td style="text-align: center;"><code>.</code></td>
			<td style="text-align: center;">온점</td>
			<td style="text-align: center;">46</td>
			<td style="text-align: center;"><code>.</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>O</code></td>
			<td style="text-align: center;">대문자 O</td>
			<td style="text-align: center;">79</td>
			<td style="text-align: center;"><code>O</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>-</code></td>
			<td style="text-align: center;">하이픈</td>
			<td style="text-align: center;">45</td>
			<td style="text-align: center;"><code>|</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>|</code></td>
			<td style="text-align: center;">세로 바</td>
			<td style="text-align: center;">124</td>
			<td style="text-align: center;"><code>-</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>/</code></td>
			<td style="text-align: center;">슬래시</td>
			<td style="text-align: center;">47</td>
			<td style="text-align: center;"><code>\</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>\</code></td>
			<td style="text-align: center;">역슬래시</td>
			<td style="text-align: center;">92</td>
			<td style="text-align: center;"><code>/</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>^</code></td>
			<td style="text-align: center;">캐럿</td>
			<td style="text-align: center;">94</td>
			<td style="text-align: center;"><code><</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code><</code></td>
			<td style="text-align: center;">왼쪽 부등호</td>
			<td style="text-align: center;">60</td>
			<td style="text-align: center;"><code>v</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>v</code></td>
			<td style="text-align: center;">소문자 V</td>
			<td style="text-align: center;">118</td>
			<td style="text-align: center;"><code>></code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>></code></td>
			<td style="text-align: center;">오른쪽 부등호</td>
			<td style="text-align: center;">62</td>
			<td style="text-align: center;"><code>^</code></td>
		</tr>
	</tbody>
</table>

<p>그러나 성원이는 내일의 농담을 생각하느라 프로그램을 만들 시간이 없다. 성원이 대신 프로그램을 만들어 주자.</p>

### 입력 

 <p>첫 줄에 그림의 세로 길이와 가로 길이를 의미하는 정수 <em>N</em>과 <em>M</em>(1 ≤ <em>N</em>, <em>M</em> ≤ 100)이 주어진다.</p>

<p>다음 <em>N</em>개의 줄에 걸쳐 그림의 각 줄을 의미하는 <em>M</em>글자의 문자열이 하나씩 주어진다. 문자열은 공백을 포함하지 않으며 위의 표에 주어진 문자로만 이루어져 있음이 보장된다.</p>

### 출력 

 <p><em>M</em>개의 줄에 걸쳐 입력된 그림을 왼쪽으로 넘어뜨렸을 때의 결과를 출력한다.</p>

