# [Silver II] 화살표 연산자 - 16114 

[문제 링크](https://www.acmicpc.net/problem/16114) 

### 성능 요약

메모리: 108080 KB, 시간: 92 ms

### 분류

많은 조건 분기, 구현

### 제출 일자

2024년 12월 6일 05:11:59

### 문제 설명

<p><em>NOTE: 이 문제의 내용은 C++11 이후의 표준을 따릅니다.</em></p>

<p>새내기들을 위해 C++ 스터디를 준비하던 키파는 인터넷에서 신기한 연산자를 발견했다. 바로 화살표 연산자(<code><--</code>)이다.</p>

<table border="1" bordercolor="black" cellpadding="0" cellspacing="0" class="table table-bordered">
	<thead>
		<tr>
			<td style="text-align:center; width:40%;">프로그램</td>
			<td style="text-align:center; width:40%;">출력</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="padding-left: 8px;"><code style="padding: 0px;">#include <iostream><br>
			<br>
			int main(){<br>
			  int x = 10;<br>
			<br>
			  while( 0 <-- x ){<br>
			    std::cout << x << std::endl;<br>
			  }<br>
			  return 0;<br>
			}</code></td>
			<td style="padding-left: 8px; vertical-align: middle;"><code style="padding: 0px;">9<br>
			8<br>
			7<br>
			6<br>
			5<br>
			4<br>
			3<br>
			2<br>
			1</code></td>
		</tr>
	</tbody>
</table>

<p>위와 같이 화살표 연산자를 사용하면 연산자 오른쪽에 있는 변수가 연산자 왼쪽의 값을 향해 다가간다! 심지어 이 연산자는 화살표의 길이(<code>-</code>의 개수)를 늘려서 값이 바뀌는 속도를 더 빠르게 할 수도 있다.</p>

<table border="1" bordercolor="black" cellpadding="0" cellspacing="0" class="table table-bordered">
	<thead>
		<tr>
			<td style="text-align:center; width:40%;">프로그램</td>
			<td style="text-align:center; width:40%;">출력</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="padding: 8px;"><code style="padding: 0px;">#include <iostream><br>
			<br>
			int main(){<br>
			  int x = 10;<br>
			<br>
			  while( 0 <---- x ){<br>
			    std::cout << x << std::endl;<br>
			  }<br>
			  return 0;<br>
			}</code></td>
			<td style="padding: 8px; vertical-align: middle;"><code style="padding: 0px;">8<br>
			6<br>
			4<br>
			2</code></td>
		</tr>
	</tbody>
</table>

<p>화살표의 길이가 2인 첫 번째 코드에서는 수가 9개 출력되었으나, 길이를 4로 늘린 두 번째 코드에서는 수가 4개밖에 출력되지 않았다. 변수가 2배 빠르게 값으로 다가간 것이다!</p>

<hr>
<p>사실 이 화살표 연산자는 전위 감소 연산자(prefix decrement operator, <code>--x</code>)를 이용한 농담으로, <code>0 <-- x</code>은 <code>--x > 0</code>을 화살표처럼 보이도록 눈속임한 것이다. 따라서 첫 번째 코드의 반복문은 아래와 같이 동작한다.</p>

<ol>
	<li><code>x</code>의 값을 1 감소시킨다.</li>
	<li>만약 <code>x</code>의 값이 0보다 크지 않다면 프로그램을 종료한다.</li>
	<li><code>x</code>의 값을 출력하고 처음으로 돌아간다.</li>
</ol>

<p>감소 연산자는 아래와 같은 특징이 있다.</p>

<ul>
	<li><code>-</code>가 여러 개 연속되어 있을 때는 반드시 앞에서부터 두 개씩 끊어서 해석된다. 예를 들어 <code>------x</code>는 <code>-- - -- -x</code> 또는 <code>- -- - --x</code> 등이 아니라 반드시 <code>-- -- --x</code>로 해석된다.</li>
	<li>감소 연산자는 단항 부정 연산자(unary minus operator, <code>-x</code>)가 적용된 식에는 적용할 수 없다. 예를 들어 <code>-----x</code>는 <code>-- -- -x</code>로 해석되고, 감소 연산자가 <code>-x</code>에 적용되었으므로 컴파일에 실패한다.</li>
</ul>

<p>두 번째 코드의 <code>0 <---- x</code>는 <code>-- --x > 0</code>과 같고, 감소 연산자가 두 번 적용되었으므로 <code>x</code>의 값이 한번에 2씩 줄어든다.</p>

<p>위의 코드에서 <code>x</code>의 초기값과 화살표의 길이를 바꿨을 때, 몇 개의 수가 출력될지 예상해 보자.</p>

### 입력 

 <p>첫 줄에 변수 <code>x</code>의 초기값을 뜻하는 정수 <em>X</em>와 화살표의 길이를 뜻하는 정수 <em>N</em>(-100 ≤ <em>X</em> ≤ 100, 0 ≤ <em>N</em> ≤ 10)이 주어진다.</p>

### 출력 

 <p>첫째 줄에 프로그램의 실행 결과를 출력한다.</p>

<ul>
	<li>만약 프로그램이 정상적으로 종료된다면 프로그램이 출력한 수의 개수를 출력한다.</li>
	<li>만약 프로그램이 무한히 많은 수를 출력한다면 <code>INFINITE</code>를 출력한다.</li>
	<li>만약 프로그램이 지문에 주어진 조건에 의해 컴파일에 실패할 경우 <code>ERROR</code>를 출력한다. </li>
</ul>

