# [Silver I] 퀼린드롬 (Easy) - 20422 

[문제 링크](https://www.acmicpc.net/problem/20422) 

### 성능 요약

메모리: 111392 KB, 시간: 104 ms

### 분류

구현, 문자열

### 제출 일자

2025년 4월 13일 02:22:56

### 문제 설명

<p><u><strong>입력 제한 외 난이도에 따른 문제의 차이는 없다.</strong></u></p>

<p>상민이는 오랜 고민 끝에, 아주 멋진 닉네임 "<code>qilip</code>" 을 생각해냈다. 오, <a href="https://ko.wikipedia.org/wiki/%ED%9A%8C%EB%AC%B8" rel="nofollow">팰린드롬</a>!.. 이라고 생각했지만..</p>

<p>이 닉네임이 팰린드롬이 되기 위해서는 거꾸로 읽어도 "<code>qilip</code>"로 같은 닉네임이어야 하지만, 거꾸로 읽으면 "<code>piliq</code>" 이므로 이 닉네임은 팰린드롬이 아니었다. 가운데를 기준으로 완전히 거울 대칭처럼 보이는 이 기묘한 문자열을 '퀼린드롬' 이라고 부르자. 예를 들어, "<code>dad</code>"는 팰린드롬 이지만 퀼린드롬은 아니며, "<code>mom</code>" 은 팰린드롬인 동시에 퀼린드롬이다. 모두가 퀼린드롬 닉네임을 탐낸다.</p>

<blockquote>
<p>대영 : 상민아, 내 닉네임도 퀼린드롬으로 만들어줘!</p>

<p>상민 : 닉네임이 뭔데?</p>

<p>대영 : <code>dy2000</code></p>

<p>상민 : <code>dY2000SYb</code></p>

<p>대영 : !</p>
</blockquote>

<p>상민이는 <strong>멋진 퀼린드롬 닉네임</strong>을 만들어달라는 수많은 요청 덕에 일상생활마저 힘들게 되었다. 멋진 퀼린드롬 닉네임이란 원본 닉네임을 <strong>부분 문자열</strong>로 가지면서 퀼린드롬인 닉네임이다. 즉, 만들어진 멋진 퀼린드롬 닉네임의 양쪽 끝을 적절히 지우면 원본 닉네임을 만들 수 있다. 모두가 퀼린드롬에 미쳐있기 때문에, 퀼린드롬으로 만들 수만 있다면 대소문자가 바뀌는 일은 중요하게 생각하지 않는다. 예를 들어, "<code>yoy</code>"는 퀼린드롬이 아니지만, 대문자로 바꾼 "<code>YoY</code>"는 퀼린드롬 이므로 사람들은 충분히 만족한다.</p>

<p>상민이를 위해 <strong>가장 짧고</strong> 멋진 퀼린드롬 닉네임을 만들어주는 프로그램을 만들어주자! 특별히, 원본과 대칭이 같은 문자는 홀수 퀼린드롬의 가운데에 놓일 수 있다.</p>

<p>완전히 같은 모양까지는 아니더라도, "이 정도면 인정이지!"라며 작성한 상민이의 거울 대칭 표는 다음과 같다.</p>

<table class="table table-bordered" style="width : auto;">
	<thead>
		<tr>
			<th align="center" style="text-align: center;">원본</th>
			<th align="center" style="text-align: center;">대칭</th>
			<th align="center" style="text-align: center;">원본</th>
			<th align="center" style="text-align: center;">대칭</th>
			<th align="center" style="text-align: center;">원본</th>
			<th align="center" style="text-align: center;">대칭</th>
			<th align="center" style="text-align: center;">원본</th>
			<th align="center" style="text-align: center;">대칭</th>
			<th align="center" style="text-align: center;">원본</th>
			<th align="center" style="text-align: center;">대칭</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center">A</td>
			<td align="center">A</td>
			<td align="center">N</td>
			<td align="center"> </td>
			<td align="center">a</td>
			<td align="center"> </td>
			<td align="center">n</td>
			<td align="center">n</td>
			<td align="center">0</td>
			<td align="center">0</td>
		</tr>
		<tr>
			<td align="center">B</td>
			<td align="center"> </td>
			<td align="center">O</td>
			<td align="center">O</td>
			<td align="center">b</td>
			<td align="center">d</td>
			<td align="center">o</td>
			<td align="center">o</td>
			<td align="center">1</td>
			<td align="center">1</td>
		</tr>
		<tr>
			<td align="center">C</td>
			<td align="center"> </td>
			<td align="center">P</td>
			<td align="center"> </td>
			<td align="center">c</td>
			<td align="center"> </td>
			<td align="center">p</td>
			<td align="center">q</td>
			<td align="center">2</td>
			<td align="center">S</td>
		</tr>
		<tr>
			<td align="center">D</td>
			<td align="center"> </td>
			<td align="center">Q</td>
			<td align="center"> </td>
			<td align="center">d</td>
			<td align="center">b</td>
			<td align="center">q</td>
			<td align="center">p</td>
			<td align="center">3</td>
			<td align="center">E</td>
		</tr>
		<tr>
			<td align="center">E</td>
			<td align="center">3</td>
			<td align="center">R</td>
			<td align="center"> </td>
			<td align="center">e</td>
			<td align="center"> </td>
			<td align="center">r</td>
			<td align="center">7</td>
			<td align="center">4</td>
			<td align="center"> </td>
		</tr>
		<tr>
			<td align="center">F</td>
			<td align="center"> </td>
			<td align="center">S</td>
			<td align="center">2</td>
			<td align="center">f</td>
			<td align="center"> </td>
			<td align="center">s</td>
			<td align="center"> </td>
			<td align="center">5</td>
			<td align="center">Z</td>
		</tr>
		<tr>
			<td align="center">G</td>
			<td align="center"> </td>
			<td align="center">T</td>
			<td align="center">T</td>
			<td align="center">g</td>
			<td align="center"> </td>
			<td align="center">t</td>
			<td align="center"> </td>
			<td align="center">6</td>
			<td align="center"> </td>
		</tr>
		<tr>
			<td align="center">H</td>
			<td align="center">H</td>
			<td align="center">U</td>
			<td align="center">U</td>
			<td align="center">h</td>
			<td align="center"> </td>
			<td align="center">u</td>
			<td align="center">u</td>
			<td align="center">7</td>
			<td align="center">r</td>
		</tr>
		<tr>
			<td align="center">I</td>
			<td align="center">I</td>
			<td align="center">V</td>
			<td align="center">V</td>
			<td align="center">i</td>
			<td align="center">i</td>
			<td align="center">v</td>
			<td align="center">v</td>
			<td align="center">8</td>
			<td align="center">8</td>
		</tr>
		<tr>
			<td align="center">J</td>
			<td align="center"> </td>
			<td align="center">W</td>
			<td align="center">W</td>
			<td align="center">j</td>
			<td align="center"> </td>
			<td align="center">w</td>
			<td align="center">w</td>
			<td align="center">9</td>
			<td align="center"> </td>
		</tr>
		<tr>
			<td align="center">K</td>
			<td align="center"> </td>
			<td align="center">X</td>
			<td align="center">X</td>
			<td align="center">k</td>
			<td align="center"> </td>
			<td align="center">x</td>
			<td align="center">x</td>
			<td align="center"> </td>
			<td align="center"> </td>
		</tr>
		<tr>
			<td align="center">L</td>
			<td align="center"> </td>
			<td align="center">Y</td>
			<td align="center">Y</td>
			<td align="center">l</td>
			<td align="center">l</td>
			<td align="center">y</td>
			<td align="center"> </td>
			<td align="center"> </td>
			<td align="center"> </td>
		</tr>
		<tr>
			<td align="center">M</td>
			<td align="center">M</td>
			<td align="center">Z</td>
			<td align="center">5</td>
			<td align="center">m</td>
			<td align="center">m</td>
			<td align="center">z</td>
			<td align="center"> </td>
			<td align="center"> </td>
			<td align="center"> </td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>첫 줄에 원본 닉네임 <em>S</em>를 입력받는다.</p>

### 출력 

 <p><strong>가장 짧고</strong> 멋진 퀼린드롬 닉네임을 출력한다. 만약 멋진 퀼린드롬 닉네임을 만들 수 없다면, "<code>-1</code>" 을 출력한다.</p>

