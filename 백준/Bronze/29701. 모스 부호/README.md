# [Bronze II] 모스 부호 - 29701 

[문제 링크](https://www.acmicpc.net/problem/29701) 

### 성능 요약

메모리: 113112 KB, 시간: 124 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현

### 문제 설명

<p>혜민이는 요즘 모스 부호에 관심이 많아졌다. 모스 부호는 짧은 신호와 긴 신호를 적절히 조합하여 문자 기호를 표기하는 방식이다. 각 문자를 나타내는 방식은 미리 정해져 있는데, 예를 들어, 짧은 신호를 '<span style="color:#e74c3c;"><code>.</code></span>', 긴 신호를 '<span style="color:#e74c3c;"><code>-</code></span>'로 나타낸다면, 모스 부호로 알파벳 'A'는 '.-', 숫자 1은 '.----'와 같이 표기할 수 있다. 모스 부호를 알고 있으면 위험한 상황에서 구조 요청을 하는 데 유용할 것 같아, 혜민이는 평상시에 친구들과 연락을 주고받을 때도 모스 부호를 사용하려고 한다. 혜민이는 친구들이 보내온 모스 부호를 올바르게 해독했는지 바로바로 확인하고 싶어졌다. 알파벳 A-Z, 숫자 0-9, 기호 '<code>,</code>', '<code>.</code>', '<code>?</code>', '<code>:</code>', '<code>-</code>', '<code>@</code>'로 이루어진 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>인 문자열을 변환한 모스 부호가 주어질 때, 주어진 모스 부호를 해독하여 원래의 문자열을 출력하는 프로그램을 작성해 보자.</p>

<p>각 문자를 모스 부호로 나타내는 방법은 아래 표에 정리되어 있다. (단, 표의 둘째, 넷째 열은 첫째, 셋째 열의 문자를 모스 부호로 변환한 결과를 나타내며, '<span style="color:#e74c3c;"><code>.</code></span>'는 짧은 신호를, '<span style="color:#e74c3c;"><code>-</code></span>'는 긴 신호를 의미한다.)</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 500px;">
	<tbody>
		<tr>
			<td style="text-align: center;">A</td>
			<td style="text-align: center;">.-</td>
			<td style="text-align: center;">B</td>
			<td style="text-align: center;">-...</td>
		</tr>
		<tr>
			<td style="text-align: center;">C</td>
			<td style="text-align: center;">-.-.</td>
			<td style="text-align: center;">D</td>
			<td style="text-align: center;">-..</td>
		</tr>
		<tr>
			<td style="text-align: center;">E</td>
			<td style="text-align: center;">.</td>
			<td style="text-align: center;">F</td>
			<td style="text-align: center;">..-.</td>
		</tr>
		<tr>
			<td style="text-align: center;">G</td>
			<td style="text-align: center;">--.</td>
			<td style="text-align: center;">H</td>
			<td style="text-align: center;">....</td>
		</tr>
		<tr>
			<td style="text-align: center;">I</td>
			<td style="text-align: center;">..</td>
			<td style="text-align: center;">J</td>
			<td style="text-align: center;">.---</td>
		</tr>
		<tr>
			<td style="text-align: center;">K</td>
			<td style="text-align: center;">-.-</td>
			<td style="text-align: center;">L</td>
			<td style="text-align: center;">.-..</td>
		</tr>
		<tr>
			<td style="text-align: center;">M</td>
			<td style="text-align: center;">--</td>
			<td style="text-align: center;">N</td>
			<td style="text-align: center;">-.</td>
		</tr>
		<tr>
			<td style="text-align: center;">O</td>
			<td style="text-align: center;">---</td>
			<td style="text-align: center;">P</td>
			<td style="text-align: center;">.--.</td>
		</tr>
		<tr>
			<td style="text-align: center;">Q</td>
			<td style="text-align: center;">--.-</td>
			<td style="text-align: center;">R</td>
			<td style="text-align: center;">.-.</td>
		</tr>
		<tr>
			<td style="text-align: center;">S</td>
			<td style="text-align: center;">...</td>
			<td style="text-align: center;">T</td>
			<td style="text-align: center;">-</td>
		</tr>
		<tr>
			<td style="text-align: center;">U</td>
			<td style="text-align: center;">..-</td>
			<td style="text-align: center;">V</td>
			<td style="text-align: center;">...-</td>
		</tr>
		<tr>
			<td style="text-align: center;">W</td>
			<td style="text-align: center;">.--</td>
			<td style="text-align: center;">X</td>
			<td style="text-align: center;">-..-</td>
		</tr>
		<tr>
			<td style="text-align: center;">Y</td>
			<td style="text-align: center;">-.--</td>
			<td style="text-align: center;">Z</td>
			<td style="text-align: center;">--..</td>
		</tr>
		<tr>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">.----</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">..---</td>
		</tr>
		<tr>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">...--</td>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">....-</td>
		</tr>
		<tr>
			<td style="text-align: center;">5</td>
			<td style="text-align: center;">.....</td>
			<td style="text-align: center;">6</td>
			<td style="text-align: center;">-....</td>
		</tr>
		<tr>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;">--...</td>
			<td style="text-align: center;">8</td>
			<td style="text-align: center;">---..</td>
		</tr>
		<tr>
			<td style="text-align: center;">9</td>
			<td style="text-align: center;">----.</td>
			<td style="text-align: center;">0</td>
			<td style="text-align: center;">-----</td>
		</tr>
		<tr>
			<td style="text-align: center;">,</td>
			<td style="text-align: center;">--..--</td>
			<td style="text-align: center;">.</td>
			<td style="text-align: center;">.-.-.-</td>
		</tr>
		<tr>
			<td style="text-align: center;">?</td>
			<td style="text-align: center;">..--..</td>
			<td style="text-align: center;">:</td>
			<td style="text-align: center;">---...</td>
		</tr>
		<tr>
			<td style="text-align: center;">-</td>
			<td style="text-align: center;">-....-</td>
			<td style="text-align: center;">@</td>
			<td style="text-align: center;">.--.-.</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>첫째 줄에 모스 부호로 변환하기 전 문자열의 길이를 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N(1 \leq N \leq 100)$</span></mjx-container>이 주어진다.</p>

<p>둘째 줄에 원래의 문자열을 모스 부호로 변환한 메시지가 주어진다. 이 메시지에서 짧은 신호는 '<span style="color:#e74c3c;"><code>.</code></span>', 긴 신호는 '<span style="color:#e74c3c;"><code>-</code></span>'로 나타내며, 원래의 문자열을 구성하는 각각의 문자를 모스 부호로 변환한 결과는 공백으로 구분되어 있다.</p>

<p>위 표를 이용해 해독할 수 없는 메시지는 주어지지 않는다.</p>

### 출력 

 <p>주어진 모스 부호를 해독하여 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>인 문자열을 공백 없이 출력한다.</p>

<p>알파벳의 경우, 반드시 대문자로 출력한다.</p>

