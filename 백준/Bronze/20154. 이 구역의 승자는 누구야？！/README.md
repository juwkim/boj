# [Bronze I] 이 구역의 승자는 누구야?! - 20154 

[문제 링크](https://www.acmicpc.net/problem/20154) 

### 성능 요약

메모리: 32796 KB, 시간: 312 ms

### 분류

수학(math), 문자열(string)

### 문제 설명

<p>가톨릭대학교에 다니는 컴퓨터정보공학부 황톨릭은 코로나 때문에 슬퍼하는 친구들을 위해 게임을 하나 만들었다.</p>

<p>게임이 시작되면 알파벳 대문자로만 이루어진 문자열이 주어진다. 문자열이 주어지면 각 문자의 획수로 문자를 변환한다. 획수들을 갖고 앞에서부터 두 개씩 더해가는데 만약 짝이 지어지지 않는다면 그대로 다음 단계로 내려간다. 다음 단계부터는 이전 단계에서 두 개씩 더해가며 생성된 숫자들을 가지고 같은 과정을 반복한다. 과정을 반복하다가 결국 마지막 한 개의 수가 남았을 때 그 수가 홀수라면 이기는 것이고 짝수라면 지는 게임이다!!</p>

<p>예를 들어 "<code>ABCDE</code>"라는 문자열이 주어지면 ‘<code>A</code>’, ‘<code>B</code>’, ‘<code>C</code>’, ‘<code>D</code>’, ‘<code>E</code>’ 각 문자의 획수인 3, 2, 1, 2, 3으로 바꾸어 아래의 그림처럼 과정을 진행한다. 단, 계산할 때, 더한 값이 10을 넘는다면 10으로 나눈 나머지로 바꿔준다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 929px; height: 150px;"></p>

<p>‘<code>E</code>’의 경우는 짝을 지을 수 없으므로 3이 바로 내려오게 된다. 결국, 마지막 남은 수가 1인 홀수이므로 이 게임은 이기게 되는 것이다.</p>

<p>게임의 심판역할인 톨릭이는 매번 계산하는 게 귀찮아 코드를 짜놓고 싶어한다. 톨릭이를 도와 코드를 짜주자!!</p>

<p>알파벳 대문자의 획수는 아래 표와 같다.</p>

<table class="table table-bordered table-center-90 td-center">
	<tbody>
		<tr>
			<td>A</td>
			<td>B</td>
			<td>C</td>
			<td>D</td>
			<td>E</td>
			<td>F</td>
			<td>G</td>
			<td>H</td>
			<td>I</td>
			<td>J</td>
			<td>K</td>
			<td>L</td>
			<td>M</td>
			<td>N</td>
			<td>O</td>
			<td>P</td>
			<td>Q</td>
			<td>R</td>
			<td>S</td>
			<td>T</td>
			<td>U</td>
			<td>V</td>
			<td>W</td>
			<td>X</td>
			<td>Y</td>
			<td>Z</td>
		</tr>
		<tr>
			<td>3</td>
			<td>2</td>
			<td>1</td>
			<td>2</td>
			<td>3</td>
			<td>3</td>
			<td>3</td>
			<td>3</td>
			<td>1</td>
			<td>1</td>
			<td>3</td>
			<td>1</td>
			<td>3</td>
			<td>3</td>
			<td>1</td>
			<td>2</td>
			<td>2</td>
			<td>2</td>
			<td>1</td>
			<td>2</td>
			<td>1</td>
			<td>1</td>
			<td>2</td>
			<td>2</td>
			<td>2</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>첫째 줄에 알파벳 대문자로만 이루어진 길이 <em>K</em>(1 ≤ <em>K</em> ≤ 1,000,000)인 문자열 S가 주어진다.</p>

### 출력 

 <p>첫째 줄에 정답을 출력한다.</p>

<p>마지막으로 남은 수가 홀수라면 "<code>I'm a winner!</code>"를 출력하고 0이거나 짝수라면 "<code>You're the winner?</code>"를 출력한다.</p>

