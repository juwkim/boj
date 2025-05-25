# [Silver II] 파이널 서바이버 - 34003 

[문제 링크](https://www.acmicpc.net/problem/34003) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

수학, 조합론, 확률론

### 제출 일자

2025년 5월 26일 03:10:37

### 문제 설명

<p>메이플스토리2는 30분마다 한 번씩 미니게임을 여는 것으로도 유명하다. 그 중 "파이널 서바이버"는 운 요소로만 승패가 결정되는 특이한 미니게임이다.</p>

<table class="table table-bordered td-center">
	<tbody>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/b58ace62-0298-41c2-bd50-720b05be097b/-/preview/" style="max-width:100%;display:block;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/90fd8779-dba6-423d-b43b-51f2f0985b64/-/preview/" style="max-width:100%;display:block;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/b2fc3bb2-60ce-440a-8756-ecf32938793a/-/preview/" style="max-width:100%;display:block;"></td>
		</tr>
	</tbody>
</table>

<p>$8 \times 8$ 크기를 가진 격자 모양의 블록 위에서 캐릭터가 서 있고, 이 중 $4$개를 제외한 $60$개의 블록이 하나씩 차례대로 사라진다. 남은 $4$개의 블록에 서 있던 사람들 모두가 우승자가 되는 심플한 게임이다. 현재 블록이 $K$ 개 남아있으면 각각의 블록이 사라질 확률은 $\frac{1}{K}$ 으로 동일하다.</p>

<table class="table table-bordered td-center">
	<tbody>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/3eb33788-6bbd-4a74-9bc0-357ce309f749/-/preview/" style="max-width:100%;display:block;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/655bf0be-028d-4504-aa67-a911b81b4643/-/preview/" style="max-width:100%;display:block;"></td>
		</tr>
	</tbody>
</table>

<p>이 게임의 유일한 공략법이 하나 있는데, $4$개의 블록이 만나는 꼭짓점 부분에 서 있으면 우승할 확률이 증가한다. 블록과 캐릭터의 충돌 판정으로 인해서 $4$개 중 하나의 블록이라도 남아있으면 떨어지지 않고 살아남게 되기 때문이다. 따라서 사람들은 모두 $7 \times 7$ 개의 꼭짓점 중 하나를 선택해서 그 자리를 지킨다.</p>

<p>현재 블록의 정보가 주어졌을 때, 우승할 확률이 가장 높은 자리와, 이때의 우승할 확률을 출력해보자.</p>

### 입력 

 <p>$8$ 줄에 걸쳐 현재 블록의 상태를 의미하는 문자열이 주어진다. 각 문자열은 $8$ 개의 <code>O</code> 혹은 <code>X</code> 로 구성되어 있다. $i$ 번째 문자열의 $j$ 번째 문자가 <code>O</code> 라면 $i$ 행 $j$ 열의 블록이 사라지지 않은 상태, <code>X</code> 라면 $i$ 행 $j$ 열의 블록이 사라진 상태를 의미한다. <code>O</code> 의 개수는 $4$ 개를 초과한다.</p>

### 출력 

 <p>첫째 줄에는 $7 \times 7$ 개의 꼭짓점 중, 우승할 확률이 가장 높은 꼭짓점의 행 번호와 열 번호를 공백으로 구분하여 출력한다. 각 행과 열 번호는 $1$ 이상 $7$ 이하의 정수이며, 가장 왼쪽 위의 꼭짓점이 $1\ 1$ 이고, 그 오른쪽이 $1\ 2$, 아래는 $2\ 1$ 이 된다. 우승할 확률이 가장 높은 자리가 여러 개라면 아무거나 출력한다.</p>

<p>둘째 줄에는 우승할 확률을 출력한다. 절대/상대 오차는 $10^{-6}$ 까지 허용한다.</p>

