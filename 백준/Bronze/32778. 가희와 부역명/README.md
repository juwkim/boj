# [Bronze III] 가희와 부역명 - 32778 

[문제 링크](https://www.acmicpc.net/problem/32778) 

### 성능 요약

메모리: 108080 KB, 시간: 96 ms

### 분류

파싱, 문자열

### 제출 일자

2024년 12월 2일 22:41:49

### 문제 설명

<p>지하철역 중에, 역 이름 뒤에 다른 이름 부역명이 괄호 안에 붙은 것을 종종 볼 수 있습니다. 예를 들어, 숭실대입구역은 부역명으로 살피재가 붙습니다. 역 정보가 주어졌을 때, 역명과 부역명을 출력해 주세요.</p>

### 입력 

 <p>첫 번째 줄에 역 정보가 주어집니다. 역 정보는 아래 두 형식 중 하나로 주어집니다.</p>

<ul>
	<li>{<code>station_name</code>}</li>
	<li>{<code>station_name</code>} {<code>open_character</code>}{<code>sub_station_name</code>}{<code>close_character</code>}</li>
</ul>

<p><code>station_name</code>은 역명을, <code>sub_station_name</code>은 부역명을 의미합니다.</p>

<p>또한, 두 번째 형식으로 주어지는 경우, <code>open_character</code>는 '<span style="color:#e74c3c;"><code>(</code></span>'로, <code>close_character</code>는 '<span style="color:#e74c3c;"><code>)</code></span>'로 주어집니다.</p>

### 출력 

 <p>첫 번째 줄에 역명을, 두 번째 줄에 부역명을 출력해 주세요. 만약, 부역명이 없다면, 부역명을 출력할 때 '<span style="color:#e74c3c;"><code>-</code></span>'를 출력해 주세요.</p>

